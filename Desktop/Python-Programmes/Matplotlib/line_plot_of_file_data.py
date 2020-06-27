import matplotlib.pyplot as plt

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
        plt.plot(xs, ys, label='line', color='b')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('line graph')
        plt.legend()
        plt.show()

xs, ys = FileHandler.get_file_data("Resources/test.txt")
LinePlot.draw_plot(xs, ys)