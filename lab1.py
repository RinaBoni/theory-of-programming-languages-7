class Rules():
    def __init__(self, key, value, is_looped):
        self.key = key
        self.value = value
        self.is_looped = is_looped
        
    def rule(self , k, v, l):
        self.key = k
        self.value = v
        self.is_looped = l
        

    def print_rules(rules):
        for i in len(rules):
            print()
        