import extract
import transform
import load
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main(data_frame):
    
    extracted_data = extract.extract(data_frame)

    transformed_data = transform.transform(extracted_data, value = '13 Sins')

    load_data = load.load(transformed_data, 'output.csv')

    return load_data


if __name__ == "__main__":
    main(data_frame = 'netflix_data.csv')

