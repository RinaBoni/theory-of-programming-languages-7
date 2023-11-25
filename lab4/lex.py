class Lexer:
    def __init__(self):
        self.keywords = ["do", "while"]
        self.states = {"H": 0, "ID": 1, "NM": 2, "ASGN": 3, "DLM": 4, "ERR": 5}
        self.tok_names = {"KWORD": 0, "IDENT": 1, "NUM": 2, "OPER": 3, "DELIM": 4, "ERROR": 5}
        self.key_value_pairs = {
            "KWORD": "KWORD",
            "IDENT": "IDENT",
            "NUM": "NUM",
            "OPER": "OPER",
            "DELIM": "DELIM",
            "ERROR": "ERROR",
        }

        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def is_keyword(self, string):
        return string in self.keywords

    def fill_table(self, string):
        self.tokens = []
        CS = self.states["H"]
        i = 0

        while i < len(string):
            if CS == self.states["H"]:
                while i < len(string) - 1 and (string[i] == " " or string[i] == "\t" or string[i] == "\n"):
                    i += 1

                if string[i] == "X" or string[i] == "V" or string[i] == "I":
                    CS = self.states["NM"]
                elif (
                    (string[i] >= "A" and string[i] <= "Z")
                    or (string[i] >= "a" and string[i] <= "z")
                    or string[i] == "_"
                ):
                    CS = self.states["ID"]
                elif string[i] == ":":
                    CS = self.states["ASGN"]
                    i += 1
                elif string[i] in [">", "<", "=", "+", "-"]:
                    token = {"token_name": self.tok_names["OPER"], "token_value": string[i]}
                    self.tokens.append(token)
                    CS = self.states["H"]
                    i += 1
                else:
                    CS = self.states["DLM"]

            elif CS == self.states["ASGN"]:
                if string[i] == "=":
                    token = {"token_name": self.tok_names["OPER"], "token_value": ":="}
                    self.tokens.append(token)
                    CS = self.states["H"]
                    i += 1
                else:
                    CS = self.states["ERR"]

            elif CS == self.states["DLM"]:
                if string[i] in ["(", ")", ";"]:
                    token = {"token_name": self.tok_names["DELIM"], "token_value": string[i]}
                    self.tokens.append(token)
                    CS = self.states["H"]
                    i += 1
                else:
                    if string[i] not in [" ", "\n", "\t"]:
                        CS = self.states["ERR"]
                    else:
                        CS = self.states["H"]
                        i += 1

            elif CS == self.states["ERR"]:
                token = {"token_name": self.tok_names["ERROR"], "token_value": f"at {i} {string[i]}"}
                self.tokens.append(token)
                CS = self.states["H"]
                i += 1

            elif CS == self.states["ID"]:
                token = {"token_name": 0, "token_value": ""}
                identifier = ""
                while (
                    i < len(string)
                    and (string[i] not in [" ", "\n", "\t"])
                    and (
                        (string[i] >= "A" and string[i] <= "Z")
                        or (string[i] >= "a" and string[i] <= "z")
                        or (string[i] >= "0" and string[i] <= "9")
                        or (string[i] == "_")
                    )
                ):
                    identifier += string[i]
                    i += 1

                if self.is_keyword(identifier):
                    token["token_name"] = self.tok_names["KWORD"]
                else:
                    token["token_name"] = self.tok_names["IDENT"]
                token["token_value"] = identifier
                self.tokens.append(token)
                CS = self.states["H"]

            elif CS == self.states["NM"]:
                token = {"token_name": self.tok_names["NUM"], "token_value": ""}
                number = ""
                while i < len(string) and (string[i] == "X" or string[i] == "V" or string[i] == "I"):
                    number += string[i]
                    i += 1

                token["token_value"] = number
                self.tokens.append(token)
                CS = self.states["H"]

lex = Lexer()

lex.fill_table(input())

result_str = ""
for token in lex.get_tokens():
    token_type = next(value for key, value in lex.key_value_pairs.items() if key == token.token_name)
    result_str += f"<{token_type}> : {token.token_value}\n"
print(result_str)
