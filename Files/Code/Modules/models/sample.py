""" Get Sample """

import matplotlib.pyplot as plt
import numpy as np

def get_sample(clean_data, col, plot: bool = False):
    sample = clean_data[col].values
    # sample = clean_data[sampled_col.sum()].values
    if plot:
        plt.figure(figsize=(12, 6))
        plt.bar(range(len(clean_data)), sample)
    return sample


""" Create Feature and Rescale """

def create_feature_rescale(sampled): # Rescaling e sampling
    sample = (sampled - np.min(sampled)) / (np.max(sampled) - np.min(sampled))
    
    feature = [sampled[t] - sampled[t-1] for t in range(1, len(sampled))]
    feature = (feature - np.min(feature)) / (np.max(feature) - np.min(feature))
    return sample, feature
