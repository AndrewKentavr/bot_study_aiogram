import numpy as np
import matplotlib.pyplot as plt

# https://proproprogs.ru/modules/matplotlib-razmeshchaem-standartnye-tekstovye-elementy-na-grafike

# ------- 1

# y = np.arange(0, 5, 1)
# x = np.array([a * a for a in y])
# y2 = [0, 2, 3, 4, 5, 7]
# x2 = [i + 1 for i in y2]
#
# lines = plt.plot(x, y, x2, y2)
#
# # Отключить показ сетки
# plt.grid(False)
#
# plt.show()

# ------- 2

# y = np.arange(0, 5, 1)
# x = np.array([a * a for a in y])
# y2 = [0, 2, 3, 4, 5, 7]
# x2 = [i + 1 for i in y2]
# lines = plt.plot(x, y, x2, y2)
#
# # Включаю МИНОРНОЙ показ сетки
# plt.minorticks_on()
#
# # Настройка самих сеток
# plt.grid(which='major', color='#444', linewidth=1)
# plt.grid(which='minor', color='#aaa', ls=':')
#
# plt.show()


# ------- 3

fig = plt.figure(figsize=(7, 4), facecolor='green')
ax = fig.add_subplot()
plt.figtext(0.05, 0.6, 'Текст в области окна')
fig.suptitle('Заголовок окна')


ax.set_xlabel('Ox')
ax.set_ylabel('Oy')

ax.text(0.05, 0.1, 'Произвольный текст в координатных осях')
ax.annotate('Аннотация', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})

plt.show()