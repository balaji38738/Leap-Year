import pandas as pd 

class PandasArray:
    
    # Creates 1d array
    def create_1d_array(self):
        self.one_d_array = pd.Series([1, 2, 3, 4, 5])

    # Displays the array
    def display_array(self):
        print("1D Array", self.one_d_array, sep="\n")

    # Converts the array to list
    def convert_to_list(self):
        self.list_ = self.one_d_array.tolist()

    # Displays the list & type
    def display_list_and_type(self):
        print("List of 1D array = ", self.list_)
        print("Type of", self.list_, "=", type(self.list_))

if __name__ == "__main__":
    pd_array = PandasArray()
    pd_array.create_1d_array()
    pd_array.display_array()
    pd_array.convert_to_list()
    pd_array.display_list_and_type()