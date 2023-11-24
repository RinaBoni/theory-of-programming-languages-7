import re


def lexical_analysis(input_text):
    # лексемы
    patterns = [
        (r'\s+', 'WHITESPACE'),
        (r'for|do', 'KEYWORD'),
        (r'\(', 'LPAREN'),
        (r'\)', 'RPAREN'),
        (r';', 'SEMICOLON'),
        (r'<|>|=', 'COMPARISON'),
        (r':=', 'ASSIGNMENT'),
        (r'[a-zA-Z_]\w*', 'IDENTIFIER'),
        (r'\d+(\.\d+)?(e[+-]?\d+)?', 'NUMBER')
    ]

    lexeme_table = []

    # Проход по тексту и поиск лексем
    position = 0
    while position < len(input_text):
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(input_text, position)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    lexeme_table.append((value, token_type))
                position = match.end()
                break

        if not match:
            print(f"Ошибка: Неизвестный символ в позиции {position}: {input_text[position]}")
            position += 1

    return lexeme_table


if __name__ == "__main__":
    input_text = input("Введите текст: ")
    result = lexical_analysis(input_text)

    # Вывод таблицы лексем
    print("\nТаблица лексем:")
    print("{:<15} {:<15}".format("Лексема", "Тип"))
    print("-" * 30)
    for lexeme, token_type in result:
        print("{:<15} {:<15}".format(lexeme, token_type))
