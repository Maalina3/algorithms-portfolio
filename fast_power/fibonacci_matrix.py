"""
Нахождение n-го числа Фибоначчи через матрицы.

Матрица [[1, 1], [1, 0]] возводится в степень n.
Верхний правый (или же нижний левый) элемент результата — F(n).

Используется быстрое возведение матрицы в степень за O(log n).

Сложность:
- Время: O(log n)
- Память: O(log n)
"""

def matrix_multiplication(a, b):
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
    ]
    
def fibonacci_matrix(n, matrix):
  if n <= 1:
    return matrix
  elif n % 2 == 0:
    return fibonacci_matrix(n // 2, matrix_multiplication(matrix, matrix))
  else:
    return matrix_multiplication(matrix, (fibonacci_matrix((n-1) // 2, matrix_multiplication(matrix,matrix))))

if __name__ == "__main__":
    matrix = ((1, 1), (1, 0))
    n = int(input())
    if n == 0:
        print("0")
    else:     
        matrix = fibonacci_matrix(n, matrix)
        print(matrix[0][1])