import re

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0
        self.keywords = ['if', 'else', 'while', 'for', 'def']  # Пример ключевых слов

    def tokenize(self):
        tokens = []

        while self.current_position < len(self.input_string):
            char = self.input_string[self.current_position]

            # Пропускаем пробелы и символы новой строки
            if char.isspace():
                self.current_position += 1
                continue

            # Распознаем числа
            if char.isdigit():
                number = ''
                while self.current_position < len(self.input_string) and self.input_string[self.current_position].isdigit():
                    number += self.input_string[self.current_position]
                    self.current_position += 1
                tokens.append(('NUMBER', int(number)))
                continue

            # Распознаем идентификаторы и ключевые слова
            if char.isalpha():
                identifier = ''
                while self.current_position < len(self.input_string) and (self.input_string[self.current_position].isalnum() or self.input_string[self.current_position] == '_'):
                    identifier += self.input_string[self.current_position]
                    self.current_position += 1

                if identifier in self.keywords:
                    tokens.append(('KEYWORD', identifier))
                else:
                    tokens.append(('IDENTIFIER', identifier))
                continue

            # Распознаем символы операций
            if char in ['+', '-', '*', '/']:
                tokens.append(('OPERATOR', char))
                self.current_position += 1
                continue

            # Обработка других символов
            tokens.append(('UNKNOWN', char))
            self.current_position += 1

        return tokens

# Пример использования
input_code = "if x > 0:\n    print('Positive')"
lexer = Lexer(input_code)
tokens = lexer.tokenize()
print(tokens)