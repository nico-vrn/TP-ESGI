import re

def tokenize(code):
    token_specification = [
        ('NUMBER',   r'\d+'),           # Integer
        ('ID',       r'[A-Za-z_]\w*'),  # Identifiers
        ('OP',       r'[+\-*/]'),       # Arithmetic operators
        ('ASSIGN',   r'='),             # Assignment operator
        ('SEMI',     r';'),             # Semicolon
        ('LPAREN',   r'\('),            # Left parenthesis
        ('RPAREN',   r'\)'),            # Right parenthesis
        ('LBRACE',   r'\{'),            # Left brace
        ('RBRACE',   r'\}'),            # Right brace
        ('KEYWORD',  r'\b(int|return)\b'), # Keywords
        ('SKIP',     r'[ \t\n]+'),      # Skip over spaces, tabs, and newlines
        ('MISMATCH', r'.'),             # Any other character
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

# Example usage
code = """
int main() {
    int a = 5 + 3;
    return a;
}
"""

tokens = tokenize(code)
for token in tokens:
    print(token)
