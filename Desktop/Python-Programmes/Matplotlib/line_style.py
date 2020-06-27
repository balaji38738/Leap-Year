import matplotlib.pyplot as plot

class StraightLine:

    # Method to draw straight line
    @staticmethod
    def draw_line(xs, ys, label_, color_, linestyle_):
        plot.plot(xs, ys, label=label_, color=color_, linestyle=linestyle_)

    @staticmethod  
    def label_and_show():
        plot.xlabel('x-axis')
        plot.ylabel('y-axis')
        plot.title('Dashed & dotted line graph')
        plot.legend()
        plot.show()

straight_line = StraightLine()
straight_line.draw_line([1, 2], [2, 4], "y=2x", "m", "dashed")
straight_line.draw_line([1, 2], [3, 6], "y=3x", "b", "dotted")
straight_line.label_and_show()