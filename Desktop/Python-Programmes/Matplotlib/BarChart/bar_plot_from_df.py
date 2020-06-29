import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

class BarChart:

    # Plots the chart
    def plot_chart(self, df):
        df.plot(kind="bar")

    # Labels axes and displays chart
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    # Data
    values = np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
    df = pd.DataFrame(values, columns=['a','b','c','d','e'], index=np.arange(1, 10, 2))
 
    # Plot bar chart
    bar_chart = BarChart()
    bar_chart.plot_chart(df)
    bar_chart.label_and_show("x-axis", "y-axis", "Multiple bar plots")