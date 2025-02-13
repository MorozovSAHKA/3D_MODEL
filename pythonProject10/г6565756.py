import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_excel("Book1.xlsx")  # Укажи свой файл
X = df["X"]
Y = df["Y"]
Z = df["Z"]


# Построение 3D-точек
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='coolwarm')  # Точки окрашены по значению Z

plt.show()