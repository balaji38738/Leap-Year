import matplotlib.pyplot as plt

class BarChart:

    # Plots the chart
    def plot_chart(self, xs, ys, label_):
        self.xs = xs
        self.ys = ys
        plt.barh(xs, ys, label=label_)

    # Labels axes and displays chart
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    prog_language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    bar_chart = BarChart()
    bar_chart.plot_chart(prog_language, popularity, "language popularity")
    bar_chart.label_and_show("Popularity", "Programming language",
        "Programming language popularity chart")