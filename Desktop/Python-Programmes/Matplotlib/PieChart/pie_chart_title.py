import matplotlib.pyplot as plt

class PieChart:

    # Draws the pie chart
    @staticmethod
    def draw_chart(slice_names, slice_values, colors_, title_):
        plt.pie(
                slice_values,
                labels=slice_names,
                startangle=90,
                explode=(0, 0.1, 0, 0, 0, 0),
                autopct='%.2f%%',
                shadow=True)
        plt.title(title_)
        plt.show()

if __name__ == "__main__":
    # Data
    prog_language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    #Plot graph
    colors = ["r", "g", "b", "y", "c", "m"]
    PieChart.draw_chart(prog_language, popularity,
                        colors, "Programming Language popularity chart")