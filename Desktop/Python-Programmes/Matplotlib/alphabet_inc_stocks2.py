import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime as dt

class Alphabet:
    __stock_data = []

    # Adds stock data
    @classmethod
    def generate_stock_data(cls):
        NUM_DAYS = 5
        start_day = dt.date(2016, 10, 3)
        dates = [start_day + dt.timedelta(days=num) for num in range(NUM_DAYS)]
        stock_value = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
        cls.__stock_data = list(zip(dates, stock_value))

    # Returns a list of stock data
    @classmethod
    def get_stock_data(cls):
        return zip(* cls.__stock_data)


class GridGraph:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    # Plots and displays the graph
    def draw_graph(self):
        fig = plt.figure()
        graph = fig.add_subplot(111)

        # Plot the data as a blue line with cross markers
        graph.plot(self.xs, self.ys, 'b-x')

        # Set the xtick locations
        graph.set_xticks(self.xs)

        # Set the xtick labels
        graph.set_xticklabels([date.strftime("%d-%m-%y") for date in self.xs])

        plt.xlabel('Date')
        plt.ylabel('Closing Value')
        plt.title('Closing value of Alphabet Inc.')
        plt.minorticks_on()

        # Customizing the grid lines
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='yellow')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')

        # Turn off the display of all ticks.
        plt.tick_params(which='both',
                        top=False,
                        left=False,
                        right=False,
                        bottom=False)
        
        plt.show()


Alphabet.generate_stock_data()
dates, stock_value = Alphabet.get_stock_data()
stock_graph = GridGraph(dates, stock_value)
stock_graph.draw_graph()