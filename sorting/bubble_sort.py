"""
Пузырьковая сортировка.

Соседние элементы сравниваются и меняются местами,
если стоят в неправильном порядке.
Проход повторяется, пока массив не отсортируется.

Сложность:
- Время: O(n²)
- Память: O(1)
"""

def bubble_sort(arr):
    for j in range(len(arr) - 1, 0, -1):
        flag = True
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = False
        if flag:
            break
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(bubble_sort(arr))