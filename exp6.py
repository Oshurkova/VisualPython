import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')

ax.legend()

ax.set_title('Синус и косинус')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()