from enum import Enum

class State(Enum):
    H = 0
    A = 1
    D = 2
    B = 3
    S = 4
    ER = 5

class State(Enum):
    H = 0
    N = 1
    P = 2
    S = 4

def Analizator(text):
    now = State.H
    count = 0
    res = ""
    while count < len(text):
        if now == State.S or text[count] == '\u00A7':
            break

        if now == State.H:
            if text[count] == '0': 
                now = State.N
            elif text[count] == '1': 
                now = State.N

        elif now == State.N:
            if text[count] == '0': 
                now = State.A
            elif text[count] == '1': 
                now = State.B
            else: 
                now = State.ER

        elif now == State.B:
            if text[count] == '0': 
                now = State.B
            elif text[count] == '1': 
                now = State.B
            else: 
                now = State.ER

        elif now == State.S:
            if text[count] == '1': 
                now = State.S
            elif text[count] == '0': 
                now = State.A
            else: 
                now = State.ER

        res += str(now)
        res += " "
        count += 1

    print(res)

# Example usage:
text = "010100101"
Analizator(text)