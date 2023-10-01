using System;
using System.Collections.Generic;
using System.IO;

namespace Lab_1
{
    class Program
    {
        class Rule
        {
            public String key;
            public String value;
            public bool isCycled;
            public Rule(String key, String value, bool isCycled)
            {
                this.key = key;
                this.value = value;
                this.isCycled = isCycled;
            }
            public Rule(String key, String value)
            {
                this.key = key;
                this.value = value;
                this.isCycled = false;
            }
        }
        class Language
        {
            private List<Rule> rules;
            public void setRules(List<Rule> rules)
            {
                this.rules = rules;
            }
            public Language(List<Rule> rules)
            {
                this.rules = rules;
            }

            public String findChain(string word)
            {
                string newWord = word;
                for (int k = 1; k <= word.Length; k++)
                {
                    string termCharacter = "";
                    for (int i = word.Length - k; i >= 0; i--)
                    {
                        termCharacter = termCharacter.Insert(0, word[i].ToString());
                        for (int j = 0; j < rules.Count; j++)
                        {
                            if (rules[j].value.Equals(termCharacter))
                            {
                                newWord = word.Remove(i, termCharacter.Length);
                                newWord = newWord.Insert(i, rules[j].key);
                                string str = newWord;
                                newWord = findChain(newWord);
                                if (newWord == "S")
                                {
                                    System.Console.WriteLine(str + "\n" + rules[j].key + "-->" + rules[j].value);

                                    return newWord;
                                }
                            }
                        }
                    }
                }
                return newWord;
            }
        }
        static void Main(string[] args)
        {
            List<Rule> rules = new List<Rule>
            {
                new Rule("S", "T"),
                new Rule("S", "T+S"),
                new Rule("S", "T-S"),
                new Rule("T", "F*T"),
                new Rule("T", "F"),
                new Rule("F", "a"),
                new Rule("F", "b")
            };
            Language language = new Language(rules);
            List<Rule> rules1 = new List<Rule>
            {
                new Rule("S", "aSBC"),
                new Rule("S", "abC"),
                new Rule("bB", "bb"),
                new Rule("CB", "BC"),
                new Rule("bC", "bc"),
                new Rule("cC", "cc")
            };
            Language language1 = new Language(rules1);


            /*string filePath1 = "chain1.txt";
            string word = File.ReadAllText(filePath1);

            string filePath2 = "chain2.txt";
            string word2 = File.ReadAllText(filePath2);*/


            string word = "a-b*a+b";
            string word2 = "aaabbbccc";
            Console.WriteLine("Цепочка создания слова: " + word);
            language.findChain(word);
            Console.WriteLine(word);
            Console.WriteLine("Цепочка создания слова: " + word2);
            language1.findChain(word2);
            Console.WriteLine(word2);
            Console.ReadLine();
        }
    }
}
