import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений x от 0 до 2π
x = np.linspace(0, 2 * np.pi, 100)

# Вычисление значений y для каждой функции
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Построение графиков с разными цветами и стилями линий
plt.plot(x, y_sin, label='y = sin(x)', color='blue', linestyle='-')
plt.plot(x, y_cos, label='y = cos(x)', color='red', linestyle='--')
plt.plot(x, y_tan, label='y = tan(x)', color='green', linestyle=':')

# Добавление легенды
plt.legend()

# Добавление подписей осей и заголовка
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций y = sin(x), y = cos(x), y = tan(x)')

# Добавление сетки
plt.grid(True)

# Отображение графика
plt.show()