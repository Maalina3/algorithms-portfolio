"""
Поиск двух чисел с заданной суммой в отсортированном массиве.

Два указателя начинают с концов массива и двигаются навстречу:
если сумма меньше target — левый вправо,
если больше — правый влево.

Сложность:
- Время: O(n)
- Память: O(1)
"""

def two_sum_sorted(arr, target):
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
    print(two_sum_sorted(arr, target))