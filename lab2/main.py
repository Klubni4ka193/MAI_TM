#Задание 16 №2

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Параметры системы
l = 1.0  # длина стержня и пружины
m = 1.0  # масса груза
c = 1.0  # жесткость пружины
w = 1.0  # частота движения

# Дифференциальное уравнение движения точки B
def system(y, t):
    theta, omega = y
    dydt = [omega, -(c*l/m)*np.sin(theta) - w**2*np.sin(theta)]
    return dydt

# Начальные условия
y0 = [np.pi/4, 0.0]

# Временной интервал
t = np.linspace(0, 10, 100)

# Решение дифференциального уравнения
sol = odeint(system, y0, t)

# Функция для анимации движения
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'o-')

def animate(i):
    x = np.array([0, l*np.sin(sol[i, 0]), l*np.sin(sol[i, 0])])
    y = np.array([0, -l*np.cos(sol[i, 0]), -l*np.cos(sol[i, 0])])
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(sol), interval=50, blit=True)


plt.show()
