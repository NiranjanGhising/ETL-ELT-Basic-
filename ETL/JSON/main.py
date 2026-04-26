import ETL.JSON.extract as extract
import ETL.JSON.transform as transform
import ETL.JSON.load as load
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main(data_frame):
    
    extracted_data = extract.extract(data_frame)

    transformed_data = transform.transform(extracted_data)

    load_data = load.load(transformed_data, 'output.csv')

    return load_data


if __name__ == "__main__":
    main(data_frame = '/home/niranjanghising/.cache/kagglehub/datasets/rtatman/iris-dataset-json-version/versions/1/iris.json')

