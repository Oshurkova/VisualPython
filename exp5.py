import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

fig, axs = plt.subplots(3, 1, figsize=(10, 8))

axs[0].plot(x, y1, color='blue')
axs[0].set_title('График синуса')

axs[1].plot(x, y2, color='green')
axs[1].set_title('График косинуса')

axs[2].plot(x, y3, color='red')
axs[2].set_title('График тангенса')

for ax in axs:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

plt.tight_layout()
plt.show()