# Algorithms Practice

Репозиторий с реализациями классических алгоритмов и структур данных на Python.

## Содержание

### Two Pointers (два указателя)

Метод решения задач, где два указателя двигаются навстречу друг другу
или с разной скоростью. Работает за O(n) по времени.

- **`reverse_list.py`** — разворот списка на месте
- **`remove_element.py`** — удаление всех вхождений элемента
- **`two_sum_sorted.py`** — поиск пары с суммой в отсортированном массиве
- **`two_sum_unsorted.py`** — поиск пары с суммой через хеш-таблицу

### Math (математика)

Классические математические алгоритмы.

- **`gcd.py`** — алгоритм Евклида для нахождения НОД
- **`extended_gcd.py`** — расширенный алгоритм Евклида (коэффициенты Безу)
- **`binary_gcd.py`** — бинарный алгоритм Евклида (алгоритм Штейна)
- **`lcm.py`** — наименьшее общее кратное
- **`is_prime.py`** — проверка числа на простоту
- **`sieve.py`** — решето Эратосфена
- **`factorize.py`** — разложение числа на простые множители
- **`fast_power.py`** — быстрое возведение числа в степень
- **`fibonacci_matrix.py`** — числа Фибоначчи через матрицы

### Sorting (сортировки)

Классические алгоритмы сортировки.

- **`bubble_sort.py`** — пузырьковая сортировка
- **`insertion_sort.py`** — сортировка вставками
- **`selection_sort.py`** — сортировка выбором

### Searching (поиск)

Алгоритмы поиска в массивах.

- **`binary_search.py`** — бинарный поиск
- **`interpolation_search.py`** — интерполяционный поиск

### Stack (стек)

Задачи на использование стека.

- **`infix_to_postfix.py`** — перевод инфиксного выражения в постфиксное и вычисление

## Сложность алгоритмов

| Файл | Время | Память |
|------|-------|--------|
| `reverse_list.py` | O(n) | O(1) |
| `remove_element.py` | O(n) | O(1) |
| `two_sum_sorted.py` | O(n) | O(1) |
| `two_sum_unsorted.py` | O(n) | O(n) |
| `gcd.py` | O(log min(a, b)) | O(1) |
| `extended_gcd.py` | O(log min(a, b)) | O(log min(a, b)) |
| `binary_gcd.py` | O(log min(a, b)) | O(1) |
| `lcm.py` | O(log min(a, b)) | O(1) |
| `sieve.py` | O(n log log n) | O(n) |
| `factorize.py` | O(√n) | O(log n) |
| `fast_power.py` | O(log n) | O(log n) |
| `fibonacci_matrix.py` | O(log n) | O(log n) |
| `bubble_sort.py` | O(n²) | O(1) |
| `insertion_sort.py` | O(n²) | O(1) |
| `selection_sort.py` | O(n²) | O(1) |
| `binary_search.py` | O(log n) | O(1) |
| `interpolation_search.py` | O(log log n) | O(1) |
| `infix_to_postfix.py` | O(n) | O(n) |