import matplotlib.pyplot as plt
import numpy as np

class LinePlot:

    # Draws line plot of data with given label & color
    @staticmethod
    def plot_graph(xs, ys, label_, color_):
        plt.plot(xs, ys, label=label_, color=color_)

    @staticmethod
    def show_graph():
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title("Parabola & cubic curve")
        plt.legend()
        plt.show()

nums = np.arange(-5, 5, 0.1)
squares = [num**2 for num in nums]
cubes = [num**3 for num in nums]
LinePlot.plot_graph(nums, squares, "y=x^2", "b")
LinePlot.plot_graph(nums, cubes, "y=x^3", "y")
LinePlot.show_graph()
