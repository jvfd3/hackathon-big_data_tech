""" Rescaling the numerical columns in the dataframe """

def rescale_zero_to_one(df):
    """ Rescales all numerical columns in the dataframe to a range between 0 and 1 """
    new_min, new_max = 0, 1
    df = (df - df.min()) / (df.max() - df.min()) * (new_max - new_min) + new_min
    return df
