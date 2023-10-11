class Rule:
    def __init__(self, k, v, l=False):
        self.Key = k
        self.Value = v
        self.IsLooped = l

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

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


if __name__ == "__main__":
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