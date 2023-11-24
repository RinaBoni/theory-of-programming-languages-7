import re

def lexical_analysis(input_code):
    # Определение шаблонов регулярных выражений для различных лексем
    patterns = [
        ('FOR', r'for\s*\([^;]*;[^;]*;[^)]*\)\s*do\s*'),
        ('SEMICOLON', r';'),
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('COMPARISON_OPERATOR', r'[<>]=?'),
        ('ASSIGNMENT', r':='),
        ('STRING_CONSTANT', r'"[^"]*"')
    ]

    tokens = []

    # Проход по входному коду для поиска лексем
    while input_code:
        match = None
        for token_type, pattern in patterns:
            regex = re.compile(pattern)
            match = regex.match(input_code)
            if match:
                value = match.group(0).strip()
                tokens.append((token_type, value))
                input_code = input_code[len(value):].lstrip()
                break

        if not match:
            # Если не удалось распознать лексему, выводим сообщение об ошибке
            print(f"Ошибка: Не удалось распознать лексему в: {input_code}")
            break

    return tokens

# Пример использования
input_code = "for (i := 0; i < 10; i := i + 1) do print(\"Hello, World!\");"
result_tokens = lexical_analysis(input_code)

# Вывод результата
for token_type, value in result_tokens:
    print(f"Тип: {token_type}, Значение: {value}")