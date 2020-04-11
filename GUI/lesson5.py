from tkinter import *

root = Tk()
root.geometry('600x400+400+200')


def add_str():
    e.insert(END, 'Hello!')


def del_str():
    e.delete(0, END)


def get_str():
    l_text['text'] = e.get()


l = Label(root, text="Поле ввода")
l.pack()

e = Entry(root)
# e.insert(0, 'Hello')
# e.insert(END, ' world')
e.pack()

btn_add = Button(root, text="Add", command=add_str).pack()
btn_del = Button(root, text="Delete", command=del_str).pack()
btn_get = Button(root, text="Get", command=get_str).pack()

l_text = Label(root, bg='blue', fg='white')
l_text.pack(fill=X)


root.mainloop()

'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''