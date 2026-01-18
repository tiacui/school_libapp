String
====================

1) add numbers
```
aaa = "123"
bbb = "222"
```
Task: add a few lines to the bottom of the code above, to add "aaa" and "bbb", and print the result, which should be "345" 



```
>>> aaa = "123"
... bbb = "222"
...
>>> result = int(aaa) + int(bbb)
>>>
>>> print(result)
345
```

2) concatenate number and string
```
aaa = 'hello'
bbb = 123
```
Task: add a few lines to the bottom of the code above, to concatenate "aaa" and "bbb", and print the result, which should be "hello123" 


```
>>> result = aaa + str(bbb)
>>> print(result)
123222
```
3) change to upper case
```
aaa = 'hello123'
```
Task: add a few lines to the bottom of the code above, to change aaa to upper case

```
>>> aaa = 'hello123'
>>> result = aaa.upper()
>>> print(result)
HELLO123
```
4) change to upper case
```
aaa = 'hello123'
```
Task: add a few lines to the bottom of the code above, to obtain the first 6 charactors of "aaa", which should be "hello1"


```
>>> result = aaa[:6]
>>> print(result)
hello1
```
Inheritance
====================
Purpose: Code reuse


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
The purpose of polymorphism in coding is to allow a single interface (like a method name) to represent different underlying actions or data types, enabling flexible, reusable, and maintainable code by treating diverse objects uniformly, reducing duplicate code, and simplifying complex logic, often through inheritance. It lets you write generic code that works with many object types, making your programs more scalable and easier to debug. 


Example Analogy:

Think of a "draw" command in a drawing application. You can tell any shape (Circle, Triangle, Square) to draw(), and each shape knows how to draw itself correctly, even though you use the same command for all of them. 

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

Encapsulation = hide how something works, expose only how to use it

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

Example:

The following will cause issues:
```
class BankAccount:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        print(f'your balance is: {self.balance}')

acc = BankAccount()
acc.balance = -1000   # invalid but allowed
acc.get_balance()
```

the right way:

```
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.__balance += amount
 
    def get_balance(self):
        print(f'your balance is: {self.balance}')


acc = BankAccount()
acc.deposit(-1000)
acc.get_balance()
```



