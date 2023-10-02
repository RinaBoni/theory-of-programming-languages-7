import random

class Rule:
    def __init__(self, key, value, isCycled):
        self.key = key
        self.value = value
        self.isCycled = isCycled

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.isCycled = False
        
class Language:
    def __init__(self, rules):
        self.rules = rules

    def setRules(self, rules):
        self.rules = rules

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



def task_one():
    rules = [
        Rule("S", "T"),
        Rule("S", "T+S"),
        Rule("S", "T-S"),
        Rule("T", "F*T"),
        Rule("T", "F"),
        Rule("F", "a"),
        Rule("F", "b")
    ]
    language = Language(rules)

    rules1 = [
        Rule("S", "aSBC"),
        Rule("S", "abC"),
        Rule("bB", "bb"),
        Rule("CB", "BC"),
        Rule("bC", "bc"),
        Rule("cC", "cc")
    ]
    language1 = Language(rules1)

    word = "a-b*a+b"
    word2 = "aaabbbccc"

    print("Цепочка создания слова: " + word)
    language.findChain(word)
    print(word)

    print("Цепочка создания слова: " + word2)
    language1.findChain(word2)
    print(word2)
    
def task_two():
    rules = [
    Rule("S", "aaCFD"),
    Rule("AD", "D"),
    Rule("F", "AFB"),
    Rule("F", "AB"),
    Rule("Cb", "bC"),
    Rule("AB", "bBA"),
    Rule("CB", "C"),
    Rule("Ab", "bA"),
    Rule("bCD", "")
    ]

    # Создаем объект класса Language с заданными правилами
    language = Language(rules)

    # Попробуем различные входные слова
    word1 = "aaCFD"
    word2 = "bCAb"
    word3 = "bCDD"

    # Вызываем метод findChain для каждого слова
    result1 = language.findChain(word1)
    result2 = language.findChain(word2)
    result3 = language.findChain(word3)

    # Проверяем результаты
    if result1 == "S":
        print("Язык порождается грамматикой.")
    else:
        print("Язык не порождается грамматикой.")

    if result2 == "S":
        print("Язык порождается грамматикой.")
    else:
        print("Язык не порождается грамматикой.")

    if result3 == "S":
        print("Язык порождается грамматикой.")
    else:
        print("Язык не порождается грамматикой.")
        
        
def t_t():
    def generate_string():
        # Начинаем с символа S
        string = "S"

        while True:
            new_string = ""
            i = 0
            while i < len(string):
                char = string[i]
                print(char)

                if char == "S":
                    new_string += "aaCFD"
                elif char == "A":
                    # Добавляем символ D с вероятностью 1/3
                    if random.random() < 1/3:
                        new_string += "D"
                    i += 1
                elif char == "D":
                    pass
                elif char == "F":
                    # Выбираем случайное правило AFB или AB с равной вероятностью
                    if random.random() < 0.5:
                        new_string += "AFB"
                    else:
                        new_string += "AB"
                    i += 1
                elif char == "C":
                    # Пропускаем символ Cb
                    i += 1
                elif char == "b":
                    # Добавляем символ Cb с вероятностью 1/2
                    if random.random() < 0.5:
                        new_string += "Cb"
                    i += 1
                elif char == "A":
                    # Добавляем символ bBA
                    new_string += "bBA"
                    i += 1
                elif char == "B":
                    # Пропускаем символ bBA
                    i += 1
                elif char == "C":
                    # Пропускаем символ CB
                    i += 1
                elif char == "b":
                    # Пропускаем символ bCD
                    i += 1
                elif char == "D":
                    # Пропускаем символ bCD
                    i += 1
                else:
                    # Достигли конца строки, завершаем генерацию
                    return new_string

            string = new_string

    # Генерируем и выводим строку
    generated_string = generate_string()
    print(generated_string)
        
def main():
    print('\nTASK ONE')
    task_one()
    print('\n\nTASK TWO')
    # task_two()
    t_t()

    

if __name__ == "__main__":
	main()