import matplotlib.pyplot as plt
import numpy as np

class BarChart:

    # Plots the chart
    def plot_chart(self, xs, ys, label_, color_, bar_width):
        self.xs = xs
        self.ys = ys
        plt.bar(self.xs, self.ys, label=label_, color=color_, width=bar_width)

    # Labels axes and displays chart
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.subplots_adjust(bottom=0.3)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    # Data
    men_means= (22, 30, 35, 35, 26)
    women_means = (25, 32, 30, 35, 29)
    xs = np.arange(1, 10, 2)
    bar_width = 0.4
    # Plot bar chart
    bar_chart = BarChart()
    bar_chart.plot_chart(xs, men_means, "men mean scores", "r", bar_width)
    bar_chart.plot_chart(xs+bar_width, women_means, "women mean scores", "b", bar_width)
    bar_chart.label_and_show("x-axis", "Mean scores",
        "Mean scores of men and women")