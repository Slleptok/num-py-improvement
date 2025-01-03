import numpy as np

# Одномерный массив
arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# Двумерный массив
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

# Вывод информации
print("Тип объекта:", type(arr))
print("Размерность массива:", matrix.ndim)

import time

# Создаем большие массивы
list_data = list(range(int(1e6)))
numpy_data = np.arange(int(1e6))

# Умножение в списке
start = time.time()
list_result = [x * 2 for x in list_data]
print("List time:", time.time() - start)

# Умножение в NumPy
start = time.time()
numpy_result = numpy_data * 2
print("NumPy time:", time.time() - start)

# Сравнение операций
numpy_sum = np.sum(numpy_data)
print("Sum with NumPy:", numpy_sum)

# Создание матрицы признаков
features = np.random.random((100, 5))  # 100 образцов, 5 признаков


# Создание сетки координат для графика
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Решение линейных уравнений
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)


# Создание массива
arr = np.array([1, 2, 3, 4], dtype='float32')

# Атрибуты массива
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

# Пример изменения формы
matrix = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = matrix.reshape((3, 2))
print("Reshaped:\n", reshaped)


# Доступ к элементам
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Элемент:", arr[1, 2])  # 6
print("Строка:", arr[1, :])   # [4 5 6]
print("Столбец:", arr[:, 1])  # [2 5 8]

# Изменение элемента
arr[1, 2] = 10
print(arr)

# Изменение строки
arr[0, :] = [0, 0, 0]
print(arr)

# Массивы с разными значениями
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
random = np.random.random((3, 3))
identity = np.eye(3)

# Диапазон значений
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

arr = np.arange(1, 21).reshape(4, 5)
print(arr)

# Неправильное копирование
a = np.array([1, 2, 3])
b = a
b[0] = 10
print("Оригинал изменился:", a)

# Правильное копирование
b = a.copy()
b[0] = 20
print("Оригинал не изменился:", a)

arr = np.array([1, 2, 3, 4])
print("Add:", arr + 2)
print("Multiply:", arr * 3)
print("Square:", arr ** 2)

# Тригонометрия
angles = np.array([0, np.pi / 2, np.pi])
print("Sine:", np.sin(angles))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Умножение матриц
product = np.dot(A, B)

# Определитель
det = np.linalg.det(A)

# Обратная матрица
inv = np.linalg.inv(A)

data = np.array([1, 2, 3, 4, 5])

# Среднее, медиана, стандартное отклонение
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

# Минимум и максимум
min_val = np.min(data)
max_val = np.max(data)

# Загрузка из текстового файла
data = np.loadtxt('data.txt', delimiter=',')

# Загрузка из CSV
#import pandas as pd
#data = pd.read_csv('data.csv').values

arr = np.array([10, 15, 20, 25, 30])

# Логическая маска
mask = arr > 20
print(arr[mask])  # [25 30]

# Индексация с условиями
even = arr[arr % 2 == 0]
print(even)  # [10 20 30]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = arr[::2, ::2]
print(result)  # [[1 3]
               #  [7 9]]
