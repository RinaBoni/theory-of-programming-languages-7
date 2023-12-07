from Lexer import Lexer
class SyntaxAnalyzer:
    def __init__(self):
        self.keywords = ["do", "for"]
        self.errors = {
            "OK": 'OK',
            "EXECPTED_ID": 'EXECPTED_ID',
            "EXECPTED_ID_OR_NUM": 'EXECPTED_ID_OR_NUM',
            "UNEXEPTED_ID": 'UNEXEPTED_ID',
            "EXEPTED_LBRACE": 'EXEPTED_LBRACE',
            "EXEPTED_RBRACE": 'EXEPTED_RBRACE',
            "EXEPTED_EXPRESION": 'EXEPTED_EXPRESION',
            "EXEPTED_DELIMITOR": 'EXEPTED_DELIMITOR',
            "EXEPTED_OPERAND": 'EXEPTED_OPERAND',
            "EXEPTED_KWORD": 'EXEPTED_KWORD',
            "EXEPTED_ASSIGN": 'EXEPTED_ASSIGN',
            "UNRECOGNIZED_STATEMENT": 'UNRECOGNIZED_STATEMENT',
        }
        
        
        
    def require_lexem(self, lexer, exepted):
        '''проверяет, совпадает ли текущая лексема с одним из ожидаемых типов'''
        if lexer:
            value = [item['token_name'] for item in lexer]
            for i in range(len(exepted)):
                if value == exepted[i]:
                    return True
        return False



    def kword(self, lexer):
        '''проверяет структуру кода, ожидая определенной последовательности лексем и возвращая ошибки, если эта последовательность нарушена'''
        if not self.require_lexem(lexer, ['IDENT', 'NUM']):
            return self.errors['EXECPTED_ID_OR_NUM']
        
        result = self.expression(lexer)
        if result != self.errors['OK']:
            return result
        
        if not self.require_lexem(lexer, ['KWORD_FOR', 'KWORD_DO']):
            return self.errors['EXEPTED_KWORD']
        
        if not self.require_lexem(lexer, ['LBRACE']):
            return self.errors['EXEPTED_LBRACE']
        
        if not self.require_lexem(lexer, ['IDENT', 'NUM']):
            return self.errors['EXECPTED_ID_OR_NUM']
        
        result = self.expression(lexer)
        if result != self.errors['OK']:
            return result
        
        if not self.require_lexem(lexer, ['RBRACE']):
            return self.errors['EXEPTED_RBRACE']
        
        if not self.require_lexem(lexer, ['DELIM']):
            return self.errors['EXEPTED_DELIMITOR']
        
        return self.errors['OK']
    
    
    
    def expression(self, lexer):
        '''анализа выражений, содержащих операторы, возвращает ошибку, если структура выражения не соответствует ожидаемой'''
        if lexer:
            value = [item['token_name'] for item in lexer]
            if value == 'OPER':
                if not self.require_lexem(lexer, ['OPER']):
                    return self.errors['EXEPTED_OPERAND']
                
                if not self.require_lexem(lexer, ['IDENT', 'NUM']):
                    return self.errors['EXECPTED_ID']
                
                result = self.expression(lexer)
                if result != self.errors['OK']:
                    return result
                
        return self.errors['OK']
    
    
    
    def declaration(self, lexer):
        ''' сканирует и проверяет последовательность лексем, ожидаемых в объявлении, и возвращает ошибку, если какая-либо из них отсутствует или не соответствует ожидаемой структуре.'''
        if not self.require_lexem(lexer, ['IDENT']):
            return self.errors['EXECPTED_ID']
        
        if not self.require_lexem(lexer, ['ASIGN']):
            return self.errors['EXEPTED_ASSIGN']
        
        if not self.require_lexem(lexer, ['IDENT', 'NUM']):
            return self.errors['EXECPTED_ID_OR_NUM']
        
        if not self.require_lexem(lexer, ['DELIM']):
            return self.errors['EXEPTED_DELIMITOR']
        
        return self.errors['OK']
    
    
    
    def statement(self, lexer):
        '''определяет тип текущей лексемы и выполняет соответствующие операции в зависимости от этого типа, возвращая ошибку, если структура оператора не соответствует ожидаемой'''
        value = [item['token_name'] for item in lexer]
        if value == 'IDENT':
            return self.declaration(lexer)
        
        if value == 'LBRACE':
            if not self.require_lexem(lexer, ['IDENT', 'NUM']):
                return self.errors['EXECPTED_ID']
            
            result = self.expression(lexer)
            if result != self.errors['OK']:
                    return result
                
            if not self.require_lexem(lexer, ['RBRACE']):
                return self.errors['EXEPTED_RBRACE']
            return self.errors['OK']
        
        if value == 'KWORD_DO':
            return self.kword(lexer)
        
        if value == 'KWORD_FOR':
            return self.errors['EXEPTED_KWORD']
        
        return self.errors['UNRECOGNIZED_STATEMENT']
    
