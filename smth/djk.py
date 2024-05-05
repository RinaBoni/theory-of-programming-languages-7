import ply.lex as lex

# Определение токенов
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE']

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Игнорируем пробелы и табуляцию
t_ignore = ' \t'

# Обработка ошибок
def t_error(t):
    print(f"Некорректный символ: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Тестируем лексер на строке
data = '3 + 4 * 10 - 6 / 2'

# Подача данных на вход лексеру
lexer.input(data)

# Печать токенов
while True:
    tok = lexer.token()
    if not tok:
        break  # Конец токенизации
    print(tok)