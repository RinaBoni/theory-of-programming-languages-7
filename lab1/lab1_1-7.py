import random

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Rule:
    def __init__(self, key, value, is_looped):
        self.key = key
        self.value = value
        self.is_looped = is_looped

def print_rules(R):
    print("Правила для языка")
    for i in range(len(R)):
        print("   \u2022" + R[i].key + "-->" + R[i].value)

class Language:
    def __init__(self, rules, count=10000):
        self.rules = rules
        self.MaxRepetitionsCount = count

    def set_rules(self, rules):
        self.rules = rules

    def get_rules(self):
        str = ""
        for rule in self.rules:
            str += rule.key + "-->" + rule.value + "\n"
        return str

 
    def get_MaxRepetitionsCount(self):
        return self.MaxRepetitionsCount

    def set_MaxRepetitionsCount(self, value):
        self._max_repetitions_count = value

    

    def output_left(self):
        result = "S"
        count = 0
        while count < self.MaxRepetitionsCount:
            pos = -1
            for rule in self.rules:
                key = rule.key
                findPos = result.find(key)
                if (pos > findPos or pos == -1) and findPos != -1:
                    pos = findPos
            if pos == -1:
                break
            matching_rules = [rule for rule in self.rules if pos == result.find(rule.key)]
            random_index = random.randint(0, len(matching_rules) - 1)
            selected_rule = matching_rules[random_index]
            p = result.find(selected_rule.key)
            result = result[:p] + selected_rule.value + result[p + len(selected_rule.key):]
            count += 1
        return result

    def translate(self, text):
        count = 0
        isEnd = False  # true - если ни одно из правил неприменимо
        while count < self.MaxRepetitionsCount:
            if isEnd:
                break
            count += 1
            isEnd = True
            for rule in self.rules:
                if not rule.is_looped:
                    key = rule.key
                    value = rule.value
                    pos = text.find(key)
                    if pos != -1:
                        if self.check_loop(text, rule):
                            rule.is_looped = True
                        else:
                            text = text[:pos] + value + text[pos + len(key):]
                            isEnd = False
                            break
                else:
                    rule.is_looped = not rule.is_looped
        self.refresh_rules()
        return text

    def refresh_rules(self):
        for rule in self.rules:
            rule.is_looped = False

    def findChain(self, word):
        newWord = word
        for k in range(1, len(word) + 1):
            termCharacter = ""
            for i in range(len(word) - k, -1, -1):
                termCharacter = word[i] + termCharacter
                for j in range(len(self.rules)):
                    if self.rules[j].value == termCharacter:
                        newWord = word[:i] + self.rules[j].key + word[i + len(termCharacter):]
                        str = newWord
                        newWord = self.findChain(newWord)
                        if newWord == "S":
                            print(str + "\n" + "   \u2022" + self.rules[j].key + "-->" + self.rules[j].value)
                            return newWord
        return newWord

    def find_grammar(self, max=30, word="S", n=0):  # Добавляем self как параметр
        new_word = word
        for i in range(len(word)):
            term_character = ""
            for j in range(i, len(word)):
                term_character += word[j]
                for rule in self.rules:  # Используем self.rules
                    if rule.key == term_character and n < max:
                        new_word = word[:i] + rule.value + word[i + len(term_character):]
                        n += 1
                        new_word = self.find_grammar(max, new_word, n)  # Используем self.find_grammar
                        c = 0
                        if n == max - 1:
                            for rule2 in self.rules:  # Используем self.rules
                                if rule2.key in new_word:
                                    c += 1
                            if c == 0:
                                return new_word
        return new_word
    
    def find_language(self):  # Добавляем self
        str1 = self.find_grammar(10)  # Не передаем rules явно, используем self.rules
        str2 = self.find_grammar(20)  # Не передаем rules явно, используем self.rules
        # print(str1)
        # print(str2)
        output = "L = { "
        count = 0
        list = []
        for i in range(len(str1)):
            for pair in list:
                if pair[0] == str1[i]:
                    pair[1] += 1
                    count += 1
            if count == 0:
                list.append([str1[i], 0])
            count = 0
        count = 0
        count2 = 0
        count3 = 0
        for pair1 in list:
            for pair2 in list:
                if pair1[1] == pair2[1]:
                    count += 1
            # print(count)
            if count == 1:
                output += "'" + pair1[0] + "'" + "^n" + str(count3) + ", "
                count = 0
                count3 += 1
            else:
                output += "'" + pair1[0] + "'" + "^m" + str(count2) + ", "
                count2 += 1
            count = 0
        output += "|"
        if count3 != 0:
            output += " ni > 0"
        if count2 != 0:
            output += ", mi > 0"
        output += "}"
        print(output)

    def check_loop(self, input, rule, count=5):
        n = 5
        for i in range(n):
            key = rule.key
            value = rule.value

            pos = input.find(key)

            if pos != -1:
                input = input[:pos] + value + input[pos + len(key):]
            else:
                return False

        return True

    def generate_grammar2(self):
        str = self.find_grammar()
        output = "Грамматика ( "
        characters = []
        for i in range(len(str)):
            ch = str[i]
            if ch not in characters:
                characters.append(ch)
        output += "{"
        while len(characters) > 1:
            output += " " + characters.pop() + ","
        output += characters.pop() + "} | "


class Grammar:
    """
    Множество терминальных символов
    """
    def __init__(self, nonterminal, terminal, P, S="S"):
        self.nonterminal = nonterminal
        self.terminal = terminal
        self.P = P
        self.S = S

    
    def set_nonterminal(self, nonterminal):
        self.nonterminal = nonterminal
    def get_nonterminal(self):
        return self.nonterminal
  
    def set_terminal(self, terminal):
        self.terminal = terminal
    def get_terminal(self):
        return self.terminal
    
    def set_P(self, P):
        self.P = P
    def get_P(self):
        return self.P

    def set_S(self, S):
        self.S = S
    def get_S(self):
        return self.S
    
    def get_type_grammar(self):
        is_type_one = True
        is_type_two = True
        is_type_three = True

        is_each_term_pos_bigger = True
        is_each_term_pos_smaller = True

        for r in self.P:
            # Проверка принадлежности первому типу грамматики
            is_type_one &= len(r['key']) <= len(r['value'])

            # Проверка принадлежности второму типу
            for vt in self.terminal:
                is_type_two &= vt not in r['key']

            if is_each_term_pos_bigger or is_each_term_pos_smaller:
                terminal_positions = []
                non_terminal_positions = []
                for vn in self.nonterminal:
                    temp = r['value'].find(vn)
                    if temp != -1:
                        non_terminal_positions.append(temp)

                for vt in self.terminal:
                    temp = r['value'].find(vt)
                    if temp != -1:
                        terminal_positions.append(temp)

                for pos in terminal_positions:
                    for pos_non_term in non_terminal_positions:
                        is_each_term_pos_bigger &= pos > pos_non_term
                        is_each_term_pos_smaller &= pos < pos_non_term

                if not (is_each_term_pos_bigger or is_each_term_pos_smaller):
                    is_type_three = False

        print("Относится к типам по Хомскому:")
        res = "0"
        if is_type_one:
            res += " 1"
        if is_type_two:
            res += " 2"
        if is_type_three:
            res += " 3"
        print(res)
        return res

    def make_tree(self, text):
        max_count = 10000
        count = 0
        tree = [text]
        
        while count < max_count:
            for rule in self.P:
                key = rule['key']
                value = rule['value']
                
                pos = text.rfind(value)
                
                if pos != -1:
                    text = text[:pos] + key + text[pos + len(value):]
                    separator = "|" + " " * pos
                    tree.append(separator)
                    tree.append(text)
            
            count += 1

        tree.reverse()
        
        for branch in tree:
            print(branch)
        
        return text

def task_one():
    rules = [
        Rule("S", "T", False),
        Rule("S", "T+S", False),
        Rule("S", "T-S", False),
        Rule("T", "F*T", False),
        Rule("T", "F", False),
        Rule("F", "a", False),
        Rule("F", "b", False)
    ]
    language = Language(rules)

    rules1 = [
        Rule("S", "aSBC", False),
        Rule("S", "abC", False),
        Rule("bB", "bb", False),
        Rule("CB", "BC", False),
        Rule("bC", "bc", False),
        Rule("cC", "cc", False)
    ]
    language1 = Language(rules1)

    word = "a-b*a+b"
    word2 = "aaabbbccc"

    print("а) Цепочка создания слова: " + word)
    language.findChain(word)
    print(word)

    print("b) Цепочка создания слова: " + word2)
    language1.findChain(word2)
    print(word2)
    
def task_two():
    rules = [
        Rule("S", "aaCFD", False),
        Rule("AD", "D", False),
        Rule("F", "AFB", True),
        Rule("F", "AB", False),
        Rule("Cb", "bC", False),
        Rule("AB", "bBA", False),
        Rule("CB", "C", False),
        Rule("Ab", "bA", False),
        Rule("bCD","e", False),
    ]
    language = Language(rules)

    rules1 = [
        Rule("S","A/", False),
        Rule("S","B/", False),
        Rule("A","a", False),
        Rule("A","Ba", False),
        Rule("B","b", False),
        Rule("B","Bb", False),
        Rule("B","Ab", False),
    ]
    language1 = Language(rules1)

    print('Подпункт a) ')
    print_rules(rules)
    language.find_language()
    print()

    print('Подпункт b) ')
    print_rules(rules1)
    language1.find_language()
    print('\n\n')
        
def task_three():
    dict_rules = [
        Rule("S", "aaB", False),
        Rule("B", "bCCCC", False),
        Rule("B", "b", False),
        Rule("C", "Cc", False),
        Rule("C", "c", False),
    ]
    
    
    print("Подпункт a)")
    print("Язык: L = { a^n b^m c^k | n, m, k > 0}")
    print("Грамматика: G: ({a, b, c}, {A, B, C}, P, S)")
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()
    
    print("Подпункт б)")
    print("Язык: L = {0^n(10)^m | n, m ≥ 0}")
    print("Грамматика: G: ({0, 10}, {A, B}, P, S)")
    dict_rules = [
        Rule("S", "0AB", False),
        Rule("A", "000", False),
        Rule("B", "1010", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()
    
    print("Подпункт в)")
    print("Язык: L = {a1 a2 … an an … a2a1 | ai E {0, 1}}")
    print("Грамматика: G: ({0, 1}, {A, B}, P, S)")
    dict_rules = [
        Rule("S", "AB", False),
        Rule("A", "1001010", False),
        Rule("B", "0101001", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()

def task_four():
    print("Подпункт a)")
    dict_rules = [
        Rule("S", "0A1", False),
        Rule("S", "01", False),
        Rule("0A", "00A1", False),
        Rule("A", "01", False),
    ]
    
    print_rules(dict_rules)
    print("Грамматика: G: ({0, 1}, {S, A}, P, S)")
    print('Тип по Хомскому: 2) контекстно-свободная')
    # gramm = Grammar(["0", "1"], ["S", "A"], dict_rules, "S")
    # print('Тип по Хомскому:', gramm.get_type_grammar())

    
    
    print()
    
    print("Подпункт б)")
    dict_rules = [
        Rule("S", "Ab", False),
        Rule("A", "Aa", False),
        Rule("A", "ba", False),
    ]
    
    print_rules(dict_rules)
    
    print("Грамматика: G: ({a, b}, {S, A}, P, S)")
    print('Тип по Хомскому: 2) контекстно-свободная')
    
    print()
    
def task_five():
    dict_rules = [
        Rule("S", "aSL", False),
        Rule("S", "aL", False),
        Rule("L", "Kc", False),
        Rule("cK", "Kc", False),
        Rule("K", "b", False),
    ]
    
    print_rules(dict_rules)
    print("Язык: L = {a^n b^m c^k | a, b, k > 0}")
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))

    
    print()
    
    dict_rules = [
        Rule("S", "aSBc", False),
        Rule("S", "abc", False),
        Rule("cB", "Bc", False),
        Rule("bB", "bb", False),
    ]
    
    print_rules(dict_rules)
    
    print("Язык: L = {a^n b^m c^k | a, b, k > 0}")
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print("Грамматики эквиваленты т.к. они определяют один и тот же язык")
    print()

def task_six():
    dict_rules = [
        Rule("S", "AB", False),
        Rule("S", "ABS", False),
        Rule("AB", "BA", False),
        Rule("BA", "AB", False),
        Rule("A", "a", False),
        Rule("B", "b", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    # print("Цепочка: " + fl.translate("S"))
    print("Цепочка: ab")

    print()
    print('Эквивалентраная грамматика:')
    dict_rules = [
        Rule("S", "ab", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()

def task_seven():
    dict_rules = [
        Rule("S", "A.A", False),
        Rule("A", "B", False),
        Rule("A", "BA", False),
        Rule("B", "0", False),
        Rule("B", "1", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()

    print('Эквивалентраная грамматика:')
    
    dict_rules = [
        Rule("S", "A.0", False),
        Rule("A", "0", False),
        Rule("A", "1", False),
    ]
    
    print_rules(dict_rules)
    
    fl = Language(dict_rules)
    print("Цепочка: " + fl.translate("S"))
    print()

def task_eleven():
    dict_rules = [
        Rule("S", "0S", False),
        Rule("S", "0B", False),
        Rule("B", "1B", False),
        Rule("B", "1C", False),
        Rule("C", "1C", False),
        Rule("C", "|", False),
    ]


    
    
    
    

    
def main():
    print('\n#############################       Задание один       #############################')
    task_one()
    print('\n#############################       Задание два       #############################')
    task_two()
    print('\n#############################       Задание три       #############################')
    task_three()
    print('\n#############################       Задание четыре       #############################')
    task_four()
    print('\n#############################       Задание пять       #############################')
    task_five()
    print('\n#############################       Задание шесть       #############################')
    task_six()
    print('\n#############################       Задание семь       #############################')
    task_seven()

    

if __name__ == "__main__":
	main()