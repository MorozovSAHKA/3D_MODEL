import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем радиус сферы
r = 1

# Создаем углы theta и phi
theta = np.linspace(0, np.pi, 100)  # Угол от 0 до pi
phi = np.linspace(0, 2 * np.pi, 100)  # Угол от 0 до 2pi

# Создаем сетку углов
theta, phi = np.meshgrid(theta, phi)

# Преобразуем сферические координаты в декартовы
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Рисуем сферу
ax.plot_surface(x, y, z, color='b', alpha=0.7)

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Сфера')

# Устанавливаем одинаковый масштаб для осей
ax.set_box_aspect([1, 1, 1])  # Это делает оси равномасштабными

# Показываем график
plt.show()