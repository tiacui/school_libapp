
Inheritance
====================

```
class Animal:
    def eat(self):
        print("eat food")

class Dog(Animal):
    def bark(self):
        print("wang")


d = Dog()
d.eat()    # from "Animal"
d.bark()   # from "Dog"
```


Polymorphism
===================

```
class Dog:
    def speak(self):
        print("wang")

class Cat:
    def speak(self):
        print("meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())
```

Encapsulation
=================

```
class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())

```
try ```print(acc.__balance)``` instead of ```print(acc.get_balance())``` and see what happens.

