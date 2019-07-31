class Person:
    def sayHi(self):
        print('Привет! Как дела?')
    def sayShalom(self):
        print('SHALOM!')

p = Person()
p.sayHi()
s = Person()
s.sayShalom()
# Этот короткий пример можно также записать как Person().sayHi()
