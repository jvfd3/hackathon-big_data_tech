""" FUNC: Plotting graphs and removing outliers """

import matplotlib.pyplot as plt
import seaborn as sns

def plot_graphs(df, col='quantity', title='', buckets=1000):
    # 2. Plot the distribution before removing outliers
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=buckets, kde=True)
    plt.title(title)
    plt.show()

def get_metadata(df, col):
    return {
        'size': df.shape[0],
        'col': col,
        'min': df[col].min(),
        'max': df[col].max()
    }

def remove_outliers(df, col, min_q, max_q):
    def get_by_range(df, col, min_v, max_v):
        return df[(df[col] >= min_v) & (df[col] <= max_v)]
    
    def IQR(df, col, min_quartile=0.1, max_quartile=0.9):
        # 3. Remove outliers using IQR
        Q1 = df[col].quantile(min_quartile)
        Q3 = df[col].quantile(max_quartile)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        iqr_outlierless = get_by_range(df, col, lower_bound, upper_bound)

        return iqr_outlierless
    
    def bruter(df, col):
        outlierless = get_by_range(df, col, -100, 20000)
        return outlierless

    def brute(df, col):
        outlierless = get_by_range(df, col, -100, 20000)
        return outlierless
    
    def force_positives(df, col):
        outlierless = df[df[col] > 0]
        return outlierless


    print('Before Outlier Removal:', get_metadata(df, col))
    plot_graphs(df, col, 'Before Outlier Removal', buckets=100)

    # outlierless, metadata = bruter(df, col)
    # outlierless, metadata = brute(df, col)
    outlierless = IQR(df, col, min_q, max_q)

    print('After Outlier Removal:', get_metadata(outlierless, col))
    plot_graphs(outlierless, col=col, title='After Outlier Removal', buckets=100)

    outlierless = force_positives(outlierless, col)

    print('After Forcing Positives:', get_metadata(outlierless, col))
    plot_graphs(outlierless, col=col, title='After Forcing Positives', buckets=100)

    return outlierless
