import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 1000)

y = np.sqrt(x) * np.sin(10 * x)

plt.plot(x, y, linestyle='-', color='b', linewidth=2, label='$Y(x) = x^{1/2} \cdot \sin(10x)$')

plt.xlabel('x', fontsize=12, color='blue') 
plt.ylabel('y', fontsize=12, color='blue') 

plt.title('Графік функції Y(x)')

plt.legend()

plt.grid(True)

plt.show()
