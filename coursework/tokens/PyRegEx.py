PyRegExList = (
    r'\n',          # Новая строка
    r'\s{4}',       # Табуляция
    r'\s',          # Пробел

    r'print',       # Вывод
    r'input',       # Ввод

    r'int',         # integer
    r'float',       # float
    r'str',         # string
    r'bool',        # boolean
    r'viod',        # void

    r'\;',          # ;
    r'\:',          # :
    r'\,',          # ,
    r'\.',          # .

    r'\(', r'\)',   # ( )
    r'\[', r'\]',   # [ ]
    r'\{', r'\}',   # { }

    r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)',         # integer
    r'[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?', # float
    r'[\'\"].*[\'\"]',                              # string
    r'True|False',                                  # boolean

    r'\*\*\=',      # **=
    r'\+\=',        # +=
    r'\-\=',        # -=
    r'\*\=',        # *=
    r'\/\=',        # /=
    r'\%\=',        # %=
    r'\/\/\=',      # //=

    r'\*\*',        # **
    r'\+',          # + 
    r'\-',          # -
    r'\*',          # *
    r'\/',          # /
    r'\%',          # %
    r'\/\/',        # //

    r'>>',          # >>
    r'<<',          # <<
    r'end=[\'\"]\n[\'\"]',  # endl

    r'\=\=',        # ==
    r'\!\=',        # !=
    r'\>\=',        # >=
    r'\<\=',        # <=
    r'\<',          # <
    r'\>',          # >

    r'\=',          # =

    r'and',         # and
    r'or',          # or
    r'not',         # not

    r'False',       # False
    r'True',        # True

    r'if',          # if
    r'elif',        # elif
    r'else',        # else

    r'for',         # for
    r'in',          # in
    r'range',       # range
    r'while',       # while
    r'continue',    # continue
    r'break',       # break

    r'del',         # del

    r'None',        # None

    r'[a-zA-Z_][a-zA-Z0-9_]*' # Идентификатор переменной
)