import matplotlib.pyplot as plt

class StraightLine:

    # Method to draw straight line
    @staticmethod
    def draw_line(xs, ys, label_, color_, linestyle_, marker_):
        plt.plot(xs, ys, label=label_, color=color_,
                linestyle=linestyle_, marker=marker_)

    @staticmethod  
    def label_and_show():
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Graph of y=2x, y=3x & y=-x')
        plt.legend()
        plt.show()

straight_line = StraightLine()
straight_line.draw_line([1, 2], [2, 4], "y=2x", "m", "dashed", "*")
straight_line.draw_line([1, 2], [3, 6], "y=3x", "b", "dotted", "+")
straight_line.draw_line([1, 2], [-1, -2], "y=-x", "g", "solid", "x")
straight_line.label_and_show()