from analyzers.Token import Token

 
def c_tokens_preprocessing(tokens):
    """пропускает токены, представляющие пробелы, двоеточия, точки с запятой, новые строки и табуляции.
    остальные токены добавляются в результирующий список."""
    res = []

    for token in tokens:
        if token.name == 'tkSpace': continue
        if token.name == 'tkColon': continue
        if token.name == 'tkSemiColon': continue
        if token.name == 'tkNewline': continue
        if token.name == 'tkTab': continue

        res.append(Token(token.name, token.value))
    return res