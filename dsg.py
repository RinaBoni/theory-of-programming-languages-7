import random

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Rule:
    def __init__(self, key, value, isCycled):
        self.key = key
        self.value = value
        self.isCycled = isCycled

    # def __init__(self, key, value):
    #     self.key = key
    #     self.value = value
    #     self.isCycled = False
        
class Language:
    def __init__(self, rules):
        self.rules = rules

    def setRules(self, rules):
        self.rules = rules

    def getRules(self):
        str = ""
        for rule in self.rules:
            str += rule.key + "-->" + rule.value + "\n"
        return str

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
                            print(str + "\n" + self.rules[j].key + "-->" + self.rules[j].value)
                            return newWord
        return newWord

    def findGrammar(self, max=30, word="S", n=0):  # Добавляем self как параметр
        new_word = word
        for i in range(len(word)):
            term_character = ""
            for j in range(i, len(word)):
                term_character += word[j]
                for rule in self.rules:  # Используем self.rules
                    if rule.key == term_character and n < max:
                        new_word = word[:i] + rule.value + word[i + len(term_character):]
                        n += 1
                        new_word = self.findGrammar(max, new_word, n)  # Используем self.findGrammar
                        c = 0
                        if n == max - 1:
                            for rule2 in self.rules:  # Используем self.rules
                                if rule2.key in new_word:
                                    c += 1
                            if c == 0:
                                return new_word
        return new_word

    
    def findLanguage(self):  # Добавляем self
        str1 = self.findGrammar(10)  # Не передаем rules явно, используем self.rules
        str2 = self.findGrammar(20)  # Не передаем rules явно, используем self.rules
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


    def check_loop(input, rule, count=5):
        for i in range(count):
            key = rule.key
            value = rule.value

            pos = input.find(key)

            if pos != -1:
                input = input[:pos] + value + input[pos+len(key):]
            else:
                return False

        return True


    def generate_grammar2(self):
        str = self.findGrammar()
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

    print('a) ', language.getRules())
    language.findLanguage()
    print()

    print('b) ', language1.getRules())
    language1.findLanguage()
    print('\n\n')
        
        
    
def main():
    print('\nЗадание один:')
    task_one()
    print('\nЗадание два:')
    task_two()

    

if __name__ == "__main__":
	main()