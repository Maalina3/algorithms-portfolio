"""
Поиск двух чисел с заданной суммой в неотсортированном массиве.

Используется хеш-таблица (set) для проверки,
встречалось ли уже число target - x.

Сложность:
- Время: O(n)
- Память: O(n)
"""

def two_sum_hash(arr, target):
    seen = set()
    for x in arr:
        if target - x in seen:
            return x, target - x
        seen.add(x) 

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(two_sum_hash(arr, target))