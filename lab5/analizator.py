import re
from ply import lex, yacc

# Определение токенов
tokens = [
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'MULTIPLY',
    'DIVIDE',
    'PLUS',
    'MINUS',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'CHAR_CONSTANT',
    'SEMICOLON',
    'COMPARISON',
    'KWORD'
    # 'FOR',
    # 'DO'
]

# Регулярные выражения для токенов
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'
t_MINUS = r'-'
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CHAR_CONSTANT = r"'.'"
t_SEMICOLON = r';'
t_COMPARISON = r'==|<=|>=|>|<'
# t_DO = r'do'
# t_FOR = r'for'

def t_KWORD(t):
    r'for|do'
    return t

# Функция для идентификации идентификаторов
def t_IDENTIFIER(t):
    r'\b(?:[a-zA-Z]\w*)\b'
    return t
# Функция для идентификации дробных чисел
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Функция для идентификации целых чисел
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Функция для обработки пробелов и табуляции (игнорируем их)
t_ignore = ' \t'

# Функция для обработки новых строк (подсчет строк)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Обработка ошибок
def t_error(t):
    print(f"Недопустимый символ '{t.value[0]}'")
    t.lexer.skip(1)

# Создание лексического анализатора
lexer = lex.lex()

# Грамматика для синтаксического анализатора

def p_expression_kword(p):
    'expression : KWORD expression KWORD expression'
    p[0] = ('KWORD', p[1], p[2], 'KWORD', p[3]), p[4]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('IDENTIFIER', p[1])

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = ('FLOAT', p[1])

def p_expression_integer(p):
    'expression : INTEGER'
    p[0] = ('INTEGER', p[1])
    
# def p_expression_for(p):
#     'expression : KWORD'


def p_expression_binary_operation(p):
    '''expression : expression MULTIPLY expression
                  | expression DIVIDE  expression
                  | expression PLUS expression
                  | expression PLUS PLUS
                  | expression MINUS expression'''

    # '''expression : expression PLUS expression
    #               | expression MINUS expression
    #               | expression MULTIPLY expression
    #               | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_comparison(p):
    'expression  : expression COMPARISON  expression'
    p[0] = ('COMPARISON', p[1], p[3])

def p_assignment(p):
    'expression : IDENTIFIER ASSIGN expression'
    p[0] = ('ASSIGN', p[1], p[3])

def p_expression_parentheses(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_char_constant(p):
    'expression : CHAR_CONSTANT'
    p[0] = ('CHAR_CONSTANT', p[1])

# def p_expression_semicolon(p):
#     'expression : expression SEMICOLON'
#     p[0] = ('SEMICOLON', p[1])
def p_expression_semicolon(p):
    'expression : expression SEMICOLON expression'
    p[0] = ('SEMICOLON', p[1], p[3])

# Обработка ошибок в синтаксическом анализе
def p_error(p):
    print("Ошибка в синтаксисе")



def syn_analization(input_text):
    # Создание синтаксического анализатора
    parser = yacc.yacc()
    lexer.input(input_text)
    # Парсинг
    result = parser.parse(lexer=lexer)
    # Вывод дерева синтаксического разбора
    print('\n\nСинтаксический анализатор:\n')
    print(result)
    
    return(result)

def lex_analization(input_text):

    lexer.input(input_text)

    lex_result =[]
    while True:
        tok = lexer.token()
        if not tok:
            break  # Конец токенизации
        lex_result.append(tok)
    print('\n\Лексический анализатор:\n')
    print(lex_result)
    return lex_result


# input_text = input("Введите строку:")
# input_text = input()
# lex_analization(input_text)