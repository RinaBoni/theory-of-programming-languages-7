from rply import LexerGenerator
# LexerGenerator используется для добавления токенов и создания лексера


class Lexer():
    def __init__(self, lexemes):
        self.lexer = LexerGenerator()   # создание объекта LexerGenerator
        self.lexemes = lexemes          # список лексем (шаблонов токенов), каждый элемент является кортежем (ID, regex), 
                                        # ID: идентификатор токена ('INTEGER'), regex: регулярное выражение, как распозать токен
    
        self.__add_tokens()             # добавление всех лексем в LexerGenerator
        self.lexer = self.lexer.build() # построение лексера 

    def __add_tokens(self):
        for ID, regex in self.lexemes:
            self.lexer.add(ID, regex)   # добавление кортежа (ID, regex) в LexerGenerator
            

    def __call__(self, text):           # позволяет объектам класса вести себя как функции
        return self.lexer.lex(text)     # преобразование текста в поток лексем (токенов), используя построенный ранее лексер