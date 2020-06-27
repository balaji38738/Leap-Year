import numpy as np
import matplotlib.pyplot as plt
june_dates = [6, 10, 14, 20, 24]
petrol_price = [78.32, 80.40, 82.70, 85.70, 86.54]
petrol_price_dollar = [1, 1.1, 1.2, 1.3, 1.4]
plt.hist(june_dates, bins=petrol_price, label="Diesel Prices", histtype='bar', rwidth=0.9)
plt.xlabel('June')
plt.ylabel('Petro price')
plt.title('histogram')
plt.legend()
plt.show()
