import numpy as np
import matplotlib.pyplot as plt

# ------- 1

# plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# plt.grid()
# plt.show()

# ------- 2

# ax_1 = plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# ax_2 = plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# ax_3 = plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# ax_1.grid()
# ax_2.grid()
# ax_3.grid()
# plt.show()

# ------- 3

# Первое число в subplot - это сколько будет графиков на y координате
# Второе число - это сколько графиков на x координате
# Третье число - это индекс элемента по заданым коор.
# ax_1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
#
# ax_2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
#
# ax_3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
# #
# ax_4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
#
# ax_1.grid()
# ax_2.grid()
# ax_3.grid()
# plt.show()

# ------- 4

f, ax = plt.subplots(2, 2)

ax[0, 0].plot(np.arange(0, 5, 0.2))
plt.grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
plt.grid()
ax[1, 0].plot(np.arange(0, 5, 0.2))
plt.grid()
ax[1, 1].plot(np.arange(0, 5, 0.2))
plt.grid()


# 4 И 5 ПУНКТЫ МОЖНО ЗАПУСКАТЬ ОДНОВРЕМЕННО, ПОЛУЧИВ 2 ОКНА
# ------- 5

fig = plt.figure(figsize=(7, 4))
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(np.arange(0, 5, 0.2))

plt.show()


# ------- 6

# from matplotlib.gridspec import GridSpec
#
# ws = [1, 2, 5]
# hs = [2, 0.5]
#
# fig = plt.figure(figsize=(7, 4))
# gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)
#
# ax1 = plt.subplot(gs[0, 0])
# ax1.plot(np.arange(0, 5, 0.2))
# ax2 = fig.add_subplot(gs[1, 0:2])
# ax2.plot(np.random.random(10))
# ax3 = fig.add_subplot(gs[:, 2])
# ax3.plot(np.random.random(10))
#
#
# plt.show()
