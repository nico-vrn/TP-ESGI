import sys
import os
import io
import re
from pcpp import Preprocessor as PCPPPreprocessor
from pycparser import c_parser, c_ast
from makeelf.elf import ELF, EM

# Préprocesseur
class Preprocessor:
    def __init__(self, filename):
        self.filename = filename

    def preprocess(self):
        pp = PCPPPreprocessor()
        pp.add_path(os.path.dirname(self.filename))
        pp.add_path("headers")  # Add your headers folder path
        
        with open(self.filename, 'r') as f:
            content = f.read()
        
        output = io.StringIO()
        pp.parse(content)
        pp.write(output)
        return output.getvalue()

# Analyse lexicale
def tokenize(code):
    token_specification = [
        ('PREPROCESSOR', r'#.*'),  # Handle preprocessor directives
        ('KEYWORD', r'\b(int|return|if|else|while|for|void|char|float|double)\b'),
        ('ID', r'[A-Za-z_]\w*'),
        ('NUMBER', r'\d+(\.\d*)?'),  # Handle numbers and floats
        ('STRING', r'"[^"]*"'),
        ('OP', r'[+\-*/=<>!]=?|&&|\|\||[%^]'),  # Added more operators
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('SEMI', r';'),
        ('COMMA', r','),
        ('DOT', r'\.'),  # Added dot
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),  # Catch all other characters
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE' or kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        elif kind == 'PREPROCESSOR':
            continue  # Skip preprocessor directives
        else:
            tokens.append((kind, value))
    tokens.append(('EOF', 'EOF'))  # Add EOF token at the end
    return tokens

# Analyse syntaxique
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        return self.program()

    def program(self):
        functions = []
        while not self.is_at_end():
            if self.match('KEYWORD', 'int') and self.look_ahead('ID') and self.look_ahead('LPAREN', 2):
                functions.append(self.function())
            else:
                self.skip_declaration()  # Skip non-function declarations
        return {'type': 'Program', 'functions': functions}

    def function(self):
        return_type = self.consume('KEYWORD')
        name = self.consume('ID')
        self.consume('LPAREN')
        self.consume('RPAREN')
        body = self.block()
        return {'type': 'Function', 'return_type': return_type, 'name': name, 'body': body}

    def block(self):
        statements = []
        self.consume('LBRACE')
        while not self.check('RBRACE'):
            statements.append(self.statement())
        self.consume('RBRACE')
        return statements

    def statement(self):
        if self.match('KEYWORD', 'int'):
            return self.var_declaration()
        elif self.match('KEYWORD', 'return'):
            return self.return_statement()
        else:
            return self.expression_statement()

    def var_declaration(self):
        self.consume('KEYWORD', 'int')
        name = self.consume('ID')
        self.consume('OP', '=')
        value = self.expression()
        self.consume('SEMI')
        return {'type': 'VarDeclaration', 'name': name, 'value': value}

    def return_statement(self):
        self.consume('KEYWORD', 'return')
        value = self.expression()
        self.consume('SEMI')
        return {'type': 'ReturnStatement', 'value': value}

    def expression_statement(self):
        expr = self.expression()
        self.consume('SEMI')
        return {'type': 'ExpressionStatement', 'expression': expr}

    def expression(self):
        return self.additive()

    def additive(self):
        expr = self.multiplicative()
        while self.match('OP', '+') or self.match('OP', '-'):
            operator = self.previous()[1]
            right = self.multiplicative()
            expr = {'type': 'BinaryOp', 'operator': operator, 'left': expr, 'right': right}
        return expr

    def multiplicative(self):
        expr = self.primary()
        while self.match('OP', '*') or self.match('OP', '/'):
            operator = self.previous()[1]
            right = self.primary()
            expr = {'type': 'BinaryOp', 'operator': operator, 'left': expr, 'right': right}
        return expr

    def primary(self):
        if self.match('NUMBER'):
            return {'type': 'Number', 'value': int(self.previous()[1])}
        elif self.match('ID'):
            return {'type': 'Variable', 'name': self.previous()[1]}
        self.consume('LPAREN')
        expr = self.expression()
        self.consume('RPAREN')
        return expr

    def match(self, *types):
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False

    def check(self, t, value=None):
        if self.is_at_end():
            return False
        if value:
            return self.tokens[self.current][0] == t and self.tokens[self.current][1] == value
        return self.tokens[self.current][0] == t

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.tokens[self.current][0] == 'EOF'

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, t, value=None):
        if self.check(t, value):
            return self.advance()[1]
        raise Exception(f"Expected {t} {value}, got {self.tokens[self.current]}")

    def skip_declaration(self):
        nest_level = 0
        while not self.is_at_end():
            if self.check('SEMI') and nest_level == 0:
                self.advance()
                return
            elif self.check('LBRACE'):
                nest_level += 1
            elif self.check('RBRACE'):
                if nest_level == 0:
                    self.advance()
                    return
                nest_level -= 1
            self.advance()

    def look_ahead(self, token_type, offset=1):
        if self.current + offset < len(self.tokens):
            return self.tokens[self.current + offset][0] == token_type
        return False

# Analyse sémantique
class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def analyze(self):
        self.visit(self.ast)

    def visit(self, node):
        method = 'visit_' + node['type']
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for key, value in node.items():
            if isinstance(value, dict):
                self.visit(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.visit(item)

    def visit_Program(self, node):
        for function in node['functions']:
            self.visit(function)

    def visit_Function(self, node):
        self.symbol_table = {}
        self.visit(node['body'])

    def visit_VarDeclaration(self, node):
        self.symbol_table[node['name']] = 'int'
        self.visit(node['value'])

    def visit_ReturnStatement(self, node):
        self.visit(node['value'])

    def visit_ExpressionStatement(self, node):
        self.visit(node['expression'])

    def visit_BinaryOp(self, node):
        self.visit(node['left'])
        self.visit(node['right'])

    def visit_Number(self, node):
        pass

    def visit_Variable(self, node):
        if node['name'] not in self.symbol_table:
            raise Exception(f"Undeclared variable '{node['name']}'")

# Génération de code intermédiaire
class IntermediateCodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.temp_counter = 0
        self.current_temp = None

    def generate(self):
        self.visit(self.ast)
        return self.code

    def visit(self, node):
        method = 'visit_' + node['type']
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for key, value in node.items():
            if isinstance(value, dict):
                self.visit(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.visit(item)

    def visit_Program(self, node):
        for function in node['functions']:
            self.visit(function)

    def visit_Function(self, node):
        self.code.append(f"FUNCTION {node['name']}")
        self.visit(node['body'])
        self.code.append("END_FUNCTION")

    def visit_VarDeclaration(self, node):
        self.visit(node['value'])
        self.code.append(f"{node['name']} = {self.current_temp}")

    def visit_ReturnStatement(self, node):
        self.visit(node['value'])
        self.code.append(f"RETURN {self.current_temp}")

    def visit_ExpressionStatement(self, node):
        self.visit(node['expression'])

    def visit_BinaryOp(self, node):
        self.visit(node['left'])
        left_temp = self.current_temp
        self.visit(node['right'])
        right_temp = self.current_temp
        self.current_temp = self.new_temp()
        self.code.append(f"{self.current_temp} = {left_temp} {node['operator']} {right_temp}")

    def visit_Number(self, node):
        self.current_temp = self.new_temp()
        self.code.append(f"{self.current_temp} = {node['value']}")

    def visit_Variable(self, node):
        self.current_temp = self.new_temp()
        self.code.append(f"{self.current_temp} = {node['name']}")

    def new_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

# Optimisation du code intermédiaire
class Optimizer:
    def __init__(self, intermediate_code):
        self.code = intermediate_code

    def optimize(self):
        # Implement optimization techniques here
        return self.code

# Génération de code assembleur
class AssemblyGenerator:
    def __init__(self, intermediate_code):
        self.code = intermediate_code
        self.assembly = []

    def generate(self):
        for line in self.code:
            if line.startswith("FUNCTION"):
                self.assembly.append(f"{line.split()[1]}:")
            elif line.startswith("RETURN"):
                self.assembly.append(f"  mov eax, {line.split()[1]}")
                self.assembly.append("  ret")
            elif line == "END_FUNCTION":
                pass
            else:
                self.assembly.append(f"  {line}")
        return self.assembly

# Création du fichier ELF
class ELFGenerator:
    def __init__(self, assembly_code):
        self.assembly = assembly_code

    def generate(self, output_file):
        elf = ELF(e_machine=EM.EM_386)
        # Convert assembly to binary
        binary_code = self.assemble(self.assembly)
        
        # Vérification du type de binary_code
        if not isinstance(binary_code, bytes):
            raise TypeError("binary_code should be of type bytes")

        code_section = elf.append_section('.text', 0x08048000, binary_code)  # Add address 0x08048000
        code_section.header.sh_flags = 0x6  # Allocatable and Executable
        elf.append_section('.shstrtab', b'\x00.text\x00.shstrtab\x00')
        elf.write(output_file)

    def assemble(self, assembly):
        # This is a placeholder function, in a real compiler this should convert assembly to binary
        binary = b""
        for line in assembly:
            # A real assembler would convert each line to machine code
            # For now, we'll just append a NOP (0x90) for each line for simplicity
            binary += b'\x90'
        return binary

# Fonction principale de compilation
def compile_c(input_file, output_file):
    try:
        # Preprocessing
        preprocessor = Preprocessor(input_file)
        preprocessed_code = preprocessor.preprocess()

        # Afficher le code préprocessé pour le débogage
        print("Preprocessed Code:\n", preprocessed_code)

        # Lexical analysis
        tokens = tokenize(preprocessed_code)
        
        # Afficher les tokens pour le débogage
        print("Tokens:\n", tokens)

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Semantic analysis
        semantic_analyzer = SemanticAnalyzer(ast)
        semantic_analyzer.analyze()

        # Intermediate code generation
        icg = IntermediateCodeGenerator(ast)
        intermediate_code = icg.generate()

        # Optimization
        optimizer = Optimizer(intermediate_code)
        optimized_code = optimizer.optimize()

        # Assembly code generation
        assembly_generator = AssemblyGenerator(optimized_code)
        assembly_code = assembly_generator.generate()

        # ELF file generation
        elf_generator = ELFGenerator(assembly_code)
        elf_generator.generate(output_file)

        print(f"Compilation successful. Output file: {output_file}")
    except Exception as e:
        print(f"An error occurred during compilation: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compiler.py <input_file.c> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    compile_c(input_file, output_file)

