import random
from enum import Enum
import gram
import machine 
import networkx as nx
import matplotlib.pyplot as plt

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
# m1.showStatesDiagram()


m2 = machine.Machine()
m2.addRule((m2.startState, m2.startState + '0'))
m2.addRule((m2.startState, '0' + m2.startState))
m2.addRule((m2.startState, 'D'))
m2.addRule(('D', 'DD'))
m2.addRule(('D', '1A'))
m2.addRule(('D', 'e'))
m2.addRule(('A', '0B'))
m2.addRule(('A', 'e'))
m2.addRule(('B', '0A'))
m2.addRule(('B', '0A'))
m2.autoSetRulesAndStatesByTransitions()
# m2.showStatesDiagram()


def showStatesDiagram(self):
    options = {
        'node_color': 'Blue',
        'arrowstyle': '-|>',
        'arrowsize': 18,
    }
    g = nx.DiGraph()
    # Добавляем состояния
    g.add_node("H", shape="circle", color="blue")
    g.add_node("S", shape="circle", color="blue")
    g.add_node("A", shape="circle", color="blue")
    g.add_node("B", shape="circle", color="blue")


    # Добавляем переходы
    g.add_edge('S', 'S', label="0, 0")
    g.add_edge('D', 'S', label="")
    g.add_edge('D', 'D', label="D")
    g.add_edge('A', 'D', label="1")
    g.add_edge('H', 'D', label="e")
    g.add_edge('B', 'A', label="0")
    g.add_edge('H', 'A', label="e")
    g.add_edge('A', 'B', label="0")
    g.add_edge('H', 'B', label="0")

    # edges = []
    # edgesWithlabels = dict()
    # ts = self.getStatesTransitions()
    # rules = ''
    # lts = len(ts)
    # for i in range(lts):
    #     edge = (ts[i][0], ts[i][2])
    #     if (edge not in edges):
    #         edges.append(edge)
    #         rules = ''

    #     rules += ts[i][1] + '; '
    #     edgesWithlabels.update({edge: rules[0:-2]})

    # pos = nx.spiral_layout(g)
    # g.add_edges_from(edges)
    # nx.draw(g, pos, with_labels=True, **options)
    # nx.draw_networkx_edge_labels(g, pos, edgesWithlabels)

    # for edge, label in edgesWithlabels.items():
    #     if edge[0] == edge[1]:
    #         x, y = pos[edge[0]]
    #         plt.text(x, y + 0.25, label, ha='center', va='center')
    # plt.show()

G = nx.DiGraph()

# Добавляем состояния
G.add_node("H", shape="circle", color="blue")
G.add_node("S", shape="circle", color="blue")
G.add_node("A", shape="circle", color="blue")
G.add_node("B", shape="circle", color="blue")


# Добавляем переходы
G.add_edge('S', 'S', label="0, 0")
G.add_edge('D', 'S', label="")
G.add_edge('D', 'D', label="D")
G.add_edge('A', 'D', label="1")
G.add_edge('H', 'D', label="e")
G.add_edge('B', 'A', label="0")
G.add_edge('H', 'A', label="e")
G.add_edge('A', 'B', label="0")
G.add_edge('H', 'B', label="0")

# Изменяем масштаб для лучшей видимости
pos = nx.spring_layout(G, seed=42, scale=2.5)

# Рисуем граф
nx.draw_networkx(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()




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

# Множество состояний
class State3:
    H, D, A, B, S, ERROR = range(6)

def analizator3(text):
    current_state = State3.H
    # count = 0
    # txtsize = len(text)
    count = len(text)-1
    txtsize = 0
    res = ""
    while current_state != State3.ERROR and current_state != State3.S and count >= txtsize:
        # print(state_to_string(current_state))

        match current_state:

            case State3.H:
                if text[count] in ('e'):
                    current_state = State3.D
                    # print('H->D\n')
                elif text[count] in ('e'):
                    current_state = State3.A
                    # print('H->A\n')
                elif text[count] in ('0'):
                    current_state = State3.B
                    # print('H->B\n')
                else:
                    current_state = State3.ERROR

            case State3.B:
                if text[count] in ('0'):
                    current_state = State3.A
                    # print('B->A\n')
                else:
                    current_state = State3.ERROR

            case State3.A:
                if text[count] in ('0'):
                    current_state = State3.B
                    # print('A->B\n')
                elif text[count] in ('1'):
                    current_state = State3.S
                    # print('A->S\n')
                else:
                    current_state = State3.ERROR

            case State3.D:
                # print('D1->S\n')
                current_state = State3.S
                # print('D->S\n')

            case State3.D:
                current_state = State3.D
                # print('D->D\n')

            case State3.S:
                if text[count] in ('0'):
                    current_state = State3.S
                    # print('S->S\n')
                elif text[count] in ('0'):
                    current_state = State3.S
                else:
                    current_state = State3.ERROR


        res += state_to_string(current_state) + " "
        # count += 1
        count -= 1
    if contains_S(res):
        return "Цепочка принадлежит грамматике"
    else:
        return "Цепочка не принадлежит грамматике"


# Анализатор для задания по варианту
def analizator23(text):
    current_state = State3.H
    # count = 0
    # txtsize = len(text)
    count = len(text)-1
    txtsize = 0
    res = ""
    
    while current_state != State3.ERROR and current_state != State3.S and count >= txtsize:
        if current_state == State3.H:
            if text[count] in ('e'):
                current_state = State3.D
                print('H->D\n')
            elif text[count] in ('e'):
                current_state = State3.A
                print('H->A\n')
            elif text[count] in ('0'):
                current_state = State3.B
                print('H->B\n')
            else:
                current_state = State3.ERROR
        
        
        elif current_state == State3.B:
            if text[count] in ('0'):
                current_state = State3.A
                print('B->A\n')
            else:
                current_state = State3.ERROR
        
        
        elif current_state == State3.A:
            if text[count] in ('0'):
                current_state = State3.B
                print('A->B\n')
            elif text[count] in ('1'):
                current_state = State3.D
                print('A->D\n')
            else:
                current_state = State3.ERROR
        
        
        elif current_state == State3.D:
            print('D1->S\n')
            current_state = State3.S
            print('D->S\n')
        # elif current_state == State3.D:
        #     current_state = State3.D
        #     print('D->D\n')
        
        
        elif current_state == State3.S:
            if text[count] in ('0'):
                current_state = State3.S
                # print('S->S\n')
            # elif text[count] in ('0'):
            #     current_state = State3.S
            else:
                current_state = State3.ERROR
        
        # print(state_to_string(current_state))
        res += state_to_string(current_state) + " "
        # count += 1
        count -= 1
        #видит начало, не видит конца 
    if contains_S(res):
        return "Цепочка принадлежит грамматике"
    else:
        return "Цепочка не принадлежит грамматике"

# Функция для печати диаграммы состояний на экран
def print_diagram(a):
    for row in a:
        for item in row:
            print(f"| {item}", end=" ")
        print("|")


# print('\n\n\n')

# print("Лабораторная работа 2. Задание 1.")
# print("\nГрамматика языка: G = ({0, 1, .}, {N, P, S}, P, N")

# # Создание правил языка
# rules1 = [
# Rule("S", "S0"),
# Rule("S", "S1"),
# Rule("S", "P0"),
# Rule("S", "P1"),
# Rule("P", "N."),
# Rule("N", "0"),
# Rule("N", "1"),
# Rule("N", "N0"),
# Rule("N", "N1")
# ]

# language1 = gram.Language(rules1)
# print("\nПравила:")
# print(language1.get_rules())
# print("Язык, который порождает эта грамматика:")
# language1.find_language()

# print("\n11.010:", analizator21("11.010"))
# print("0.1:", analizator21("0.1"))
# print("01.:", analizator21("01."))
# print("100:", analizator21("100"))

# print('\n\n\n')

# print("Лабораторная работа 2. Задание 2.")
# print("\nГрамматика языка: G = ({0, 1, |, +, -}, {H, A, B, S}, P, H")

# rules2=[
#     Rule("S", "A|"),
#     Rule("A", "0"),
#     Rule("A", "1"),
#     Rule("A", "A0"),
#     Rule("A", "A1"),
#     Rule("A", "B0"),
#     Rule("A", "B1"),
#     Rule("B", "A+"),
#     Rule("B", "A-"),
# ]

# language2 = gram.Language(rules2)
# print("\nПравила:")
# print(language2.get_rules())
# print("Язык, который порождает эта грамматика:")
# language2.find_language()

# print("\n1011|:", analizator22("1011|"))
# print("10+011|:", analizator22("10+011|"))
# print("0-101+1|:", analizator22("0-101+1|"))

print('\n\n\n')

print("Лабораторная работа 2. Задание 3.")

print("\nГрамматика языка: G = ({0, 1, e}, {H, A, B, D, S}, P, H")
print('Это контекстно-свободная грамматика')
# Создание правил языка для задания по варианту
rules3 = [
Rule("S", "S0"),
Rule("S", "0S"),
Rule("S", "D"),
Rule("D", "DD"),
Rule("D", "1A"),
Rule("D", "e"),
Rule("A", "0B"),
Rule("A", "e"),
Rule("B", "0A"),
Rule("B", "0")
]

language3 = gram.Language(rules3)
print("\nПравила:")
print('S -> 0S | S0 | D\nD -> DD | 1A | ε\nA -> 0B | ε\nB -> 0A | 0')
# print(language3.get_rules())
print("\nЯзык, который порождает эта грамматика:")
# language3.find_language()
print('L = { \'1\'^n0,\'0\'^m0,\'ε\'^k0, | ni > 0, mi > 0, k > 0}')

print('\nграмматика почти эквивалентная данной:')
print('S -> 0S | S0 | D\nD -> DD | 1A | εA\nA -> 0B | εB | ε\nB -> 0A | 0')

analiz_str = "100"
print(f"Строка для анализа: {analiz_str}")
print("Анализатор:", analizator3(analiz_str))
analiz_str = "0100"
print(f"Строка для анализа: {analiz_str}")
print("Анализатор:", analizator3(analiz_str))
analiz_str = "1"
print(f"Строка для анализа: {analiz_str}")
print("Анализатор:", analizator3(analiz_str))

print('\n\n\n')

