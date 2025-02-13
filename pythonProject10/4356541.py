import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=1, scale=1, size=1000)
plt.hist(data, bins=30, color="blue", edgecolor="black")

plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма случайных данных')

plt.grid(True)

plt.show()