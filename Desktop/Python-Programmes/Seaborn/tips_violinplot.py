import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

class SeabornViolinPlot:
    
    # Draws seaborn violin plot
    @staticmethod
    def draw_plot(x_column, y_column, dataset, title_):
        sns.set(style ="whitegrid") 
        sns.violinplot(x=x_column, y=y_column, data=dataset)
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv") 

    SeabornViolinPlot.draw_plot("sex", "total_bill", tips,
                        "sex against total bill")

