from timeit import timeit


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

    # Монети повинні бути відсортовані в порядку зменшення номіналів
    coins.sort(reverse=True)

    rest_coins = dict()
    for coin in coins:
        if amount // coin > 0:
            rest_coins[coin] = amount // coin
            amount %= coin
            if amount == 0:
                break
    return rest_coins


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
    # мінімальна кількість монет для кожної суми
    min_coins_required = [0] + [float("inf")] * amount

    # які монети використані для кожної суми
    max_coin_used = [0] * (amount + 1)

    for suma in range(1, amount + 1):
        for coin in coins:
            # якщо поточна сума i >= за поточну монету
            # і мінімальна кількість монет для суми i - coin < мінімальна кількість монет для суми i
            if (
                suma >= coin
                and min_coins_required[suma - coin] + 1 < min_coins_required[suma]
            ):
                min_coins_required[suma] = min_coins_required[suma - coin] + 1
                max_coin_used[suma] = coin

    # print(f"{min_coins_required = }")
    # print(f"{max_coin_used = }")

    coins_required = dict()
    current_sum = amount
    while current_sum > 0:
        coin = max_coin_used[current_sum]
        coins_required[coin] = coins_required.get(coin, 0) + 1
        current_sum -= coin
    return coins_required


if __name__ == "__main__":

    tests = [
        (1327, [50, 25, 10, 5, 2, 1]),
        (113, [50, 25, 10, 5, 2, 1]),
        (12, [10, 6, 1]),
    ]

    number_tests = 100_000
    functions = [find_coins_greedy, find_min_coins]

    for amount, coins in tests:

        print(f"\n---=== Тест для суми {amount} і набору монет {coins} ===---")

        for func in functions:
            print(
                f"{func.__name__} = {func(amount, coins)}, всього монет {sum(func(amount, coins).values())}"
            )

        # continue

        # оцінка швидкості виконання
        print(f"\n--- оцінка швидкості виконання для n = {number_tests} ---")
        for func in functions:
            time = timeit(lambda: func(113, [50, 25, 10, 5, 2, 1]), number=number_tests)
            print(f"{func.__name__} - {time}")
