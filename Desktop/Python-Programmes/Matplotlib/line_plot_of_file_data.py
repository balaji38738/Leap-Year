import matplotlib.pyplot as plot

class FileHandler:
    
    # Given text file returns co-ordinates from it
    @staticmethod
    def get_file_data(file_path):
        with open(file_path, "r") as file:
            all_lines = file.readlines()
        xs, ys = [], []
        for line in all_lines:
            x, y = line.split(" ")
            xs.append(x)
            ys.append(y)
        return xs, ys
            

class LinePlot:

    # Draws line plot from given lists of x & y co-ordinates
    @staticmethod 
    def draw_plot(xs, ys):
        plot.plot(xs, ys, label='line', color='b')
        plot.xlabel('x-axis')
        plot.ylabel('y-axis')
        plot.title('line graph')
        plot.legend()
        plot.show()

xs, ys = FileHandler.get_file_data("Resources/test.txt")
LinePlot.draw_plot(xs, ys)