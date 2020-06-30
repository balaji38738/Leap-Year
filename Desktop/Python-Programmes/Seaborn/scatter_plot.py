import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

class SeabornScatterPlot:
    
    # Draws seaborn bar plot
    @staticmethod
    def draw_scatte_plot(x_column, y_column, dataset, title_):
        sns.set(style ="whitegrid") 
        sns.scatterplot(x=x_column, y=y_column, data=dataset)
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv") 

    SeabornScatterPlot.draw_scatte_plot("day", "total_bill", tips,
                        "Day against total bill")

