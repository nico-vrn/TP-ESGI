import re

# Preprocessor
class Preprocessor:
    def __init__(self, code):
        self.code = code
        self.defines = {}
        self.lines = self.code.splitlines()

    def preprocess(self):
        self.handle_defines()
        self.handle_includes()
        return "\n".join(self.lines)
    
    def handle_defines(self):
        new_lines = []
        for line in self.lines:
            match = re.match(r'#define (\w+) (.+)', line)
            if match:
                name, value = match.groups()
                self.defines[name] = value
            else:
                new_lines.append(self.replace_defines(line))
        self.lines = new_lines

    def replace_defines(self, line):
        for name, value in self.defines.items():
            line = line.replace(name, value)
        return line
    
    def handle_includes(self):
        new_lines = []
        for line in self.lines:
            match = re.match(r'#include "(.+)"', line)
            if match:
                filename = match.group(1)
                with open(filename, 'r') as f:
                    included_code = f.read()
                preprocessor = Preprocessor(included_code)
                included_lines = preprocessor.preprocess().splitlines()
                new_lines.extend(included_lines)
            else:
                new_lines.append(line)
        self.lines = new_lines

# AST Node Classes
class ASTNode:
    pass

class Expression(ASTNode):
    pass

class Program(ASTNode):
    def __init__(self, functions):
        self.functions = functions

class Function(ASTNode):
    def __init__(self, return_type, name, body):
        self.return_type = return_type
        self.name = name
        self.body = body

class Statement(ASTNode):
    pass

class ReturnStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

class VariableDeclaration(Statement):
    def __init__(self, var_type, var_name, initializer):
        self.var_type = var_type
        self.var_name = var_name
        self.initializer = initializer

class IfStatement(Statement):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForStatement(Statement):
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body

class FunctionCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class BinaryOperation(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Variable(Expression):
    def __init__(self, name):
        self.name = name

class Number(Expression):
    def __init__(self, value):
        self.value = value


# Lexical Analysis
def tokenize(code):
    token_specification = [
        ('KEYWORD',  r'\b(int|return|if|else|while|for)\b'), # Keywords
        ('NUMBER',   r'\d+'),                                # Integer
        ('ID',       r'[A-Za-z_]\w*'),                       # Identifiers
        ('COMP_OP',  r'==|!=|<=|>=|<|>'),                    # Comparison operators
        ('ASSIGN',   r'='),                                  # Assignment operator
        ('OP',       r'[+\-*/]'),                            # Arithmetic operators
        ('SEMI',     r';'),                                  # Semicolon
        ('LPAREN',   r'\('),                                 # Left parenthesis
        ('RPAREN',   r'\)'),                                 # Right parenthesis
        ('LBRACE',   r'\{'),                                 # Left brace
        ('RBRACE',   r'\}'),                                 # Right brace
        ('COMMA',    r','),                                  # Comma
        ('SKIP',     r'[ \t\n]+'),                           # Skip over spaces, tabs, and newlines
        ('MISMATCH', r'.'),                                  # Any other character
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    line_num = 1
    line_start = 0
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            tokens.append((kind, value, line_num, column))
    
    return tokens

# Syntax Analysis
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        functions = []
        while self.pos < len(self.tokens):
            functions.append(self.parse_function())
        return Program(functions)
    
    def parse_function(self):
        print(f"Parsing function at position {self.pos}")
        return_type = self.consume('KEYWORD')
        name = self.consume('ID')
        self.consume('LPAREN')
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return Function(return_type, name, body)
    
    def parse_statements(self):
        statements = []
        while not self.check('RBRACE'):
            statements.append(self.parse_statement())
        return statements
    
    def parse_statement(self):
        print(f"Parsing statement at position {self.pos}")
        if self.check('KEYWORD', 'return'):
            self.consume('KEYWORD', 'return')
            expression = self.parse_expression()
            self.consume('SEMI')
            return ReturnStatement(expression)
        elif self.check('KEYWORD', 'int'):
            var_type = self.consume('KEYWORD', 'int')
            var_name = self.consume('ID')
            self.consume('ASSIGN')
            initializer = self.parse_expression()
            self.consume('SEMI')
            return VariableDeclaration(var_type, var_name, initializer)
        elif self.check('KEYWORD', 'if'):
            return self.parse_if_statement()
        elif self.check('KEYWORD', 'while'):
            return self.parse_while_statement()
        elif self.check('KEYWORD', 'for'):
            return self.parse_for_statement()
        elif self.check('ID') and self.check('LPAREN', 1):
            return self.parse_function_call()
        else:
            raise SyntaxError(f'Unknown statement at position {self.pos}')
    
    def parse_if_statement(self):
        self.consume('KEYWORD', 'if')
        self.consume('LPAREN')
        condition = self.parse_expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        then_branch = self.parse_statements()
        self.consume('RBRACE')
        else_branch = None
        if self.check('KEYWORD', 'else'):
            self.consume('KEYWORD', 'else')
            self.consume('LBRACE')
            else_branch = self.parse_statements()
            self.consume('RBRACE')
        return IfStatement(condition, then_branch, else_branch)
    
    def parse_while_statement(self):
        self.consume('KEYWORD', 'while')
        self.consume('LPAREN')
        condition = self.parse_expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return WhileStatement(condition, body)
    
    def parse_for_statement(self):
        self.consume('KEYWORD', 'for')
        self.consume('LPAREN')
        init = self.parse_statement()
        condition = self.parse_expression()
        self.consume('SEMI')
        increment = self.parse_expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return ForStatement(init, condition, increment, body)

    def parse_function_call(self):
        name = self.consume('ID')
        self.consume('LPAREN')
        args = []
        if not self.check('RPAREN'):
            args.append(self.parse_expression())
            while self.check('COMMA'):
                self.consume('COMMA')
                args.append(self.parse_expression())
        self.consume('RPAREN')
        self.consume('SEMI')
        return FunctionCall(name, args)

    def parse_expression(self):
        left = self.parse_term()
        while self.check('OP') or self.check('COMP_OP'):
            operator = self.consume('OP') if self.check('OP') else self.consume('COMP_OP')
            right = self.parse_term()
            left = BinaryOperation(left, operator, right)
        return left
    
    def parse_term(self):
        if self.check('NUMBER'):
            return Number(self.consume('NUMBER'))
        elif self.check('ID'):
            return Variable(self.consume('ID'))
        else:
            raise SyntaxError('Expected number or identifier')
    
    def consume(self, expected_type, expected_value=None):
        token = self.tokens[self.pos]
        if token[0] != expected_type or (expected_value and token[1] != expected_value):
            raise SyntaxError(f'Expected {expected_type} {expected_value} but got {token}')
        self.pos += 1
        return token[1]
    
    def check(self, expected_type, expected_value=None):
        if self.pos >= len(self.tokens):
            return False
        token = self.tokens[self.pos]
        if token[0] != expected_type:
            return False
        if expected_value and token[1] != expected_value:
            return False
        return True

# Semantic Analysis
class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}
    
    def analyze(self):
        for function in self.ast.functions:
            self.visit_function(function)
    
    def visit_function(self, function):
        self.symbol_table = {}
        for statement in function.body:
            self.visit_statement(statement)
    
    def visit_statement(self, statement):
        if isinstance(statement, VariableDeclaration):
            self.visit_variable_declaration(statement)
        elif isinstance(statement, ReturnStatement):
            self.visit_return_statement(statement)
        elif isinstance(statement, IfStatement):
            self.visit_if_statement(statement)
        elif isinstance(statement, WhileStatement):
            self.visit_while_statement(statement)
        elif isinstance(statement, ForStatement):
            self.visit_for_statement(statement)
        elif isinstance(statement, FunctionCall):
            self.visit_function_call(statement)
        else:
            raise ValueError(f"Unknown statement type: {type(statement)}")
    
    def visit_variable_declaration(self, declaration):
        if declaration.var_name in self.symbol_table:
            raise RuntimeError(f"Variable '{declaration.var_name}' already declared")
        self.symbol_table[declaration.var_name] = declaration.var_type
        self.visit_expression(declaration.initializer)
    
    def visit_return_statement(self, statement):
        self.visit_expression(statement.expression)
    
    def visit_if_statement(self, statement):
        self.visit_expression(statement.condition)
        for stmt in statement.then_branch:
            self.visit_statement(stmt)
        if statement.else_branch:
            for stmt in statement.else_branch:
                self.visit_statement(stmt)
    
    def visit_while_statement(self, statement):
        self.visit_expression(statement.condition)
        for stmt in statement.body:
            self.visit_statement(stmt)
    
    def visit_for_statement(self, statement):
        self.visit_statement(statement.init)
        self.visit_expression(statement.condition)
        self.visit_expression(statement.increment)
        for stmt in statement.body:
            self.visit_statement(stmt)

    def visit_function_call(self, call):
        for arg in call.args:
            self.visit_expression(arg)
    
    def visit_expression(self, expression):
        if isinstance(expression, BinaryOperation):
            self.visit_expression(expression.left)
            self.visit_expression(expression.right)
        elif isinstance(expression, Variable):
            if expression.name not in self.symbol_table:
                raise RuntimeError(f"Variable '{expression.name}' not declared")
        elif isinstance(expression, Number):
            pass
        else:
            raise ValueError(f"Unknown expression type: {type(expression)}")

# Intermediate Code Generation
class IntermediateCodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []
        self.temp_count = 0
    
    def generate(self):
        for function in self.ast.functions:
            self.visit_function(function)
        return self.code
    
    def visit_function(self, function):
        for statement in function.body:
            self.visit_statement(statement)
    
    def visit_statement(self, statement):
        if isinstance(statement, VariableDeclaration):
            self.visit_variable_declaration(statement)
        elif isinstance(statement, ReturnStatement):
            self.visit_return_statement(statement)
        elif isinstance(statement, IfStatement):
            self.visit_if_statement(statement)
        elif isinstance(statement, WhileStatement):
            self.visit_while_statement(statement)
        elif isinstance(statement, ForStatement):
            self.visit_for_statement(statement)
        elif isinstance(statement, FunctionCall):
            self.visit_function_call(statement)
        else:
            raise ValueError(f"Unknown statement type: {type(statement)}")
    
    def visit_variable_declaration(self, declaration):
        temp_var = self.new_temp()
        self.visit_expression(declaration.initializer, temp_var)
        self.code.append(f"{declaration.var_name} = {temp_var}")
    
    def visit_return_statement(self, statement):
        temp_var = self.new_temp()
        self.visit_expression(statement.expression, temp_var)
        self.code.append(f"return {temp_var}")
    
    def visit_if_statement(self, statement):
        condition_var = self.new_temp()
        self.visit_expression(statement.condition, condition_var)
        self.code.append(f"if {condition_var} goto L1")
        else_label = f"L{self.new_temp()}"
        self.code.append(f"goto {else_label}")
        self.code.append(f"L1:")
        for stmt in statement.then_branch:
            self.visit_statement(stmt)
        if statement.else_branch:
            end_label = f"L{self.new_temp()}"
            self.code.append(f"goto {end_label}")
            self.code.append(f"{else_label}:")
            for stmt in statement.else_branch:
                self.visit_statement(stmt)
            self.code.append(f"{end_label}:")
        else:
            self.code.append(f"{else_label}:")
    
    def visit_while_statement(self, statement):
        start_label = f"L{self.new_temp()}"
        self.code.append(f"{start_label}:")
        condition_var = self.new_temp()
        self.visit_expression(statement.condition, condition_var)
        end_label = f"L{self.new_temp()}"
        self.code.append(f"if not {condition_var} goto {end_label}")
        for stmt in statement.body:
            self.visit_statement(stmt)
        self.code.append(f"goto {start_label}")
        self.code.append(f"{end_label}:")
    
    def visit_for_statement(self, statement):
        self.visit_statement(statement.init)
        start_label = f"L{self.new_temp()}"
        self.code.append(f"{start_label}:")
        condition_var = self.new_temp()
        self.visit_expression(statement.condition, condition_var)
        end_label = f"L{self.new_temp()}"
        self.code.append(f"if not {condition_var} goto {end_label}")
        for stmt in statement.body:
            self.visit_statement(stmt)
        self.visit_expression(statement.increment, None)
        self.code.append(f"goto {start_label}")
        self.code.append(f"{end_label}:")
    
    def visit_function_call(self, call):
        temp_vars = []
        for arg in call.args:
            temp_var = self.new_temp()
            self.visit_expression(arg, temp_var)
            temp_vars.append(temp_var)
        self.code.append(f"call {call.name}({', '.join(temp_vars)})")
    
    def visit_expression(self, expression, target):
        if isinstance(expression, BinaryOperation):
            left_temp = self.new_temp()
            right_temp = self.new_temp()
            self.visit_expression(expression.left, left_temp)
            self.visit_expression(expression.right, right_temp)
            self.code.append(f"{target} = {left_temp} {expression.operator} {right_temp}")
        elif isinstance(expression, Variable):
            self.code.append(f"{target} = {expression.name}")
        elif isinstance(expression, Number):
            self.code.append(f"{target} = {expression.value}")
        else:
            raise ValueError(f"Unknown expression type: {type(expression)}")
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

# Assembly Code Generation
class AssemblyCodeGenerator:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.assembly_code = []
    
    def generate(self):
        for line in self.intermediate_code:
            self.generate_line(line)
        return self.assembly_code
    
    def generate_line(self, line):
        parts = line.split()
        if parts[0] == 'return':
            self.assembly_code.append(f"MOV R0, {parts[1]}")
            self.assembly_code.append("RET")
        elif parts[0] == 'if':
            self.assembly_code.append(f"CMP {parts[1]}, 0")
            self.assembly_code.append(f"JNE {parts[3]}")
        elif parts[0] == 'goto':
            self.assembly_code.append(f"JMP {parts[1]}")
        elif parts[0].startswith('L'):
            self.assembly_code.append(f"{parts[0]}:")
        elif parts[0] == 'call':
            args = parts[1][parts[1].index('(')+1:parts[1].index(')')].split(', ')
            for i, arg in enumerate(args):
                self.assembly_code.append(f"MOV R{i+1}, {arg}")
            self.assembly_code.append(f"CALL {parts[1][:parts[1].index('(')]}")
        else:
            if '=' in parts:
                target, expression = parts[0], parts[2:]
                if len(expression) == 1:
                    self.assembly_code.append(f"MOV {target}, {expression[0]}")
                else:
                    left, operator, right = expression
                    self.assembly_code.append(f"MOV R1, {left}")
                    self.assembly_code.append(f"{self.translate_operator(operator)} R1, {right}")
                    self.assembly_code.append(f"MOV {target}, R1")
    
    def translate_operator(self, operator):
        return {
            '+': 'ADD',
            '-': 'SUB',
            '*': 'MUL',
            '/': 'DIV',
            '>': 'JG',
            '<': 'JL',
            '>=': 'JGE',
            '<=': 'JLE',
            '==': 'JE',
            '!=': 'JNE'
        }[operator]

# Example usage
code = """
#define VAL 5

int main() {
    int a = VAL + 3;
    if (a > 5) {
        return a;
    } else {
        return 0;
    }
}
"""

preprocessor = Preprocessor(code)
preprocessed_code = preprocessor.preprocess()

tokens = tokenize(preprocessed_code)
parser = Parser(tokens)
ast = parser.parse()
semantic_analyzer = SemanticAnalyzer(ast)
semantic_analyzer.analyze()
intermediate_code_generator = IntermediateCodeGenerator(ast)
intermediate_code = intermediate_code_generator.generate()
assembly_code_generator = AssemblyCodeGenerator(intermediate_code)
assembly_code = assembly_code_generator.generate()

def print_ast(node, indent=0):
    print('  ' * indent + str(node))
    if isinstance(node, Program):
        for func in node.functions:
            print_ast(func, indent + 1)
    elif isinstance(node, Function):
        print_ast(node.body, indent + 1)
    elif isinstance(node, list):
        for stmt in node:
            print_ast(stmt, indent + 1)
    elif isinstance(node, ReturnStatement):
        print_ast(node.expression, indent + 1)
    elif isinstance(node, VariableDeclaration):
        print('  ' * (indent + 1) + f'{node.var_type} {node.var_name}')
        print_ast(node.initializer, indent + 2)
    elif isinstance(node, IfStatement):
        print('  ' * (indent + 1) + 'if')
        print_ast(node.condition, indent + 2)
        print('  ' * (indent + 1) + 'then')
        print_ast(node.then_branch, indent + 2)
        if node.else_branch:
            print('  ' * (indent + 1) + 'else')
            print_ast(node.else_branch, indent + 2)
    elif isinstance(node, WhileStatement):
        print('  ' * (indent + 1) + 'while')
        print_ast(node.condition, indent + 2)
        print('  ' * (indent + 1) + 'do')
        print_ast(node.body, indent + 2)
    elif isinstance(node, ForStatement):
        print('  ' * (indent + 1) + 'for')
        print_ast(node.init, indent + 2)
        print_ast(node.condition, indent + 2)
        print_ast(node.increment, indent + 2)
        print('  ' * (indent + 1) + 'do')
        print_ast(node.body, indent + 2)
    elif isinstance(node, FunctionCall):
        print('  ' * (indent + 1) + f'call {node.name}')
        for arg in node.args:
            print_ast(arg, indent + 2)
    elif isinstance(node, BinaryOperation):
        print_ast(node.left, indent + 1)
        print('  ' * (indent + 1) + node.operator)
        print_ast(node.right, indent + 1)
    elif isinstance(node, Variable):
        print('  ' * (indent + 1) + node.name)
    elif isinstance(node, Number):
        print('  ' * (indent + 1) + str(node.value))

print_ast(ast)

# Print the intermediate code
print("\nIntermediate Code:")
for line in intermediate_code:
    print(line)

# Print the assembly code
print("\nAssembly Code:")
for line in assembly_code:
    print(line)
