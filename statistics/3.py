import numpy as np
import matplotlib.pyplot as plt


# https://proproprogs.ru/modules/matplotlib-granichnye-znacheniya-osey-i-lokatory-dlya-metok


# ------- 1

# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))

# Для set_xlim первое число MIN
# Второе число MAX

# ax.set_xlim(-5, 30)
# ax.set_ylim(-1, 6)
# plt.show()

# ------- 2

# from matplotlib.ticker import NullLocator
#
#
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))
# lc = NullLocator()
# ax.grid()
# # Скрывает метки по оси x
# ax.xaxis.set_major_locator(lc)
# plt.show()

# ------- 3

# from matplotlib.ticker import LinearLocator
#
#
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))
# lc = LinearLocator()
# ax.grid()
# # Делает 5 меток
# ax.yaxis.set_major_locator(LinearLocator(5))
# plt.show()

# ------- 4

# from matplotlib.ticker import MultipleLocator
#
#
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(1, 5, 0.25))
# lc = MultipleLocator()
# ax.grid()
# # Делает ШАГ меток длинной 1
# ax.xaxis.set_major_locator(MultipleLocator(base=1))
# plt.show()

# ------- 5

from matplotlib.ticker import IndexLocator


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
# Устанавливает метки от минимального значения до максимального
ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0))
plt.show()
