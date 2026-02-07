import pandas as pd
def extract(filename):
    '''
    Takes the csv file and give few rows of the file
    ARGS:
        filename: takes csv file.

    Result: reads the file and give few rows of the specific csv file.
    '''
    print(f"extracting the file:{filename}")
    data_frame = pd.read_csv("netflix_data.csv")
    return data_frame.head()

