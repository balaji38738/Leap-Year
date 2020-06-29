import matplotlib.pyplot as plt
import numpy as np

class BarChart:

    # Plots the chart
    def plot_chart(self, xs, ys, label_):
        self.xs = xs
        self.ys = ys
        x_pos = np.arange(1, 12, 2)
        plt.xticks(x_pos, self.xs)
        plt.bar(x_pos, self.ys, label=label_, color="red")

    # Labels axes and displays chart
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.subplots_adjust(bottom=0.3)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    prog_language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    bar_chart = BarChart()
    bar_chart.plot_chart(prog_language, popularity, "language popularity")
    bar_chart.label_and_show("Programming language", "Popularity",
        "Programming language popularity chart")