import random
from enum import Enum
import gram
import machine 

m1 = machine.Machine()
m1.addRule((m1.startState, m1.startState + '0'))
m1.addRule((m1.startState, m1.startState + '1'))
m1.addRule((m1.startState, 'P0'))
m1.addRule((m1.startState, 'P1'))
m1.addRule(('P', 'N.'))
m1.addRule(('N', 'N1'))
m1.addRule(('N', 'N0'))
m1.addRule(('N', '1'))
m1.addRule(('N', '0'))
m1.autoSetRulesAndStatesByTransitions()
m1.showStatesDiagram()




# Правила языка
class Rule:
    def __init__(self, k, v, l=False):
        self.key = k
        self.value = v
        self.IsLooped = l

    def __str__(self):
        return f"{self.key} --> {self.value}"

# Функция для печати правил на экран
def print_rules(arr):
    print("Правила языка:")
    for rule in arr:
        print(rule)

# Множество состояний
class State:
    H, C, D, S, N, P, B, A, ERROR = range(9)

# Функция для выбора случайного состояния из двух вариантов
def random_state(a, b):
    return random.choice([a, b])

# Функция для преобразования состояния в строку
def state_to_string(current_state):
    states = ["H", "C", "D", "S", "N", "P", "B", "A", "ERROR"]
    return states[current_state]

# Анализатор 2.1
def analizator21(text):
    current_state = State.H
    # current_state = State.N
    count = 0
    txtsize = len(text)
    res = ""
    
    while current_state != State.ERROR and current_state != State.S and count < txtsize:
        if current_state == State.H:
            if text[count] in ('1', '0'):
                current_state = State.N
            else:
                current_state = State.ERROR
        elif current_state == State.N:
            if text[count] in ('1', '0'):
                current_state = State.N
            elif text[count] == '.':
                current_state = State.P
            else:
                current_state = State.ERROR
        elif current_state == State.P:
            if text[count] in ('1', '0'):
                current_state = State.S
            else:
                current_state = State.ERROR
        elif current_state == State.S:
            if text[count] in ('1', '0'):
                current_state = State.S
            else:
                current_state = State.ERROR
        
        res += state_to_string(current_state) + " "
        count += 1
    
    

    if contains_S(res):
        return "Цепочка принадлежит грамматике"
    else:
        return "Цепочка не принадлежит грамматике"

    # return res


def contains_S(input_string):
    return 'S' in input_string


# Анализатор 2.2
def analizator22(text):
    current_state = State.H
    count = 0
    txtsize = len(text)
    res = ""
    
    while current_state != State.ERROR and current_state != State.S and count < txtsize:
        if current_state == State.H:
            if text[count] in ('1', '0'):
                current_state = State.A
        elif current_state == State.A:
            if text[count] in ('1', '0'):
                current_state = State.A
            if text[count] == '|':
                current_state = State.S
            if text[count] in ('+', '-'):
                current_state = State.B
        elif current_state == State.S:
            current_state = State.ERROR
        elif current_state == State.B:
            if text[count] in ('1', '0'):
                current_state = State.A
        else:
            current_state = State.ERROR
        res += state_to_string(current_state) + " "
        count += 1
    

    if contains_S(res):
        return "Цепочка принадлежит грамматике"
    else:
        return "Цепочка не принадлежит грамматике"



# Анализатор для задания по варианту
def analizator2(text):
    current_state = State.H
    count = 0
    txtsize = len(text)
    res = ""
    
    while current_state != State.ERROR and current_state != State.S and count < txtsize:
        if current_state == State.H:
            current_state = State.S
        elif current_state == State.S:
            if text[count] in ('1', '0'):
                current_state = State.D
            if text[count] in ('+', '-'):
                current_state = State.B
        elif current_state == State.D:
            if text[count] == '0':
                current_state = random_state(State.S, State.C)
        elif current_state == State.C:
            if text[count] == '1':
                current_state = random_state(State.S, State.D)
        else:
            current_state = State.ERROR
        
        res += state_to_string(current_state) + " "
        count += 1
    
    return res

# Функция для печати диаграммы состояний на экран
def print_diagram(a):
    for row in a:
        for item in row:
            print(f"| {item}", end=" ")
        print("|")


print('\n\n\n')

print("Лабораторная работа 2. Задание 1.")
print("\nГрамматика языка: G = ({0, 1, .}, {N, P, S}, P, N")

# Создание правил языка
rules1 = [
Rule("S", "S0"),
Rule("S", "S1"),
Rule("S", "P0"),
Rule("S", "P1"),
Rule("P", "N."),
Rule("N", "0"),
Rule("N", "1"),
Rule("N", "N0"),
Rule("N", "N1")
]

language1 = gram.Language(rules1)
print("\nПравила:")
print(language1.get_rules())
print("Язык, который порождает эта грамматика:")
language1.find_language()

print("\n11.010:", analizator21("11.010"))
print("0.1:", analizator21("0.1"))
print("01.:", analizator21("01."))
print("100:", analizator21("100"))

print('\n\n\n')

print("Лабораторная работа №2. Общее задание №2.")
print("\nГрамматика языка: G = ({0, 1, |, +, -}, {H, A, B, S}, P, H")

rules2=[
    Rule("S", "A|"),
    Rule("A", "0"),
    Rule("A", "1"),
    Rule("A", "A0"),
    Rule("A", "A1"),
    Rule("A", "B0"),
    Rule("A", "B1"),
    Rule("B", "A+"),
    Rule("B", "A-"),
]

language2 = gram.Language(rules2)
print("\nПравила:")
print(language2.get_rules())
print("Язык, который порождает эта грамматика:")
language2.find_language()

print("\n1011|:", analizator22("1011|"))
print("10+011|:", analizator22("10+011|"))
print("0-101+1|:", analizator22("0-101+1|"))

print('\n\n\n')

# print("Лабораторная работа №2. Задание по вариантам. Вариант 12.")

# # Создание правил языка для задания по варианту
# rules2 = [
# Rule("S", "1C"),
# Rule("S", "0D"),
# Rule("C", "0D"),
# Rule("C", "0S"),
# Rule("C", "1"),
# Rule("D", "1C"),
# Rule("D", "1S"),
# Rule("D", "0")
# ]

# print_rules(rules2)

# analiz_str = "0101"
# print(f"Строка для анализа: {analiz_str}")
# print("Анализатор:", analizator2(analiz_str))

# print("Диаграмма переходов:")
# diagr = [
# [" ", "C", "D", "S"],
# ["0", " ", "C,D", "C"],
# ["1", "S,D", " ", "D"]]