import pandas as pd 

class PdArrayArithmetic:

    # Returns one array raised to another array
    def power(self, array1, array2):
        return array1**array2

if __name__ == "__main__":
    # Pandas arrays
    array1 = pd.Series([0, 1, 2, 3, 4, 5, 6])
    array2 = pd.Series([3] * 7)
    
    pd_arithmetic = PdArrayArithmetic()
    
    print("array1", array1, sep="\n")
    print("array2", array2, sep="\n")

    print("array1**array2", pd_arithmetic.power(array1, array2), sep="\n")