CRegExList = [
    r'\n',              # Новая строка
    r'\s{4}',           # Табуляция
    r'\s',              # Пробел

    r'cout',            # вывод
    r'cin',             # ввод

    r'int',             # integer
    r'float|double',    # float
    r'char\[[0-9]*\]',  # string
    r'bool',            # boolean
    r'void',            #void

    r'\;',              # ;
    r'\:',              # :
    r'\,',              # ,
    r'\.',              # .

    r'\(', r'\)',       # ( )
    r'\[', r'\]',       # [ ]
    r'\{', r'\}',       # { }

    r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)',         #integer
    r'[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?', #float
    r'[\'\"].*[\'\"]',                              #string
    r'1|0',                                         #boolean

    r'\*\*\=',          # **=
    r'\+\=',            # +=
    r'\-\=',            # -=
    r'\*\=',            # *=
    r'\/\=',            # /=
    r'\%\=',            # %=
    r'\/\/\=',          # //=

    r'\*\*',            # **
    r'\+',              # + 
    r'\-',              # -
    r'\*',              # *
    r'\/',              # /
    r'\%',              # %
    r'\/\/',            # //

    r'>>',              # >>
    r'<<',              # <<
    r'endl',            # endl

    r'\=\=',            # ==
    r'\!\=',            # !=
    r'\>\=',            # >=
    r'\<\=',            # <=
    r'\<',              # <
    r'\>',              # >

    r'\=',              # =

    r'\&\&',            # and
    r'\|\|',            # or
    r'\!',              # not

    r'False',           # False
    r'True',            # True

    r'if',              # if
    r'else if',         # elif
    r'else',            # else

    r'for',             # for
    r'in',
    r'range',           # range
    r'while',           # while
    r'continue',        # continue
    r'break',           # break

    r'free',            # del

    r'None',            # None

    r'[a-zA-Z_][a-zA-Z0-9_]*' # Идентификатор переменной
]