import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

class SeabornBoxPlot:
    
    # Draws seaborn box plot
    @staticmethod
    def draw_plot(x_column, y_column, dataset, title_):
        sns.boxplot(x=x_column, y=y_column, data=dataset)
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    tips = pd.read_csv("https://raw.githubusercontent.com"
                                + "//mwaskom//seaborn-data//master//tips.csv")

    SeabornBoxPlot.draw_plot("day", "tip", tips,
                        "Day against tips")

