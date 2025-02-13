import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем параметры тора
R = 3  # Расстояние от центра тора до центра "трубы"
r = 1  # Радиус "трубы"

# Создаем углы theta и phi
theta = np.linspace(0, 2 * np.pi, 35)  # Угол вокруг "трубы"
phi = np.linspace(0, 2 * np.pi, 35)  # Угол вокруг центра тора

# Создаем сетку углов
theta, phi = np.meshgrid(theta, phi)

# Преобразуем параметрические уравнения в декартовы координаты
x = (R + r * np.cos(theta)) * np.cos(phi)
y = (R + r * np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Рисуем тор
ax.plot_surface(x, y, z, color='coral', alpha=0.8)

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Тор (Бублик)')

# Устанавливаем одинаковый масштаб для осей
ax.set_box_aspect([1, 1, 0.4])  # Это делает оси равномасштабными

# Показываем график
plt.show()