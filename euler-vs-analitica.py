import numpy as np
import matplotlib.pyplot as plt

# Parámetros
h = 0.2
t = np.arange(0, 1 + h, h)

# Solución analítica
y_exacta = np.exp(-t)

# Método de Euler
y_euler = np.zeros(len(t))
y_euler[0] = 1

for i in range(1, len(t)):
    y_euler[i] = y_euler[i-1] - h * y_euler[i-1]

# Resultados
print("t    Exacta    Euler")
for ti, ye, yn in zip(t, y_exacta, y_euler):
    print(f"{ti:.1f}  {ye:.4f}  {yn:.4f}")

# Gráfica
plt.plot(t, y_exacta, label="Solución exacta")
plt.plot(t, y_euler, 'o--', label="Euler")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Comparación: Solución Analítica vs Método de Euler")
plt.legend()
plt.grid(True)
plt.show()