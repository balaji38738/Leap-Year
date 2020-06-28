import matplotlib.pyplot as plt 

class MultiplePlots:
    fig = plt.figure()
    
    # Adds plot on figure
    def more_plot(self, nrows, ncols, index):
        plt.subplot(nrows, ncols, index)

    def plot_graph(self, xs, ys, label_):
        self.xs = xs
        self.ys= ys
        plt.plot(self.xs, self.ys, label=label_)

    # Labels the axis & title, and shows graph
    def label_graph(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()

    # Displays the graph
    def show_graph(self):
        plt.show()

if __name__ == "__main__":
    # Data
    time = [0, 5, 10, 15]
    distance = [0, 40, 70, 90]
    speed = [0, 8, 6, 4]

    multiple_plot = MultiplePlots()

    # Time vs distance graph
    multiple_plot.more_plot(1, 2, 1)
    multiple_plot.plot_graph(time, distance, "Time vs Distance")
    multiple_plot.label_graph("Time(s)", "Distance(m)", "Time vs Distance Graph")

    # Time vs speed graph
    multiple_plot.more_plot(1, 2, 2)
    multiple_plot.plot_graph(time, speed, "Time vs Speed")
    multiple_plot.label_graph("Time(s)", "Speed(m/s)", "Time vs Speed graph")
    multiple_plot.show_graph()
