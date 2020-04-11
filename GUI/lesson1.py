# https://www.tutorialspoint.com/python3/python_gui_programming.htm

from tkinter import *

root = Tk()
root.title('Мое первое GUI приложение')
root.iconbitmap('python.ico')
root.geometry('600x400+400+200')
root.resizable(True, True)
root.config(bg='#156')
# root['bg'] = 'red'

root.mainloop()
