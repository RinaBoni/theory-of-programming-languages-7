import tkinter as tk
import Lexer
from SyntaxAnalyzer import SyntaxAnalyzer
from pynput import keyboard

# def convert():
#     output_str_lex.replace('1.0', tk.END, "")
#     output_s = Lexer.output(input_str.get('1.0', tk.END))
#     errors=[]

#     for item in output_s:
#         output_str_lex.insert(tk.END, str(item) + '\n'+ '\n')

#         result = SyntaxAnalyzer.statement(item)
#         index = [it['index'] for it in item]
#         value = [it['token_value'] for it in item]
#         if result != SyntaxAnalyzer.errors['OK']:
#             err = {'index': index, 'value': value, 'error type': result}
#             errors.append(err)

#         output_str_syn.insert(tk.END, str(err) + '\n'+ '\n')

# def on_press(key):
#     convert()


def convert():
    input_s = input_str.get('1.0', tk.END)
    output_s = Lexer.output(input_s)
    syntax_analyzer_instance = SyntaxAnalyzer()

    for item in output_s:
        output_str_lex.insert(tk.END, str(item) + '\n'+ '\n')
        
    result = syntax_analyzer_instance.statement(output_s)
    print('\n\n\n')
    print(result)
    print('\n\n\n')
    for item in output_s:
        index = item['index']
        value = item['token_value']
        # if result != syntax_analyzer_instance.errors['OK']:
        err = {'index': index, 'value': value, 'error type': result}

        output_str_syn.insert(tk.END, str(err) + '\n'+ '\n')




win = tk.Tk()   #создаем окно

win.title('Лексический анализатор')
win.geometry('1650x520+100+100') #?х? - размер окна, +?+? отступ от левой верхней точки
win.config(bg='#100d23')    #цвет фона

lable_input = tk.Label(win, text='Введите ваш код:', 
                                bg='#100d23',
                                fg='#0aefc8',
                                font=('Consolas')
                                ).grid(row=0, column=0)

lable_output_lex = tk.Label(win, text='Лексический анализатор:', 
                                bg='#100d23',
                                fg='#0aefc8',
                                font=('Consolas')
                                ).grid(row=0, column=2)

lable_output_syn = tk.Label(win, text='Синтаксический анализатор:', 
                                bg='#100d23',
                                fg='#0aefc8',
                                font=('Consolas')
                                ).grid(row=0, column=3)

btn_convert = tk.Button(win, text='Обработать',
                        fg='#100d23',
                        bg='#0aefc8',
                        font=('Consolas'),
                        activebackground='#c592ff',
                        command=convert
                        ).grid(row=0, column=1)

input_str = tk.Text(win, 
                width=35, 
                height=28,
                bg='#161329',
                fg='#0aefc8',)
input_str.grid(row=1, column=0)


output_str_lex = tk.Text(win, 
                width=63, 
                height=28,
                bg='#161329',
                fg='#0aefc8',)
output_str_lex.grid(row=1, column=2)

output_str_syn = tk.Text(win, 
                width=75, 
                height=28,
                bg='#161329',
                fg='#0aefc8',)
output_str_syn.grid(row=1, column=3)



win.grid_columnconfigure(0, minsize=225)
win.grid_columnconfigure(1, minsize=0)
win.grid_columnconfigure(2, minsize=300)
win.grid_columnconfigure(3, minsize=300)

# with keyboard.Listener(
#         on_press=on_press) as listener:
#     win.mainloop()  #запускаем 
#     listener.join()


win.mainloop()  #запускаем окно