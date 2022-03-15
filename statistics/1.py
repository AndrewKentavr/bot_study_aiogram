import matplotlib.pyplot as plt
import numpy as np

# https://proproprogs.ru/modules/matplotlib-funkciya-plot-dlya-postroeniya-i-oformleniya-dvumernyh-grafikov

x = np.array([0, 5, 6, 7, 8])
y = np.array([1, 2, -6, 0, 4])

x_2 = np.array([0, 3, 4, 5, 7])
y_2 = np.array([3, 1, -3, 0, 6])

# Если передать список, то он будет конвертироват в массив NumPy
# plt.plot(x, y)

# ------- 1
# plt.plot(x, y, x_2, y_2, 'r--')

# ------- 2

# Параметры для графиков - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
lines_1 = plt.plot(x, y)
lines_2 = plt.plot(x_2, y_2)
plt.setp(lines_2, linestyle='-.', color='r', marker='o', markerfacecolor='black')

# ------- 3

# Настройка будет сделанна общая
lines = plt.plot(x, y, x_2, y_2)
plt.setp(lines, linestyle='-.')
# Закрашивание графика
plt.fill_between(x, y, where=y > 0)
# Сетка для графика
plt.grid()
plt.show()
