class Lexer:
    keywords = ["for", "do"]

    class States:
        H, ID, NM, ASGN, DLM, ERR = range(6)

    class TokenNames:
        KEYWORD, IDENTIFIER, NUMBER, OPERATION, DELIMITER, ERROR = range(6)

    key_value_pairs = {
        TokenNames.KEYWORD: "KEYWORD",
        TokenNames.IDENTIFIER: "IDENTIFIER",
        TokenNames.NUMBER: "NUMBER",
        TokenNames.OPERATION: "OPERATION",
        TokenNames.DELIMITER: "DELIMITER",
        TokenNames.ERROR: "ERROR"
    }

    def __init__(self):
        self.tokens = ()

    def get_tokens(self):
        return self.tokens

    def is_keyword(self, string):
        return string in self.keywords

    def fill_table(self, string):
        self.tokens = []
        CS = self.States.H
        i = 0

        while i < len(string):
            if CS == self.States.H:
                while i < len(string) - 1 and (string[i] == ' ' or string[i] == '\t' or string[i] == '\n'):
                    i += 1
                if ('0' <= string[i] <= '9'):
                    CS = self.States.NM
                elif ('A' <= string[i] <= 'Z' or 'a' <= string[i] <= 'z' or string[i] == '_'):
                    CS = self.States.ID
                elif string[i] == ':':
                    CS = self.States.ASGN
                    i += 1
                elif string[i] in ['>', '<', '=', '+', '-']:
                    token = {'token_name': 'OPERATION', 'token_value': string[i]}
                    self.tokens.append(token)
                    CS = self.States.H
                    i += 1
                else:
                    CS = self.States.DLM
            elif CS == self.States.ASGN:
                if string[i] == '=':
                    token = {'token_name': 'OPERATION', 'token_value': ':='}
                    self.tokens.append(token)
                    CS = self.States.H
                    i += 1
                else:
                    CS = self.States.ERR
            elif CS == self.States.DLM:
                if string[i] in ['(', ')', ';']:
                    token = {'token_name': 'DELIMITER', 'token_value': string[i]}
                    self.tokens.append(token)
                    CS = self.States.H
                    i += 1
                else:
                    if string[i] not in [' ', '\n', '\t']:
                        CS = self.States.ERR
                    else:
                        CS = self.States.H
                        i += 1
            elif CS == self.States.ERR:
                token = {'token_name': 'ERROR', 'token_value': f"at {i} {string[i]}"}
                self.tokens.append(token)
                CS = self.States.H
                i += 1
            elif CS == self.States.ID:
                token = {'token_name': 'IDENTIFIER', 'token_value': ''}
                identifier = ""
                while i < len(string) and (
                        string[i] != ' ' or string[i] != '\n' or string[i] != '\t') and (
                        ('A' <= string[i] <= 'Z') or ('a' <= string[i] <= 'z') or (
                        '0' <= string[i] <= '9') or string[i] == '_'):
                    identifier += string[i]
                    i += 1
                if self.is_keyword(identifier):
                    token['token_name'] = 'KEYWORD'
                else:
                    token['token_name'] = 'IDENTIFIER'
                token['token_value'] = identifier
                self.tokens.append(token)
                CS = self.States.H
            elif CS == self.States.NM:
                token = {'token_name': 'NUMBER', 'token_value': ''}
                number = ""
                # while i < len(string) and (string[i] == 'X' or string[i] == 'V' or string[i] == 'I'):
                while i < len(string) and ('0' <= string[i] <= '9'):
                    number += string[i]
                    i += 1
                token['token_value'] = number
                self.tokens.append(token)
                CS = self.States.H
        return self.tokens



def sh():
    print('halo')

def output(input_string):
    lexer = Lexer()
    lexer.fill_table(input_string)
    tokens = lexer.get_tokens()
    return tokens

    # for tok in tokens:
    #     print('\n', tok)