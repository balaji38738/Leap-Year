import matplotlib.pyplot as plt
import seaborn as sns

class SeabornPointPlot:
    
    # Draws seaborn point plot
    @staticmethod
    def draw_point_plot(x_column, y_column, dataset, title_, order_):
        sns.set(style ="whitegrid") 
        sns.pointplot(x=x_column, y=y_column, hue = 'class',
                    data = dataset, palette = 'hls', order = order_,
                    )
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    titanic_data = sns.load_dataset("titanic")
    SeabornPointPlot.draw_point_plot("sex", "survived", titanic_data,
                        "Sex against survived data of titanic", ['male', 'female'])