import numpy as np
import matplotlib.pyplot as plt

# Параметры системы
m = 1.0  # масса груза
l = 1.0  # длина стержня и пружины
g = 9.81  # ускорение свободного падения
w = 0.0  # частота движения

# Функция для расчета реакции N
def reaction(O, O_dot):
    return m * l * O_dot ** 2 - m * g * np.cos(O)

# Углы O, скорости V0 и шаг по времени
O0 = 0.0
O_dot_min = np.sqrt(g/l)  # наименьшая скорость V0 при растянутом стержне AB
O_values = np.linspace(0, np.pi/2, 100)
O_dot_values = np.linspace(0, 2*O_dot_min, 100)  # скорость точки B

# Рассчитываем реакцию N в зависимости от угла O
N_values = np.zeros_like(O_values)
for i, O in enumerate(O_values):
    N_values[i] = reaction(O, O_dot_min)

# Построение графика реакции N от угла O
plt.figure()
plt.plot(O_values, N_values, label='Reakcia N')
plt.xlabel('O')
plt.ylabel('N')
plt.title('Зависимость реакции N от угла O')
plt.legend()
plt.grid()
plt.show()
