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
    five_year_data = pd.read_csv("https://raw.githubusercontent.com//resbaz" +
                    "//r-novice-gapminder-files//master//data//gapminder-FiveYearData.csv")

    SeabornBoxPlot.draw_plot("continent", "lifeExp", five_year_data,
                        "Life expectancy against continent")

