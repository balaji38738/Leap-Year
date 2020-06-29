import matplotlib.pyplot as plt 
import numpy as np
import random

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
    # Generates random weight(kg) & height(feet) data for gymnasts
    gymnast_weight = [random.uniform(50, 70) for index in range(10)]
    gymnast_height = [random.uniform(5.8, 6.5) for index in range(10)]

    # Generates random weight(kg) & height(feet)  data for basketball players
    basketball_player_weight = [random.uniform(60, 75) for index in range(10)]
    basketball_player_height = [random.uniform(6.4, 7) for index in range(10)]

    # Generates random weight(kg) & height(feet) for sumo wrestlers
    sumo_wrestler_weight = [random.uniform(100, 150) for index in range(10)]
    sumo_wrestler_height = [random.uniform(5.6, 6.4) for index in range(10)]  

    # Plotting gymnast data
    ScatterPlot.draw_plot(gymnast_weight, gymnast_height, "Gymnast")

    # Plotting basketball player data
    ScatterPlot.draw_plot(basketball_player_weight, basketball_player_height, "Basketball player")

    # Plotting sumo wrestler data
    ScatterPlot.draw_plot(sumo_wrestler_weight, sumo_wrestler_height, "Sumo wrestler")

    # Show graph
    ScatterPlot.label_and_show("Weight(Kg)", "Height(feet)",
                                "Physique data of players among different games")