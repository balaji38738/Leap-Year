import matplotlib.pyplot as plot

class StraightLine:

    # Method to draw straight line
    def draw_line(self):
        plot.plot([1, 2], [1, 4], label='straight line', color='b')
        plot.xlabel('x-axis')
        plot.ylabel('y-axis')
        plot.title('Straight line graph')
        plot.legend()
        plot.show()

straight_line = StraightLine()
straight_line.draw_line()
