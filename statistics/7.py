import numpy as np
import matplotlib.pyplot as plt

# https://proproprogs.ru/modules/matplotlib-risuem-stupenchatye-stekovye-stem-i-tochechnye-grafiki

# ------- 1 СТУПЕНЧАТЫЙ ГРАФИК

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
x = np.arange(0, 10)

# step - ступенчатые график
#
# where - изменяет местоположение ТОЧЕК на графике
# ax.step(x, x, '-go', where='pre')
# ax.step(x, x, '-go', where='mid')
ax.step(x, x, '-go', where='post')

ax.grid()

# ------- 2 ГИСТОГРАММА

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
y = np.random.normal(0, 2, 500)

# с помощью второго значения можно изменять диапозон столбов
ax.hist(y, 50)
ax.grid()

# ------- 3 ГИСТОГРАММА BAR

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
x = [f'H{i+1}' for i in range(10)]
y = np.random.randint(1, 5, len(x))

ax.bar(x, y)
ax.grid()

# ------- 4 ГИСТОГРАММА BAR, по оси ординат

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
x = [f'H{i+1}' for i in range(10)]
y = np.random.randint(1, 5, len(x))

ax.barh(x, y)
ax.grid()

# ------- 5 ГИСТОГРАММА BAR

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(3, 20, len(x))
w = 0.3
ax.bar(x - w / 2, y1, width=w)
ax.bar(x + w / 2, y2, width=w)

ax.grid()

# ------- 6 Круговые диаграммы
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
ax.pie(vals, labels=labels)
ax.grid()
plt.show()
