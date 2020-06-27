import matplotlib.pyplot as plot
import pandas as pd

class FileHandler:
    
    # Given text file returns co-ordinates from it
    @staticmethod
    def get_file_data(file_path):
        return pd.read_csv(file_path)


class LinePlot:

    # Draws line plot of given ohlc data
    @staticmethod 
    def draw_plot(ohlc):
        plot.plot(ohlc["Date"], ohlc["Open"], label='Open', color='r')
        plot.plot(ohlc["Date"], ohlc["High"], label='High', color='g')
        plot.plot(ohlc["Date"], ohlc["Low"], label='Low', color='b')
        plot.plot(ohlc["Date"], ohlc["Close"], label='Close', color='y')
        plot.xlabel('Date')
        plot.ylabel('Sensex')
        plot.title('Financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.')
        plot.legend()
        plot.show()


ohlc = FileHandler.get_file_data("Resources//fdata.csv")
LinePlot.draw_plot(ohlc)


