import numpy as np
import matplotlib.pyplot as plot
june_dates = [6, 10, 14, 20, 24]
petrol_price = [78.32, 80.40, 82.70, 85.70, 86.54]
petrol_price_dollar = [1, 1.1, 1.2, 1.3, 1.4]
plot.hist(june_dates, petrol_price, histtype='bar', rwidth=0.9)
plot.xlabel('June')
plot.ylabel('Petro price')
plot.title('histogram')
plot.legend()
plot.show()
