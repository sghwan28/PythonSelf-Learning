import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 100)

plt.plot(x, x**0.5, label='square root')
plt.plot(x, np.sin(x), label='sinc')
plt.plot(x, x**2, label='square')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("test plot")

plt.legend()

plt.show(block=True)
plt.interactive(False)