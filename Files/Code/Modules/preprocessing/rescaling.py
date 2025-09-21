""" Rescaling the numerical columns in the dataframe """

def rescale_zero_to_one(df):
    """ Rescales all numerical columns in the dataframe to a range between 0 and 1 """
    df = df.select_dtypes(include=['number'])  # Select only numerical columns
    return df
