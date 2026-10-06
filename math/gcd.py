"""
Алгоритм Евклида для нахождения НОД двух чисел.

Идея: НОД(a, b) = НОД(b, a mod b).
Процесс повторяется, пока одно из чисел не станет нулём.

Сложность:
- Время: O(log min(a, b))
- Память: O(1)
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b   
    return a

if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(gcd(a, b))