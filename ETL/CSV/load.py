import pandas as pd
def load(data_frame, target_table):

    '''
    loads the data into the target table 

    Args:
        data_frame(dataframe): takes the csv file
        target_table(dataframe name): loads the file in specific file.
    '''
    
    data_frame.to_csv(target_table,index = False)

    return "File Saved!"
    