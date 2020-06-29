import matplotlib.pyplot as plt 
import numpy as np

class ScatterPlot:
    # Draws scatter plot
    @staticmethod
    def draw_plot(xs, ys, label_):
        plt.scatter(xs, ys, label=label_, facecolors='none', edgecolors="b")
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('scatter plot')
        plt.legend()
        plt.show()

    
if __name__ == "__main__":
    # Generates random data
    xs = np.random.randn(100)
    ys = np.random.randn(100)

    ScatterPlot.draw_plot(xs, ys, "Random Distribution")