import tkinter as tk
from tkinter import filedialog
import traceback

 
from analyzers.Lexer import Lexer
from analyzers.CParser import CParser
from tokens.tkIDs import tkIDsList
from tokens.CRegEx import CRegExList
from tokens.PyRegEx import PyRegExList
from preprocessors.tokens_preprocessing import c_tokens_preprocessing

class CodeTranslatorApp:
    def __init__(self, win):
        self.win = win
        win.title("Code Translator")
        win.geometry('1680x720+0+0') #?х? - размер окна, +?+? отступ от левой верхней точки
        win.config(bg='#100d23')    #цвет фона

        lable_input = tk.Label(win, text='Введите ваш код на C++:', 
                                bg='#100d23',
                                fg='#0aefc8',
                                font=('Consolas')
                                ).grid(row=0, column=0)

        lable_output = tk.Label(win, text='Python:', 
                                bg='#100d23',
                                fg='#0aefc8',
                                font=('Consolas')
                                ).grid(row=0, column=2)


        self.input_text = tk.Text(win, 
                width=79, 
                height=41,
                bg='#161329',
                fg='#0aefc8',
                insertbackground='#0aefc8',
                insertwidth=4)
        self.input_text.grid(row=1, column=0)

      
        self.translate_button =tk.Button(win, text='Перевести',
                        fg='#100d23',
                        bg='#0aefc8',
                        font=('Consolas'),
                        activebackground='#c592ff',
                        command=self.translate_code
                        ).grid(row=0, column=1)

        self.output_text = tk.Text(win, 
                width=78, 
                height=41,
                bg='#161329',
                fg='#0aefc8',
                insertbackground='#161329',)
        self.output_text.grid(row=1, column=2)


        # Добавим переменную для хранения текущей рамки
        self.error_frame = None

    def translate_code(self):
        code = self.input_text.get("1.0", tk.END)

        if code.startswith("#include"):
            lexer = Lexer(zip(tkIDsList, CRegExList))   # cоздаетcя лексический анализатор на основе списка токенов tkIDsList и регулярных выражений CRegExList
            parser = CParser(tkIDsList)                 # cоздаетcя парсер на основе токенов tkIDsList
            parser.parse()                              # задается грамматические правила для парсера
            parser = parser.pg.build()                  # собирается парсер после определения всех правил
            code = code[code.find('{') + 1:code.rfind('}')]     # отбрасывает все, что находится до и после фигурных скобок   
            tokens = c_tokens_preprocessing(lexer(code))        # применяет лексер к тексту, чтобы получить поток токенов

            try:
                result = parser.parse(iter(tokens))     # преобразует токены в итерируемый объект и передает их в парсер, чтобы получить результат
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END,  result)

            except Exception as e:
                error_info = f"Error: {e}\n"
                self.output_text.delete("1.0", tk.END)
                self.insert_colored_line(error_info, 1)
        else:
            self.output_text.insert(tk.END, 'Программа на C++ должна начинаться с #include <iostream>')            

    def insert_colored_line(self, line_text, line_number, color="red"):
        # Создаем тег с определенным цветом
        self.output_text.tag_config(f"color_{line_number}", foreground=color)

        # Определяем место вставки
        insert_position = f"{line_number}.0"

        # Вставляем строку
        self.output_text.insert(insert_position, line_text + "\n")

        # Применяем тег к вставленной строке
        self.output_text.tag_add(f"color_{line_number}", insert_position, f"{line_number + 1}.0")


if __name__ == '__main__':
    root = tk.Tk()
    app = CodeTranslatorApp(root)
    root.mainloop()