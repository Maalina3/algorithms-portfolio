"""
Удаление всех вхождений элемента из списка (in-place).

Используются два указателя: i читает, k пишет.
Элементы, не равные element, сдвигаются в начало,
сохраняя исходный порядок.

Сложность:
- Время: O(n)
- Память: O(1)
"""

def remove_element(arr, element):
    k = 0
    for i in range(len(arr)):
        if arr[i] != element:
            arr[k] = arr[i]
            k += 1
    return arr[:k]

if __name__ == "__main__":
    arr = input().split()
    element = input()
    print(remove_element(arr, element))