import pandas as pd
import sqlalchemy

def extract(table_name):
    db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/")

# Query the sales table
    return pd.read_sql("SELECT * FROM sales", db_engine)
