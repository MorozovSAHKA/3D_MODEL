import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений x от 0 до 2π
x = np.linspace(0, 2 * np.pi, 100)

# Вычисление значений y = sin(x)
y = np.sin(x)

# Построение графика
plt.plot(x, y)

# Добавление подписей осей и заголовка
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = sin(x)')

# Добавление сетки
plt.grid(True)

# Отображение графика
plt.show()