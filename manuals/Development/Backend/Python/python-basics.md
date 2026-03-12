# Основы Python

## Обзор

Python — высокоуровневый интерпретируемый язык программирования, известный чистым синтаксисом и широкой экосистемой.

## Запуск Python

```bash
python3 --version
python3 script.py
python3 -i          # интерактивная оболочка
```

## Переменные и типы

```python
name = "Alice"          # str
age = 30                # int
pi = 3.14               # float
active = True           # bool
items = [1, 2, 3]       # list
point = (10, 20)        # tuple
data = {"key": "val"}   # dict
```

## Управляющие конструкции

```python
if age >= 18:
    print("Взрослый")
elif age >= 13:
    print("Подросток")
else:
    print("Ребёнок")

for i in range(5):
    print(i)

while active:
    break
```

## Функции

```python
def greet(name: str) -> str:
    return f"Привет, {name}!"

result = greet("Alice")
```

## Классы

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} издаёт звук"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} лает"
```

## Работа с файлами

```python
# Запись
with open("file.txt", "w") as f:
    f.write("Привет\n")

# Чтение
with open("file.txt", "r") as f:
    content = f.read()
```

## Виртуальные окружения

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

## Ссылки

- https://docs.python.org/3/
