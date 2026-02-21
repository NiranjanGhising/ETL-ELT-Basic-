import pandas as pd
import os 

def load(data_frame, target_table):

    '''
    loads the data into the target table 

    Args:
        data_frame(dataframe): takes the csv file
        target_table(dataframe name): loads the file in specific file.
    '''
    
    data_frame.to_sql(target_table)
    file_exists = os.path.exists(target_table)
    if file_exists:
        return "File Saved!"
    else:
        raise Exception(f"File does NOT exists at path {target_table}")

    