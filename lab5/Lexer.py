class Lexer:
    def __init__(self):
        self.keywords = ["do", "for"]
        self.states = {
            "H": 0, 
            "ID": 1, 
            "NM": 2, 
            "ASGN": 3, 
            "DLM": 4, 
            "ERR": 5}
        self.tok_names = {
            "KWORD_DO": 'KWORD_DO', 
            "KWORD_FOR": 'KWORD_FOR', 
            "IDENT": 'IDENT', 
            "NUM": 'NUM', 
            "OPER": 'OPER', 
            "ASIGN": 'ASIGN', 
            "DELIM": 'DELIM', 
            "LBRACE": 'LBRACE', 
            "RBRACE": 'RBRACE', 
            "EXPRESSION": 'EXPRESSION', 
            "ERROR": 'ERROR'}

        self.tokens = []
        self.curr = None

    def getNext(self):
        self.curr = self.curr.next
        return self.curr

    def getTokens(self):
        return self.tokens

    def is_keyword(self, string):
        for keyword in self.keywords:
            if keyword == string:
                return True
        return False

    def fillTable(self, string):
        self.tokens = []
        CS = self.states["H"]
        i = 0
        while i < len(string):
            if CS == self.states["H"]:
                while i < len(string) - 1 and (string[i] == ' ' or string[i] == '\t' or string[i] == '\n'):
                    i += 1
                if ('0' <= string[i] <= '9'):
                    CS = self.states["NM"]
                elif (string[i] >= 'A' and string[i] <= 'Z') or (string[i] >= 'a' and string[i] <= 'z') or string[i] == '_':
                    CS = self.states["ID"]
                elif string[i] == ':':
                    CS = self.states["ASGN"]
                    i += 1
                elif string[i] == '>' or string[i] == '<' or string[i] == '=' or string[i] == '+' or string[i] == '-':
                    token = {"token_name": self.tok_names["OPER"], "token_value": string[i], "index": i}
                    self.tokens.append(token)
                    CS = self.states["H"]
                    i += 1
                else:
                    CS = self.states["DLM"]
            elif CS == self.states["ASGN"]:
                if string[i] == '=':
                    tok = {"token_name": self.tok_names["ASIGN"], "token_value": ":=", "index": i}
                    self.tokens.append(tok)
                    CS = self.states["H"]
                    i += 1
                else:
                    CS = self.states["ERR"]
            elif CS == self.states["DLM"]:
                if string[i] == '(' or string[i] == ')' or string[i] == ';':
                    tok = {"token_name": self.tok_names["DELIM"], "token_value": string[i], "index": i}
                    if string[i] == '(':
                        tok["token_name"] = self.tok_names["LBRACE"]
                    if string[i] == ')':
                        tok["token_name"] = self.tok_names["RBRACE"]
                    self.tokens.append(tok)
                    CS = self.states["H"]
                    i += 1
                else:
                    if string[i] != ' ' and string[i] != '\n' and string[i] != '\t':
                        CS = self.states["ERR"]
                    else:
                        CS = self.states["H"]
                        i += 1
            elif CS == self.states["ERR"]:
                token = {"token_name": self.tok_names["ERROR"], "token_value": "at " + str(i) + " " + string[i], "index": i}
                self.tokens.append(token)
                CS = self.states["H"]
                i += 1
            elif CS == self.states["ID"]:
                token = {"token_name": "", "token_value": "", "index": i}
                id = ""
                while i < len(string) and (string[i] != ' ' or string[i] != '\n' or string[i] != '\t') and (((string[i] >= 'A') and (string[i] <= 'Z')) or ((string[i] >= 'a') and (string[i] <= 'z')) or ((string[i] >= '0') and (string[i] <= '9')) or (string[i] == '_')):
                    id += string[i]
                    i += 1
                if self.is_keyword(id):
                    if id == "do":
                        token["token_name"] = self.tok_names["KWORD_DO"]
                    if id == "for":
                        token["token_name"] = self.tok_names["KWORD_FOR"]
                else:
                    token["token_name"] = self.tok_names["IDENT"]
                token["token_value"] = id
                token["index"] = i
                self.tokens.append(token)
                CS = self.states["H"]
            elif CS == self.states["NM"]:
                token = {"token_name": self.tok_names["NUM"], "token_value": "", "index": i}
                num = ""
                while i < len(string) and ('0' <= string[i] <= '9'):
                    num += string[i]
                    i += 1
                token["token_value"] = num
                token["index"] = i
                self.tokens.append(token)
                CS = self.states["H"]
        self.curr = self.tokens[0]
        print(self.tokens)
        return self.tokens
        
        
def output(input_string):
    lexer = Lexer()
    lexer.fillTable(input_string)
    tokens = lexer.getTokens()
    return tokens