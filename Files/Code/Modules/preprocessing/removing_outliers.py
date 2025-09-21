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

def remove_outliers(df, col, outlier_scope, debug):
    def get_by_range(df, col, min_v, max_v):
        return df[(df[col] >= min_v) & (df[col] <= max_v)]

    def IQR(df, col, m_quartile=0.1, max_quartile=0.9):
        # 3. Remove outliers using IQR
        Q1 = df[col].quantile(m_quartile)
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

    if debug['verbose']:
        print('Before Outlier Removal:', get_metadata(df, col))
    if debug['plot']:
        plot_graphs(df, col, 'Before Outlier Removal', buckets=100)

    min_q = outlier_scope.get('min_quantile', 0.1)
    max_q = outlier_scope.get('max_quantile', 0.9)
    # outlierless, metadata = bruter(df, col)
    # outlierless, metadata = brute(df, col)
    outlierless = IQR(df, col, min_q, max_q)

    if debug['verbose']:
        print('After Outlier Removal:', get_metadata(outlierless, col))
    if debug['plot']:
        plot_graphs(outlierless, col=col, title='After Outlier Removal', buckets=100)

    outlierless = force_positives(outlierless, col)

    if debug['verbose']:
        print('After Forcing Positives:', get_metadata(outlierless, col))
    if debug['plot']:
        plot_graphs(outlierless, col=col, title='After Forcing Positives', buckets=100)

    return outlierless
