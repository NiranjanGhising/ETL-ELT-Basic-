def transform(data_frame, value):
    '''
    Transforms the dataframe and only include the title and genre column for specific title
    
    Args:
        data_fram(csv file): takes csv file 
        Value(str): takes the title name
    
    Returns:
            CSV file with only title and genre column for specific value
            
    '''
    return data_frame.loc[data_frame['title']== value, ['title', 'genre']]