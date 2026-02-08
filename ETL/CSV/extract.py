import pandas as pd
import logging

logger = logging.getLogger(__name__)

def extract(data_frame):
    '''
    Takes the csv file and give few rows of the dataframe
    ARGS:
        filename: takes dataframe.

    Result: reads the file of the specific dataframe.
    '''

    try:
        data_frame = pd.read_csv(data_frame)
        logger.info("Successfully extracted.\n")
        return data_frame
    except FileNotFoundError:
        logger.error(f"File Not Found :{data_frame}")
        raise

    except Exception as e:
        logger.critical(f"Unexpected error during extraction: {e}")
        raise



