import pandas as pd

def transform(raw_data):

    raw_data["Order Date"] = pd.to_datetime(raw_data['Order Date'], format="%m/%d/%y %H:%M")

    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data['Price Each']<10, :]

  	# Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data.loc[raw_data['Quantity Ordered']>1, :]
    
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = clean_data.loc[:,['Order Date','Quantity Ordered','Purchase Address']]
    
    
    

    # Return the filtered DataFrame
    return clean_data
    