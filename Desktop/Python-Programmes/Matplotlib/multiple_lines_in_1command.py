import matplotlib.pyplot as plt
import numpy as np

class MultipleLinePlot:
    def __init__(self, xs1, ys1, xs2, ys2):
        self.xs1 = xs1
        self.ys1 = ys1
        self.xs2 = xs2
        self.ys2 = ys2

    # Labels axes, title & shows graph
    def plot_graph(self, xlabel_, ylabel_, title_):
        plt.plot(self.xs1, self.ys1, "b.", self.xs2, self.ys2, "r--")
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend("")
        plt.show()

nums = np.arange(10)
multiline_line = MultipleLinePlot(nums, nums**2, nums, nums**3)
multiline_line.plot_graph("x-axis", "y-axis", "parabola & cubic graph")