import random

class Rule:
    def __init__(self, key, value, is_looped=False):
        self.Key = key  # Порождающая цепочка языка
        self.Value = value  # Порождаемая цепочка языка
        self.IsLooped = is_looped  # Введет ли правило зацикливанию

    def __str__(self):
        return f"Rule(Key='{self.Key}', Value='{self.Value}', IsLooped={self.IsLooped})"

def print_rules(rules):
    print("Правила для языка")
    for rule in rules:
        print(f"   \u2022 {rule.Key} --> {rule.Value}")

class FormalLanguage:
    def __init__(self, rules, max_repetitions_count=10000):
        self._rules = rules
        self.MaxRepetitionsCount = max_repetitions_count

    def check_loop(input_str, rule, count=5):
        for i in range(count):
            key = rule.Key
            value = rule.Value

            pos = input_str.find(key)

            if pos != -1:
                input_str = input_str[:pos] + value + input_str[pos + len(key):]
            else:
                return False

        return True

    import random

    def output_left(self):
        result = "S"
        count = 0
        while count < self.MaxRepetitionsCount:
            pos = -1

            # Найдем крайний левый нетерминальный символ в цепочке
            for rule in self._rules:
                key = rule.Key
                find_pos = result.find(key)
                if (pos > find_pos or pos == -1) and find_pos != -1:
                    pos = find_pos

            # Если не найдено ни одного подходящего правила - выходим
            if pos == -1:
                break

            # Найдем все правила, подходящие для крайнего левого нетерминального символа
            matching_rules = [rule for rule in self._rules if pos == result.find(rule.Key)]

            if matching_rules:
                # Случайно выберем правило
                selected_rule = random.choice(matching_rules)

                p = result.find(selected_rule.Key)
                result = result[:p] + selected_rule.Value + result[p + len(selected_rule.Key):]

            count += 1

        return result

    def translate(self, text):
        count = 0
        is_end = False  # True - если ни одно из правил неприменимо
        while count < self.MaxRepetitionsCount:
            if is_end:
                break

            count += 1
            is_end = True
            # Применяем по очереди каждое правило языка к строке
            for rule in self._rules:
                if not rule.IsLooped:  # Если правило не зацикливает
                    key = rule.Key
                    value = rule.Value

                    pos = text.find(key)

                    if pos != -1:  # Если ключ найден
                        # Если правило зацикливает перевод - запоминаем это
                        if not self.check_loop(text, rule):
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
    def __init__(self, nonterminal, terminal, rules, s="S"):
        self.Nonterminal = nonterminal
        self.Terminal = terminal
        self.P = rules
        self.S = s

    def get_type_grammar(self):
        is_type_one = True
        is_type_two = True
        is_type_three = True

        is_each_term_pos_bigger = True
        is_each_term_pos_smaller = True

        for r in self.P:
            # Проверка принадлежности первому типу грамматики
            is_type_one &= len(r.Key) <= len(r.Value)

            # Проверка принадлежности второму типу
            for vt in self.Terminal:
                is_type_two &= vt not in r.Key

            if is_each_term_pos_bigger or is_each_term_pos_smaller:
                terminal_positions = []
                non_terminal_positions = []

                for vn in self.Nonterminal:
                    temp = r.Value.find(vn)
                    if temp != -1:
                        non_terminal_positions.append(temp)

                for vt in self.Terminal:
                    temp = r.Value.find(vt)
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

        return res

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
                    for i in range(pos):
                        separator = " " + separator

                    tree.append(separator)
                    tree.append(text)
            count += 1

        tree.reverse()

        for branch in tree:
            print(branch)

        return text


if __name__ == "__main__":
    dict = []
    fl = FormalLanguage(dict)

    print("Задание 11.")
    print("Подпункт а)")
    print("Грамматика описывает язык 0^n 1^n 'Символ перепендикуляра' |")

    dict = [
        Rule("S", "0S"),
        Rule("S", "0B"),
        Rule("B", "1B"),
        Rule("B", "1C"),
        Rule("C", "1C"),
        Rule("C", "|"),
    ]

    fl = FormalLanguage(dict)
    print("Праволинейный:")
    print_rules(dict)
    print("01|")

    print("\n\nРеализация дерева")
    print("S\n|\n|\nB---|\n|   |\n|   |\n|   C---|\n|   |   |\n|   |   |\n0   1   \\\n")
    print("\n\n")

    dict = [
        Rule("S", "A|"),
        Rule("A", "A1"),
        Rule("A", "CB1"),
        Rule("B", "B1"),
        Rule("B", "C1"),
        Rule("B", "CB1"),
        Rule("C", "0"),
    ]
    fl = FormalLanguage(dict)
    print("Леволинейный:")
    print_rules(dict)

    print(fl.output_left())
    print("Подпункт б)")
    print("Грамматика описывает язык {a^n b^n} 'Символ перепендикуляра' |")

    dict = [
        Rule("S", "aA"),
        Rule("S", "aB"),
        Rule("S", "bA"),
        Rule("A", "bS"),
        Rule("B", "aS"),
        Rule("B", "bB"),
        Rule("B", "|"),
    ]
    fl = FormalLanguage(dict)
    print("Праволинейный:")
    print_rules(dict)

    print(fl.output_left())

    dict = [
        Rule("S", "A|"),
        Rule("A", "Ba"),
        Rule("A", "Bb"),
        Rule("A", "Ab"),
        Rule("A", "ABa"),
        Rule("A", "ABb"),
        Rule("B", "a"),
        Rule("B", "b"),
    ]
    fl = FormalLanguage(dict)
    print("Леволинейный:")
    print_rules(dict)

    print(fl.output_left())

    print("Задание 12.")
    dict = [
        Rule("S", "S1"),
        Rule("S", "A0"),
        Rule("A", "A1"),
        Rule("A", "0"),
    ]
    fl = FormalLanguage(dict)
    print("Грамматика G1")
    print_rules(dict)

    print(fl.output_left())

    dict = [
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
    fl = FormalLanguage(dict)
    print("Грамматика G2")
    print_rules(dict)

    print(fl.output_left())

    dict = [
        Rule("S", "S1"),
        Rule("S", "A0"),
        Rule("S", "A1"),
        Rule("A", "0"),
    ]
    fl = FormalLanguage(dict)
    print("Грамматика L1∩L2")
    print_rules(dict)

    print(fl.output_left())