"""
Быстрое возведение числа в степень.

Степень делится пополам на каждом шаге:
x^n = (x^(n/2))^2, если n чётное,
x^n = (x^(n/2))^2 * x, если n нечётное.

Сложность:
- Время: O(log n)
- Память: O(log n) — глубина рекурсии
"""

def fast_power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return fast_power(x * x, n // 2)
    elif n % 2 == 1:
        return x * fast_power(x * x, (n - 1) // 2)

if __name__ == "__main__":
    x, n = int(input()), int(input())
    print(fast_power(x, n))