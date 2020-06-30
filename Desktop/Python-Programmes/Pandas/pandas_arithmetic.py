import pandas as pd 

class PdArrayArithmetic:

    # Returns addition of 2 pandas arrays
    def add(self, array1, array2):
        return array1 + array2

    # Returns subtraction of 2 pandas arrays
    def subtract(self, array1, array2):
        return array1 - array2

    # Returns multiplication of 2 pandas arrays
    def multiply(self, array1, array2):
        return array1 * array2

    # Returns division of 2 pandas arrays
    def divide(self, array1, array2):
        return array1 / array2

if __name__ == "__main__":
    # Pandas arrays
    array1 = pd.Series([1, 2, 3, 4, 5])
    array2 = pd.Series([2, 3, 5, 7, 9])
    
    pd_arithmetic = PdArrayArithmetic()
    
    print("array1", array1)
    print("array2", array2)

    print("array1 + array2", pd_arithmetic.add(array1, array2), sep="\n")
    print("array1 - array2", pd_arithmetic.subtract(array1, array2), sep="\n")
    print("array1 * array2", pd_arithmetic.multiply(array1, array2), sep="\n")
    print("array1 / array2", pd_arithmetic.divide(array1, array2), sep="\n")