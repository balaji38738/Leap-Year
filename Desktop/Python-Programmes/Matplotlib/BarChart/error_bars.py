import matplotlib.pyplot as plt
import numpy as np

class BarChart:

    # Plots the chart
    def plot_chart(self, xs, ys, label_, yerr_):
        self.xs = xs
        self.ys = ys
        plt.bar(self.xs, self.ys, label=label_, yerr=yerr_)

    # Labels axes and displays chart
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    # Data
    mean_velocity = [0.2474, 0.1235, 0.1737, 0.1824]
    xs = np.arange(1, 8, 2)
    velocity_std = [0.3314, 0.2278, 0.2836, 0.2645]

    # Plot bar chart
    bar_chart = BarChart()
    bar_chart.plot_chart(xs, mean_velocity, "men mean scores", velocity_std)
    bar_chart.label_and_show("x-axis", "mean velocity", "Mean velocity with std")