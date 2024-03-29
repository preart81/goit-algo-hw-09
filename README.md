# Реалізація функцій для касової системи, яка видає решту покупцеві

Жадібні алгоритми та динамічне програмування

## Опис методів

В модулі `main.py` реалізовано два метода для визначення оптимального способу видачі решти покупцеві.

1.  `find_coins_greedy`

```Py
def find_coins_greedy(amount: int, coins: list = [50, 25, 10, 5, 2, 1]) -> dict:
    """
    Функція приймає суму, яку потрібно видати покупцеві, і повертає словник із
    кількістю монет кожного номіналу, що використовуються для формування цієї
    суми.

    Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}.
    Це жадібний алгоритм: спочатку відбирає найбільші доступні номінали монет.

    Параметри:
        amount:int -- сума, яку потрібно видати
        coins:list -- список номіналів монет відсортований по спаданню

    Повертає:
        словник з кількістю монет кожного номіналу
    """
```

1.  `find_min_coins`

```Py
def find_min_coins(amount: int, coins: list = [50, 25, 10, 5, 2, 1]) -> dict:
    """
    Функція приймає суму, яку потрібно видати покупцеві, і повертає словник із
    кількістю монет кожного номіналу, що використовуються для формування цієї
    суми.

    Використовується метод динамічного програмування, щоб знайти мінімальну
    кількість монет, необхідних для формування цієї суми.

    Функція повертає словник із номіналами монет та їх кількістю для досягнення
    заданої суми найефективнішим способом.

    Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}

    Параметри:
        amount -- сума, яку потрібно видати
        coins -- список номіналів монет

    Повертає:
        словник з кількістю монет кожного номіналу
    """
```

## Порівняння ефективності алгоритмів

### Тестування

Результати тестування часу виконання за допомогою timeit із кількістю посторів n:

```
---=== Тест для суми 1327 і набору монет [50, 25, 10, 5, 2, 1] ===---
find_coins_greedy = {50: 26, 25: 1, 2: 1}, всього монет 28
find_min_coins = {50: 26, 25: 1, 2: 1}, всього монет 28

--- оцінка швидкості виконання для n = 100000 ---
find_coins_greedy - 0.08794469991698861
find_min_coins - 5.44215889996849

---=== Тест для суми 113 і набору монет [50, 25, 10, 5, 2, 1] ===---
find_coins_greedy = {50: 2, 10: 1, 2: 1, 1: 1}, всього монет 5
find_min_coins = {50: 2, 10: 1, 2: 1, 1: 1}, всього монет 5

--- оцінка швидкості виконання для n = 100000 ---
find_coins_greedy - 0.07808149978518486
find_min_coins - 5.689623800106347

---=== Тест для суми 12 і набору монет [10, 6, 1] ===---
find_coins_greedy = {10: 1, 1: 2}, всього монет 3
find_min_coins = {6: 2}, всього монет 2

--- оцінка швидкості виконання для n = 100000 ---
find_coins_greedy - 0.0872295000590384
find_min_coins - 5.287456399993971
```

### Висновки

Жадібний алгоритм `find_coins_greedy` витрачає в 60 разів менше часу в тестах.

Він швидше знаходить відповідь. Крім того в нього передбачено вихід з циклу, якщо зібрано необхідну суму. Часова складність жадібного алгоритму в гіршому випадку $O(n)$, в кращому випадку – $O(1)$ (коли перша монета рівна потрібній сумі).

Часова складність динамічного алгоритму `find_min_coins` приблизно $O(n^2)$

Динамічний алгоритм може знайти мінімально можливу решту по кількості монет, жадібний алгоритм не гарантує такої оптимізації.
