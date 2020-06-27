import matplotlib.pyplot as plt
import numpy as np
import math

class StraightLine:

    # Draw line given xs & ys
    def draw_line(self, xs, ys, label_):
        plt.plot(xs, ys, marker='+', label=label_, markersize=5)
        plt.yscale("linear")
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Graph of y=2x')
        plt.legend()
        plt.show()

    # Displays current axis llmits
    @staticmethod
    def display_axis_limits():
        print(plt.axis())

    @staticmethod
    def change_axis_limits(xmin, xmax, ymin, ymax):
        plt.axis([xmin, xmax, ymin, ymax])

xs = np.arange(1, 20)
ys = [2*x for x in xs]
straight_line = StraightLine()
straight_line.draw_line(xs, ys, "y=2x")
straight_line.display_axis_limits()
straight_line.change_axis_limits(-20, 20, 0, 80)
straight_line.display_axis_limits()
straight_line.draw_line(xs, ys, "y=2x")