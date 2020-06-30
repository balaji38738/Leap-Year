import matplotlib.pyplot as plt 
import seaborn as sns

class SeabornViolinPlot:
    
    # Draws seaborn violin plot
    @staticmethod
    def draw_plot(x_column, y_column, dataset, title_):
        sns.set(style ="whitegrid") 
        sns.violinplot(x=x_column, y=y_column, data=dataset)
        plt.title(title_) 
        plt.show()


if __name__ == "__main__":
    iris = sns.load_dataset("iris")

    SeabornViolinPlot.draw_plot("species", "sepal_length", iris,
                        "Species against sepal length of iris flower")

