import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

class SeabornPlot:
    
    # Draws seaborn bar plot
    @staticmethod
    def draw_bar(x_column, y_column, dataset, title_, order_):
        sns.set(style ="whitegrid") 
        sns.barplot(x=x_column, y=y_column, hue = 'class',
                    data = dataset, palette = 'hls', order = order_,
                    )
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    # titanic_data = pd.read_csv("https://github.com//mwaskom//seaborn-data//blob/master//titanic.csv",
    #                             error_bad_lines=False)
    titanic_data = sns.load_dataset("titanic")
    SeabornPlot.draw_bar("sex", "survived", titanic_data,
                        "Sex against survived data of titanic", ['male', 'female'])

