import ETL.SQL.extract as extract
import ETL.SQL.transform as transform
import ETL.SQL.load as load
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main(data_frame):
    
    extracted_data = extract.extract(data_frame)

    transformed_data = transform.transform(extracted_data, value = '13 Sins')

    load_data = load.load(transformed_data, 'output.sql')

    return load_data


if __name__ == "__main__":
    main(data_frame = 'netflix_data.csv')

