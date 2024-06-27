import re

# AST Node Classes
class ASTNode:
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

class Expression(ASTNode):
    pass

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
        ('KEYWORD',  r'\b(int|return)\b'), # Keywords
        ('NUMBER',   r'\d+'),              # Integer
        ('ID',       r'[A-Za-z_]\w*'),     # Identifiers
        ('OP',       r'[+\-*/]'),          # Arithmetic operators
        ('ASSIGN',   r'='),                # Assignment operator
        ('SEMI',     r';'),                # Semicolon
        ('LPAREN',   r'\('),               # Left parenthesis
        ('RPAREN',   r'\)'),               # Right parenthesis
        ('LBRACE',   r'\{'),               # Left brace
        ('RBRACE',   r'\}'),               # Right brace
        ('SKIP',     r'[ \t\n]+'),         # Skip over spaces, tabs, and newlines
        ('MISMATCH', r'.'),                # Any other character
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
        else:
            raise SyntaxError(f'Unknown statement at position {self.pos}')
    
    def parse_expression(self):
        left = self.parse_term()
        while self.check('OP'):
            operator = self.consume('OP')
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

# Example usage
code = """
int main() {
    int a = 5 + 3;
    return a;
}
"""

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.parse()

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
    elif isinstance(node, BinaryOperation):
        print_ast(node.left, indent + 1)
        print('  ' * (indent + 1) + node.operator)
        print_ast(node.right, indent + 1)
    elif isinstance(node, Variable):
        print('  ' * (indent + 1) + node.name)
    elif isinstance(node, Number):
        print('  ' * (indent + 1) + str(node.value))

print_ast(ast)
