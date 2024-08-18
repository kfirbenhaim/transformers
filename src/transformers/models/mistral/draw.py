import matplotlib.pyplot as plt
# Define the sets of 2D points
x1 = [64, 256, 2048, 4096]
topline = [9.4162, 9.4162, 9.4162, 9.4162]
tova_optimal = [9.9858, 9.5426, 9.4163, 9.4162]
tova = [54.2388, 18.1461, 11.6944, 9.4162]
sliding_window = [9.4162]
plt.plot(x1, topline, label='Topline')
plt.plot(x1, tova_optimal, label='Optimal TOVA')
plt.plot(x1, tova, label='TOVA')
# plt.plot(x1[-1], sliding_window, label='Sliding Window')
plt.xticks(x1)
plt.legend()
plt.show()
