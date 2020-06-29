import matplotlib.pyplot as plt 
import numpy as np

class ScatterPlot:
    # scatter plot
    @staticmethod
    def draw_plot(xs, ys, label_):
        plt.scatter(xs, ys, label=label_)

    # Labels axes & title & shows graph
    @staticmethod
    def label_and_show(xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()
        plt.show()

    
if __name__ == "__main__":
    # Data
    math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
    science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
    marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Plotting math marks
    ScatterPlot.draw_plot(marks_range, math_marks, "Maths marks")

    # Plotting science marks
    ScatterPlot.draw_plot(marks_range, science_marks, "Science marks")

    # Show graph
    ScatterPlot.label_and_show("Marks range", "Marks scored",
                                "Marks of 10 students in science and maths")