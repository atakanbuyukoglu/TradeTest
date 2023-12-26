import numpy as np
from matplotlib import pyplot as plt

# Code to test algo on some random price movement

price_start = 100
price_volatility = 1.0
timestep_count = 10000

# Percentage change for every day
price_change = np.random.normal(loc=0.0, scale=price_volatility, size=(timestep_count,))

prices = np.cumprod(np.concatenate(([price_start], 0.01 * price_change + 1)))

plt.plot(prices)
plt.xlabel('Zaman')
plt.ylabel('Fiyat')
plt.title('Hisse Grafiği')
plt.show()


