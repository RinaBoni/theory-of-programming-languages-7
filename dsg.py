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