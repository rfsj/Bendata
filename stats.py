#import scipy.stats as stats
import pandas as pd
import scipy.stats as stats
from numpy import mean, absolute
def chi_square(data_graph):
    #https://towardsdatascience.com/chi-square-test-with-python-d8ba98117626
    data_stat = data_graph.iloc[:, [0,1,3]]
    print(data_stat)
    df = pd.DataFrame(data_stat, columns = ['n', 'data_frequency', 'benford_frequency']) 
    df['expected_freq'] = df['benford_frequency'].sum() * df['data_frequency']
    print(df)
    # significance level
    alpha = 0.05

    # Calcualtion of Chisquare
    chi_square = 0
    for i in range(len(df)):
        O = df.loc[i, 'benford_frequency']
        E = df.loc[i, 'expected_freq']
        chi_square += (O-E)**2/E

    # The p-value approach
    print("Approach 1: The p-value approach to hypothesis testing in the decision rule")
    p_value = 1 - stats.chi2.cdf(chi_square, df['n'].nunique() - 1)
    print(p_value)
    conclusion = "Failed to reject the null hypothesis."
    if p_value <= alpha:
        conclusion = "Null Hypothesis is rejected."
            
    print("chisquare-score is:", chi_square, " and p value is:", p_value)
    print(conclusion)
        
    # The critical value approach
    print("\n--------------------------------------------------------------------------------------")
    print("Approach 2: The critical value approach to hypothesis testing in the decision rule")
    critical_value = stats.chi2.ppf(1-alpha, df['n'].nunique() - 1)
    conclusion = "Failed to reject the null hypothesis."
    if chi_square > critical_value:
        conclusion = "Null Hypothesis is rejected."
            
    print("chisquare-score is:", chi_square, " and critical value is:", critical_value)
    print(conclusion)

def z_score(data,keyscolumn_select):
    #zscore = scipy.stats.zscore(data[keyscolumn_select], axis=0, ddof=0, nan_policy='propagate')
    #or
    zscore_mean = data[keyscolumn_select].mean()
    zscore_str = data[keyscolumn_select].std()
    zscore = (data[keyscolumn_select]-zscore_mean)/zscore_str
    return zscore
def absolute_mean_deviation(specific_column_transform_to_list):
    # Importing mean, absolute from numpy
    series = pd.Series(specific_column_transform_to_list)
    #result = series.mad()
    mean_series = series.mean()[0]
    result = (series - mean_series).abs()
    print(result)
    return result