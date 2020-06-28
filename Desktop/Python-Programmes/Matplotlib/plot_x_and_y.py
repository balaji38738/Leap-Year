import matplotlib.pyplot as plt
import datetime
import numpy as np

class LinePlot:

    # Method to plot line
    def plot_line(self, xs, ys, label_):
        plt.plot(xs, ys, label=label_, color='b')

    # Labels the axis & title, and shows graph
    def label_and_show(self, xlabel_, ylabel_, title_):
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.title(title_)
        plt.legend()
        plt.show()

NUM_DAYS = 10
today = datetime.datetime.today()
date_list = [today - datetime.timedelta(days=x) for x in range(NUM_DAYS)]
date_list.reverse()
new_covid_patients = np.linspace(400000, 500000, num=10)
line = LinePlot()
line.plot_line(date_list, new_covid_patients, "June month covid patient graph")
line.label_and_show("Date", "Total covid patients", "Covid patients in India in June")