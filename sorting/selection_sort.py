"""
Сортировка выбором.

На каждом шаге ищется минимальный элемент в неотсортированной части
и меняется местами с первым элементом этой части.

Сложность:
- Время: O(n²)
- Память: O(1)
"""

def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimum_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(selection_sort(arr))