import pandas as pd 
import numpy as np

class DictToDf:

    # Converts a dictionary to dataframe
    @staticmethod
    def get_df(dict, index_):
        return pd.DataFrame(dict, index=index_)

if __name__  == "__main__":
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
                        'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
    
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    exam_df = DictToDf.get_df(exam_data, labels)

    # Prints name & score columns of dataframe
    print(exam_df.iloc[[1, 3, 5, 6], [0, 1]])