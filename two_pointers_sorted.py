"""
Задача: найти два числа в массиве, сумма которых равна target.
Используется метод двух указателей.
Сложность: O(n) по времени, O(1) по памяти.
Массив должен быть отсортирован.
"""
def two_pointers_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left != right:
        total = arr[left] + arr[right]
        if total == target:
            return arr[left], arr[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(two_pointers_sorted(arr, target))