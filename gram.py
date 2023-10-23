class Rule:
    def __init__(self, key, value, is_cycled=False):
        self.key = key
        self.value = value
        self.is_cycled = is_cycled

def print_rules(R):
    print("Правила для языка")
    for i in range(len(R)):
        print("   \u2022" + R[i].key + "-->" + R[i].value)


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

