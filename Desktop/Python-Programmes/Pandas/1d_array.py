import pandas as pd 

class PandasArray:
    def create_1d_array(self):
        self.one_d_array = pd.Series([1, 2, 3, 4, 5])

    def display_array(self):
        print(self.one_d_array)

if __name__ == "__main__":
    pd_array = PandasArray()
    pd_array.create_1d_array()
    pd_array.display_array()