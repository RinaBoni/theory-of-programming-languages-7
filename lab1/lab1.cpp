// lab1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <string>
#include <list>
using namespace std;

class Rule {
public: string key;
      string value;
      bool isCycled;

      void rule(string key, string value, bool isCycled)
      {
          this->key = key;
          this->value = value;
          this->isCycled = isCycled;
      }
      void rule(string key, string value)
      {
          this->key = key;
          this->value = value;
          this->isCycled = false;
      }
};


class Language
{
private: list<Rule> rules;
public:
    void setRules(list<Rule> rules)
    {
        this->rules = rules;
    }
    void language(list<Rule> rules)
    {
        this->rules = rules;
    }

    string findChain(string word)
    {
        string newWord = word;
        for (int k = 1; k <= word.size(); k++)
        {
            string termCharacter = "";
            for (int i = word.size() - k; i >= 0; i--)
            {
                termCharacter = termCharacter.insert (0, string(1, word[i]));
                for (int j = 0; j < rules.size(); j++)
                {
                    if (rules[j].value.Equals(termCharacter))
                    {
                        newWord = word.erase(i, termCharacter.size());
                        newWord = newWord.insert (i, rules[j].key);
                        string str = newWord;
                        newWord = findChain(newWord);
                        if (newWord == "S")
                        {
                            cout << (str + "\n" + rules[j].key + "-->" + rules[j].value);
                            return newWord;
                        }
                    }
                }
            }
        }
        return newWord;
    }
};

int main()
{
    std::cout << "Hello World!\n";
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
