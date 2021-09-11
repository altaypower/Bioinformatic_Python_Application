"""
1.
Какие числа будут выведены в результате выполнения данного кода?
class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)

ответ:
10, 30
2.
Что будет выведено в результате выполнения данного кода?
class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()

Ответ:
С

2.
Рассмотрим следующее объявление классов
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass


Какие последовательности могут являться корректным порядком разрешения методов для класса E?

Ответ:
Никакие из перечисленных
"""