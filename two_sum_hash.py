"""
Задача: найти два числа в неотсортированном массиве, сумма которых равна target.
Используется хеш-таблица (set).
Сложность: O(n) по времени, O(n) по памяти.
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