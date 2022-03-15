import numpy as np
import matplotlib.pyplot as plt

# https://proproprogs.ru/modules/matplotlib-dobavlyaem-legendu-i-risuem-geometricheskie-figury-na-grafikah

# ------- 1


# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')
# ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')
#
# ax.legend()
# plt.show()

# ------- 2

# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(np.arange(0, 5, 0.25))
# ax.plot(np.arange(0, 10, 0.5))
#
# line1, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')
# line2, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')
#
# # Можем изменять послед. вывода линий, а так же местополож. легенды
# ax.legend((line2, line1), ['Линия 2', 'Линия 1'], loc='upper right')
# # loc: ['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center']
#
# plt.show()

# ------- 3

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25))
ax.plot(np.arange(0, 10, 0.5))

line1, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line2, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')

ax.legend((line2, line1), [r'$f(x) = a \cdot b + c$', r'$f(x) = k \cdot x + b$'], facecolor='#aaa', framealpha=0.5)

plt.show()

