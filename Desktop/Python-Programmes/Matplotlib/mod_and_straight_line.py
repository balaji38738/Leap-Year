import matplotlib.pyplot as plt
import numpy as np

class LinePlot:

    # Draws line plot of data with given label, width & color
    @staticmethod
    def plot_graph(xs, ys, label_, color_, linewidth_):
        plt.plot(xs, ys, label=label_, color=color_, linewidth=linewidth_)

    @staticmethod
    def show_graph():
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title("Mod & straight line")
        plt.legend()
        plt.show()

nums = np.arange(-5, 6)
mod = [abs(num) for num in nums]
double = [2*num for num in nums]
LinePlot.plot_graph(nums, mod, "y=|x|", "b", 1)
LinePlot.plot_graph(nums, double, "y=2x", "y", 1.3)
LinePlot.show_graph()