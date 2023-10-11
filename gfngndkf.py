import random

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

class Rule:
    def __init__(self, k, v, l=False):
        self.Key = k
        self.Value = v
        self.IsLooped = l


def print_rules(R):
    print("Правила для языка")
    for rule in R:
        print(f"   • {rule.Key} --> {rule.Value}")

def print_tree(node, level=0):
    if node:
        print("  " * level + node.symbol)
        for child in node.children:
            print_tree(child, level + 1)

class FormalLanguage:
    def __init__(self, rules, count=10000):
        self._rules = rules
        self.MaxRepetitionsCount = count

    def check_loop(self, input_str, rule, count=5):
        for _ in range(count):
            key = rule.Key
            value = rule.Value
            pos = input_str.find(key)
            if pos != -1:
                input_str = input_str[:pos] + value + input_str[pos + len(key):]
            else:
                return False
        return True

    def output_left(self):
        result = "S"
        count = 0
        while count < self.MaxRepetitionsCount:
            pos = -1
            for rule in self._rules:
                key = rule.Key
                find_pos = result.find(key)
                if (pos > find_pos or pos == -1) and find_pos != -1:
                    pos = find_pos

            if pos == -1:
                break

            rules = [rule for rule in self._rules if pos == result.find(rule.Key)]
            r = random.choice(rules)
            p = result.find(r.Key)
            result = result[:p] + r.Value + result[p + len(r.Key):]
            count += 1
        return result

    def build_tree(self, text):
        root = Node("S")
        stack = [(root, text)]
        count = 0

        while count < self.MaxRepetitionsCount and stack:
            node, text = stack.pop()
            count += 1
            pos = -1
            for rule in self._rules:
                key = rule.Key
                find_pos = text.find(key)
                if (pos > find_pos or pos == -1) and find_pos != -1:
                    pos = find_pos

            if pos == -1:
                continue

            rules = [rule for rule in self._rules if pos == text.find(rule.Key)]
            r = random.choice(rules)
            p = text.find(r.Key)
            new_text = text[:p] + r.Value + text[p + len(r.Key):]

            for symbol in new_text:
                child = Node(symbol)
                node.children.append(child)

            stack.extend([(child, new_text) for child in reversed(node.children)])

        return root

    def translate(self, text):
        count = 0
        is_end = False
        while count < self.MaxRepetitionsCount:
            if is_end:
                break
            count += 1
            is_end = True
            for rule in self._rules:
                if not rule.IsLooped:
                    key = rule.Key
                    value = rule.Value
                    pos = text.find(key)
                    if pos != -1:
                        if self.check_loop(text, rule):
                            rule.IsLooped = True
                        else:
                            text = text[:pos] + value + text[pos + len(key):]
                            is_end = False
                            break
                else:
                    rule.IsLooped = not rule.IsLooped
        self.refresh_rules()
        return text

    def refresh_rules(self):
        for rule in self._rules:
            rule.IsLooped = False

class Grammar:
    def __init__(self, vn, vt, rules, s="S"):
        self.Nonterminal = vn
        self.Terminal = vt
        self.P = rules
        self.S = s

    def get_type_grammar(self):
        is_type_one = True
        is_type_two = True
        is_type_three = True
        is_each_term_pos_bigger = True
        is_each_term_pos_smaller = True
        for r in self.P:
            is_type_one &= len(r.Key) <= len(r.Value)
            for vt in self.Terminal:
                is_type_two &= vt not in r.Key
            if is_each_term_pos_bigger or is_each_term_pos_smaller:
                terminl_positions = []
                non_terminl_positions = []
                for vn in self.Nonterminal:
                    temp = r.Value.find(vn)
                    if temp != -1:
                        non_terminl_positions.append(temp)
                for vt in self.Terminal:
                    temp = r.Value.find(vt)
                    if temp != -1:
                        terminl_positions.append(temp)
                for pos in terminl_positions:
                    for pos_non_term in non_terminl_positions:
                        is_each_term_pos_bigger &= pos > pos_non_term
                        is_each_term_pos_smaller &= pos < pos_non_term
                if not (is_each_term_pos_bigger or is_each_term_pos_smaller):
                    is_type_three = False
        result = "0"
        if is_type_one:
            result += " 1"
        if is_type_two:
            result += " 2"
        if is_type_three:
            result += " 3"
        return result

    def make_tree(self, text):
        max_count = 10000
        count = 0
        tree = [text]
        while count < max_count:
            for rule in self.P:
                key = rule.Key
                value = rule.Value
                pos = text.rfind(value)
                if pos != -1:
                    text = text[:pos] + key + text[pos + len(value):]
                    separator = "|"
                    for _ in range(pos):
                        separator = " " + separator
                    tree.append(separator)
                    tree.append(text)
            count += 1
        tree.reverse()
        for branch in tree:
            print(branch)
        return text

if __name__ == "__main__":
    import sys
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

    print("Задание 11.")
    print("Подпункт а)")
    print("Грамматика описывает язык 0^n 1^n 'Символ перепендикуляра' |")
    dict_rules = [
        Rule("S", "0S"),
        Rule("S", "0B"),
        Rule("B", "1B"),
        Rule("B", "1C"),
        Rule("C", "1C"),
        Rule("C", "|"),
    ]
    fl = FormalLanguage(dict_rules)
    print("Праволинейный:")
    print_rules(dict_rules)
    print(fl.output_left())

    dict_rules = [
        Rule("S", "A|"),
        Rule("A", "A1"),
        Rule("A", "CB1"),
        Rule("B", "B1"),
        Rule("B", "C1"),
        Rule("B", "CB1"),
        Rule("C", "0"),
    ]
    fl = FormalLanguage(dict_rules)
    print("Леволинейный:")
    print_rules(dict_rules)
    print(fl.output_left())
    print("Подпункт б)")
    print("Грамматика описывает язык {a^n b^n} 'Символ перепендикуляра' |")
    dict_rules = [
        Rule("S", "aA"),
        Rule("S", "aB"),
        Rule("S", "bA"),
        Rule("A", "bS"),
        Rule("B", "aS"),
        Rule("B", "bB"),
        Rule("B", "|"),
    ]
    fl = FormalLanguage(dict_rules)
    print("Праволинейный:")
    print_rules(dict_rules)
    root = fl.build_tree(fl.output_left())
    print_tree(root)

    dict_rules = [
        Rule("S", "A|"),
        Rule("A", "Ba"),
        Rule("A", "Bb"),
        Rule("A", "Ab"),
        Rule("A", "ABa"),
        Rule("A", "ABb"),
        Rule("B", "a"),
        Rule("B", "b"),
    ]
    fl = FormalLanguage(dict_rules)
    print("Леволинейный:")
    print_rules(dict_rules)
    root = fl.build_tree(fl.output_left())
    print_tree(root)
    print()

    print("Задание 12.")
    dict_rules = [
        Rule("S", "S1"),
        Rule("S", "A0"),
        Rule("A", "A1"),
        Rule("A", "0"),
    ]
    fl = FormalLanguage(dict_rules)
    print(fl.output_left())

    dict_rules = [
        Rule("S", "A1"),
        Rule("S", "B0"),
        Rule("S", "E1"),
        Rule("A", "S1"),
        Rule("B", "C1"),
        Rule("B", "D1"),
        Rule("C", "0"),
        Rule("D", "B1"),
        Rule("E", "E0"),
        Rule("E", "1"),
    ]
    fl = FormalLanguage(dict_rules)
    print(fl.output_left())