# Python Basics

## Overview

Python is a high-level, interpreted programming language known for its clear syntax and wide ecosystem.

## Running Python

```bash
python3 --version
python3 script.py
python3 -i          # interactive shell
```

## Variables and Types

```python
name = "Alice"          # str
age = 30                # int
pi = 3.14               # float
active = True           # bool
items = [1, 2, 3]       # list
point = (10, 20)        # tuple
data = {"key": "val"}   # dict
```

## Control Flow

```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

for i in range(5):
    print(i)

while active:
    break
```

## Functions

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

result = greet("Alice")
```

## Classes

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks"
```

## File I/O

```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Read
with open("file.txt", "r") as f:
    content = f.read()
```

## Virtual Environments

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

## References

- https://docs.python.org/3/
