import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform(data_frame, value):
    
    '''
    Transforms the dataframe and only include the title and genre column for specific title
    
    Args:
        data_frame(dataframe): takes dataframe
        value(str): takes the title name
    
    Returns:
            dataframe with only title and genre column for specific value

    '''
    try:
        
        if data_frame['title'].isin([value]).any():
            logger.info("Successfully Transformed.")
            return data_frame.loc[data_frame['title']== value, ['title', 'genre']]
        else:
            logger.error(f"Title not found:{value}")
        

    except Exception as e:
        logger.error(f"Transform Failed.:{e}")
