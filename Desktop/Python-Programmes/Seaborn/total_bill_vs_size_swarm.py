import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

class SeabornSwarmPlot:
    
    # Draws seaborn box plot
    @staticmethod
    def draw_plot(x_column, y_column, dataset, title_):
        sns.swarmplot(x=x_column, y=y_column, data=dataset)
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    tips = pd.read_csv("https://raw.githubusercontent.com"
                    + "//mwaskom//seaborn-data//master//tips.csv")

    SeabornSwarmPlot.draw_plot("size", "total_bill", tips,
                        "Size against total bill")