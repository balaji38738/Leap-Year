import matplotlib.pyplot as plt

class StraightLine:

    # Method to draw straight line
    def draw_line(self):
        plt.plot([1, 2], [1, 4], label='straight line', color='b')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Straight line graph')
        plt.legend()
        plt.show()

straight_line = StraightLine()
straight_line.draw_line()
