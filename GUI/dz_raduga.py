from tkinter import *

root = Tk()
root.geometry('30x200+400+200')

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

# Variant_1 - #
# def color_red():
#     l['text'] = 'Красный'
#     e.delete(0, END)
#     e.insert(0, '#ff0000')
#
#
# def color_orange():
#     l['text'] = 'Оранжевый'
#     e.delete(0, END)
#     e.insert(0, '#ff7d00')
#
#
# def color_yellow():
#     l['text'] = 'Желтый'
#     e.delete(0, END)
#     e.insert(0, '#ffff00')
#
#
# def color_green():
#     l['text'] = 'Зеленый'
#     e.delete(0, END)
#     e.insert(0, '#00ff00')
#
#
# def color_blue():
#     l['text'] = 'Голубой'
#     e.delete(0, END)
#     e.insert(0, '#007dff')
#
#
# def color_dark_blue():
#     l['text'] = 'Синий'
#     e.delete(0, END)
#     e.insert(0, '#0000ff')
#
#
# def color_violet():
#     l['text'] = 'Фиолетовый'
#     e.delete(0, END)
#     e.insert(0, '#7d00ff')
#
#
# l = Label(root)
# e = Entry(root, width=30, justify='center')
# l.pack()
# e.pack()
#
# btn_red = Button(root, bg='#ff0000', command=color_red).pack(fill=X)
# btn_orange = Button(root, bg='#ff7d00', command=color_orange).pack(fill=X)
# btn_yellow = Button(root, bg='#ffff00', command=color_yellow).pack(fill=X)
# btn_green = Button(root, bg='#00ff00', command=color_green).pack(fill=X)
# btn_blue = Button(root, bg='#007dff', command=color_blue).pack(fill=X)
# btn_dark_blue = Button(root, bg='#0000ff', command=color_dark_blue).pack(fill=X)
# btn_violet = Button(root, bg='#7d00ff', command=color_violet).pack(fill=X)

# Variant_2 - #


# def get_color_txt_hex(txt, hex):
#     l['text'] = txt
#     e.delete(0, END)
#     e.insert(0, hex)
#
#
# l = Label(root)
# e = Entry(root, width=30, justify='center')
# l.pack()
# e.pack()
#
# btn_red = Button(root, bg='#ff0000', command=lambda: get_color_txt_hex('Красный', '#ff0000')).pack(fill=X)
# btn_orange = Button(root, bg='#ff7d00', command=lambda: get_color_txt_hex('Оранжевый', '#ff7d00')).pack(fill=X)
# btn_yellow = Button(root, bg='#ffff00', command=lambda: get_color_txt_hex('Желтый', '#ffff00')).pack(fill=X)
# btn_green = Button(root, bg='#00ff00', command=lambda: get_color_txt_hex('Зелёный', '#00ff00')).pack(fill=X)
# btn_blue = Button(root, bg='#007dff', command=lambda: get_color_txt_hex('Голубой', '#007dff')).pack(fill=X)
# btn_dark_blue = Button(root, bg='#0000ff', command=lambda: get_color_txt_hex('Синий', '#0000ff')).pack(fill=X)
# btn_violet = Button(root, bg='#7d00ff', command=lambda: get_color_txt_hex('Фиолетовый', '#7d00ff')).pack(fill=X)

# Variant_3 - #

# def get_color_txt_hex(txt, hx):
#     l['text'] = txt
#     e.delete(0, END)
#     e.insert(0, hx)
#
#
# l = Label(root)
# e = Entry(root, width=30, justify='center')
# l.pack()
# e.pack()
#
# colors = {
#     "#ff0000": 'Красный',
#     "#ff7d00": 'Оранжевый',
#     "#ffff00": 'Желтый',
#     "#00ff00": 'Зеленый',
#     "#007dff": 'Голубой',
#     "#0000ff": 'Синий',
#     "#7d00ff": 'Фиолетовый',
# }
#
# for k, v in colors.items():
#     Button(root, bg=k, command=lambda txt=k, hx=v: get_color_txt_hex(txt, hx)).pack(fill=X)

# Variant_4 - OOP

colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

for k, v in colors.items():
    MyButtons(root, v, k)


root.mainloop()
