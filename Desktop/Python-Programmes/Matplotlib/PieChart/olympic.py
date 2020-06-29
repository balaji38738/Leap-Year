import matplotlib.pyplot as plt
import pandas as pd

class PieChart:

    # Draws the pie chart
    @staticmethod
    def draw_chart(slice_names, slice_values, colors_, title_):
        plt.pie(
                slice_values,
                labels=slice_names,
                startangle=90,
                explode=(0.1, 0, 0, 0),
                autopct='%.2f%%',
                shadow=True)
        plt.title(title_)
        plt.show()


if __name__ == "__main__":
    # Data
    olympic_data = pd.read_csv("Resources//olympic_data.csv")

    #Plot graph
    colors = ["r", "g", "b", "y"]
    PieChart.draw_chart(olympic_data["country"], olympic_data["gold_medal"],
                        colors, "Gold medals of five most successful countries in 2016 summer olympics")