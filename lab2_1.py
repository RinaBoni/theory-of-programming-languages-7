import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum


class Rule:
    def __init__(self, key, value, is_cycled=False):
        self.key = key
        self.value = value
        self.is_cycled = is_cycled

class Language:
    def __init__(self, rules):
        self.rules = rules

    def get_rules(self):
        result = ""
        for rule in self.rules:
            result += f"{rule.key}-->{rule.value}\n"
        return result

    def find_chain(self, word):
        def find(word):
            new_word = word
            for k in range(1, len(word) + 1):
                term_character = ""
                for i in range(len(word) - k, -1, -1):
                    term_character = word[i] + term_character
                    for rule in self.rules:
                        if rule.value == term_character:
                            new_word = word[:i] + rule.key + word[i + len(term_character):]
                            new_word_copy = new_word
                            new_word = find(new_word)
                            if new_word == "S":
                                print(f"{new_word_copy}\n{rule.key}-->{rule.value}")
                                return new_word
            if new_word != "S":
                new_word = "Строка не выводима"
            return new_word

        return find(word)

    def find_language(self):
        def find_grammar(max_length=30, word="S", n=0):
            new_word = word
            for i in range(len(word)):
                term_character = ""
                for j in range(i, len(word)):
                    term_character += word[j]
                    for rule in self.rules:
                        if rule.key == term_character and n < max_length:
                            new_word = word[:i] + rule.value + word[i + len(term_character):]
                            n += 1
                            new_word = find_grammar(max_length, new_word, n)
                            c = 0
                            if n == max_length - 1:
                                for rule2 in self.rules:
                                    if rule2.key in new_word:
                                        c += 1
                                if c == 0:
                                    return new_word
            return new_word

        result = find_grammar(10)
        output = "L = { "
        count = 0
        char_count = []
        for char in result:
            char_found = False
            for i, pair in enumerate(char_count):
                if pair[0] == char:
                    char_count[i] = (char, pair[1] + 1)
                    count += 1
                    char_found = True
            if not char_found:
                char_count.append((char, 0))
            count = 0
        count2 = 0
        count3 = 0
        for pair1 in char_count:
            for pair2 in char_count:
                if pair1[1] == pair2[1]:
                    count += 1
            if count == 1:
                output += f"'{pair1[0]}'^n{count3}, "
                count = 0
                count3 += 1
            else:
                output += f"'{pair1[0]}'^m{count2}, "
                count2 += 1
                count = 0
        output += "|"
        if count3 != 0:
            output += " ni > 0"
        if count2 != 0:
            output += ", mi > 0"
        output += "}"
        print(output)


# class FiniteAutomaton:
#     def __init__(self):
#         self.states = {'S', 'P', 'N'}
#         self.alphabet = {'0', '1', '.'}
#         self.transitions = {
#             ('S', '0'): 'N',
#             ('S', '1'): 'N',
#             ('S', 'P'): 'P',
#             ('P', '.'): 'N',
#             ('N', '0'): 'N',
#             ('N', '1'): 'N',
#             ('N', 'N0'): 'N',
#             ('N', 'N1'): 'N'
#         }
#         self.start_state = 'S'
#         self.accept_states = {'N'}

#     def is_accepted(self, input_string):
#         current_state = self.start_state
#         for symbol in input_string:
#             if (current_state, symbol) not in self.transitions:
#                 return False
#             current_state = self.transitions[(current_state, symbol)]
#         return current_state in self.accept_states





class State(Enum):
    H = 0
    N = 1
    P = 2
    S = 4

class FiniteAutomaton:
    def __init__(self):
        self.current_state = 'H'

    def transition(self, input_symbol):
        count = 0
        while count < len(input_symbol):
            if self.current_state == 'S':
                if input_symbol[count] == '0':
                    self.current_state = 'S0'
                elif input_symbol[count] == '1':
                    self.current_state = 'S1'
                elif input_symbol == 'P':
                    self.current_state = 'P0'
            elif self.current_state == 'S0' or self.current_state == 'S1':
                if input_symbol == '0' or input_symbol == '1':
                    self.current_state = 'N'
            elif self.current_state == 'P0':
                if input_symbol == '.':
                    self.current_state = 'N'
            elif self.current_state == 'N':
                if input_symbol == '0':
                    self.current_state = 'N0'
                elif input_symbol == '1':
                    self.current_state = 'N1'
        
    def check_string(self, input_string):
        for symbol in input_string:
            self.transition(symbol)

        if self.current_state == 'N':
            return True
        else:
            return False

def ans(answer):
    if answer=='y':
        input_string = input("Введите строку: ")
        automaton = FiniteAutomaton()
        result = automaton.check_string(input_string)

        if result:
            print("Строка принадлежит грамматике.")
        else:
            print("Строка не принадлежит грамматике.")
        
        # automaton = FiniteAutomaton()
        # input_string = input("Введите строку: ")
        # if automaton.is_accepted(input_string):
        #     print("Строка принадлежит грамматике")
        # else:
        #     print("Строка не принадлежит грамматике")
        answer = input("Вы хотите ввести строку? (y/n) ")
        ans(answer)
    else:
        pass


rules = [
        Rule("S", "S0"),
        Rule("S", "S1"),
        Rule("S", "P0"),
        Rule("S", "P1"),
        Rule("P", "N."),
        Rule("N", "0"),
        Rule("N", "1"),
        Rule("N", "N0"),
        Rule("N", "N1"),
    ]



language1 = Language(rules)
print("\n\n\nПравила:")
print(language1.get_rules())

print("                                                                      \n"
          "                        _________                                        \n"
          "                       | <-(1;0)-|                                         \n"
          "->start H----(1;0)---->N                                       \n"
          "                       |                                      \n"
          "                       .                                      \n"
          "                       |                  __________                      \n"
          "                       v                 |<--(1;0)--|                       \n"
          "                       P------(1;0)----->S                                \n"
          "                                                                      \n"
          "                                                                      \n"
          "                                                                      \n")

print("Язык, который порождает эта грамматика:")
language1.find_language()
answer = input("Вы хотите ввести строку? (y/n) ")
ans(answer)



G = nx.DiGraph()

# Добавляем состояния
G.add_node("H", shape="circle", color="blue")
G.add_node("S", shape="circle", color="blue")
G.add_node("P", shape="circle", color="blue")
G.add_node("N", shape="circle", color="blue")


# Добавляем переходы
G.add_edge('H', 'N', label="0, 1")
G.add_edge('N', 'N', label="0, 1")
G.add_edge('N', 'P', label=".")
G.add_edge('S', 'S', label="0, 1")
G.add_edge('P', 'S', label="0, 1")

# Изменяем масштаб для лучшей видимости
pos = nx.spring_layout(G, seed=42, scale=2.5)

# Рисуем граф
nx.draw_networkx(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()






# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
# G.add_weighted_edges_from([('H', 'N', '0.1'), ('N', 'N', '0.1'), ('N', 'P', '1'), ('S', 'S', '0.1'), ('P', 'S', '0.1')])

# # nx.draw_spring(G, with_labels=True)
# # plt.show()


# # Получение позиций вершин для отображения
# pos = nx.spring_layout(G)

# # Рисование графа с весами на ребрах
# nx.draw(G, pos, with_labels=True, node_size=500, font_size=12, node_color='lightblue', edge_color='gray')

# # Отображение весов на ребрах
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.5, font_size=10)

# # Показать граф
# plt.show()