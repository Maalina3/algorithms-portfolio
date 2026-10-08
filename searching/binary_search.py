"""
Бинарный поиск в отсортированном массиве.

Цель: найти индекс элемента target.
На каждом шаге берём серединный элемент. Если он меньше target —
ищем справа, если больше — слева. Каждый шаг вдвое сокращает область поиска.

Возвращает индекс найденного элемента или -1, если элемента нет.

Сложность:
- Время: O(log n)
- Память: O(1)
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        half = (left + right) // 2
        if arr[half] == target:
            return half
        elif arr[half] < target:
            left = half + 1
        elif arr[half] > target:
            right = half - 1
    return -1
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(binary_search(arr, target))