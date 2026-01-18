1, for list below:
```
items = ['pen', 'pencil', 'eraser', 'ink']
```
1.0, How to get the number of items in items?

```
>>> print(len(items))
4
```

1.1, How to change 'pencil' to 'canyon'?

```
>>> items = ['pen', 'pencil', 'eraser', 'ink']
>>> items[1]
'pencil'

```

1.2, How to get only the first 2 elements (i.e. ```['pen', 'pencil']```) from items?

```

>>> print(items[0:2])
['pen', 'pencil']

```

1.3, How to get the last value "ink" from the list? use 2 methods.

```

>>> print(items[3])
ink

>>> print(items[-1])
ink

```

1.4, how to append a value 'paper' to items?

```
>>> items.insert(4, "paper")
>>> items
['pen', 'pencil', 'eraser', 'ink', 'paper']

```

===================


2, for dict below:
```
prices = {
    "apple": 2,
    "banana": 1,
    "orange": 3
}
```
2.1, how to get the price of "orange"?

```

>>> print(prices["orange"])
3
```

2.2, How to enumerate the prices of all fruits, and print each in format "fruitname - $price", for example, "apple - $2". (can not hardcode fruit name in the code)
```

>>> for fruit, price in prices.items():
...     print(f"{fruit} - ${price}")
...
apple - $2
banana - $1
orange - $3

```
2.3, how to get price of "orange"?
```

>>> orange_price = prices["orange"]
... print(orange_price)
...
3

```
2.4, how to add a fruit "grape" ($5) to the dict?
```

>>> prices["grape"] = 5
>>>
>>> print(prices["orange"])
3

```
2.5, How to get the size of the dict?
```

>>> size = len(prices)
... print(size)
...
4

```
========================


1,  How to get the value 8?
```
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

>>> print(x[2][0])
7

```


2, How to get the value 30?

```
data = [10, [20, 30], 40]
```

```
>>> data = [10, [20, 30], 40]
>>> data[1][1]
30
```



3, How to get the email "emma@test.com"?
```
user = {
    "id": 101,
    "profile": {
        "name": "Emma",
        "email": "emma@test.com"
    }
}
```


```
... user["profile"]["email"]
'emma@test.com'
>>>

```


4.1), How to get the student "Lucy"?

```
classroom = {
    "teacher": "Mr Smith",
    "students": ["Tom", "Lucy", "Jack"]
}
```
```

>>> student = classroom["students"][1]
>>>
>>> print(student)
Lucy

```

4.2), how to change the value "Lucy" to "Lucy123"?

```

>>> user[1] = "Lucy123"
>>> print(student)
Lucy
```

5, How to get the number of pages of "Science"?
```
books = [
    {"title": "Math", "pages": 120},
    {"title": "Science", "pages": 200},
    {"title": "History", "pages": 150}
]
```

```
>>> books = [
...     {"title": "Math", "pages": 120},
...     {"title": "Science", "pages": 200},
...     {"title": "History", "pages": 150}
... ]
>>> print(books[1]["pages"])
200
```

6, How to change the score 80 to 82?
```
student = {
    "name": "Liam",
    "scores": [75, 80, 85]
}
```


```
>>> score = student["scores"][1]
>>> student["scores"][1] = 82
>>> print(student)
{'name': 'Liam', 'scores': [75, 82, 85]}
>>>

```

7, How to add "Charlie" to the members list?
```
team = {
    "name": "Red",
    "members": ["Alice", "Bob"]
}
```

```
>>> team = {
...     "name": "Red",
...     "members": ["Alice", "Bob"]
... }
>>>
>>> team["members"].append("Charlie")
```


8, How to get the value "yellow" using a negative index?
```
colors = [
    ["red", "green"],
    ["blue", "yellow"]
]
```


```
>>> colors = [
...     ["red", "green"],
...     ["blue", "yellow"]
... ]
>>> print(colors[-1][-1])
yellow

```



9, How to get the size of Class B?
```
school = {
    "classes": [
        {"name": "Class A", "size": 25},
        {"name": "Class B", "size": 28}
    ]
}

```

```
>>> class_b_size = school["classes"][1]["size"]
... print(class_b_size)
...
28
```


10, How to add a new key "color" with value "blue"?
```
car = {
    "brand": "Toyota",
    "year": 2020
}
```

```
>>> car["color"] = "blue"
... print(car)
...
{'brand': 'Toyota', 'year': 2020, 'color': 'blue'}
>>>
```


11, How to print all books one by one in formats like "Math - 120 pages"?
```
books = [
    {"title": "Math", "pages": 120},
    {"title": "Science", "pages": 200},
    {"title": "History", "pages": 150}
]
```


```
>>> for book in books:
...     print(f"{book['title']} - {book['pages']} pages")
...
Math - 120 pages
Science - 200 pages
History - 150 pages

`` 
