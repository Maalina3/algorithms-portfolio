"""
Разворот списка на месте с помощью двух указателей.

Два указателя начинают с концов массива и двигаются навстречу,
меняя элементы местами.

Сложность:
- Время: O(n)
- Память: O(1)
"""

def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(reverse_list(arr))