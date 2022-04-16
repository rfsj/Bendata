#import scipy.stats as stats
import pandas as pd
import scipy
import scipy.stats as stats
from numpy import mean, absolute
import math
import numpy
import scipy
import scipy.stats as stats
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def zscore(length, data_frequency_percent, benford_frequency_percent): #Percent
    results = []
    for n in range(0, 9):
        if (abs(data_frequency_percent[n] - benford_frequency_percent[n])) > (1 / (2 * length)):
           zscore = (abs(data_frequency_percent[n] - benford_frequency_percent[n]) - (1 / (2 * length))) / (math.sqrt(benford_frequency_percent[n] * ((1-benford_frequency_percent[n]) / length)))
        else:
           zscore = (abs(data_frequency_percent[n] - benford_frequency_percent[n])) / (math.sqrt(benford_frequency_percent[n] * ((1 - benford_frequency_percent[n]) / length)))
        results.append({"n": n+1,
                        "zscore": zscore})
    print(results)
    return results
    
    #((|p-p0|)-(1/2n))/sqrt(p0(1-p0)/n)
    return 
def chi_square(data_frequency, benford_frequency):
    results = []
    chi_square = 0
    chi_square_sum = 0
    for n in range(0, 9):
        O = data_frequency[n]
        E = benford_frequency[n]
        chi_square = (O-E)**2/E
        chi_square_sum = chi_square_sum + chi_square
        results.append({"n": n+1,
                        "chi_square": chi_square}) 
    return results, chi_square_sum

def mad(data_frequency_percent, benford_frequency_percent):
    K = 8 #for one digit
    mad_sum = 0
    for n in range(0, 9):
        O = data_frequency_percent[n]
        E = benford_frequency_percent[n]
        mad = abs(O-E)/ K
        mad_sum = mad_sum + mad
    #|pi-p0i|/K
    return mad_sum

def testM(length, data_frequency_percent, benford_frequency_percent): #quem sabe não kk
    #m = sqrt(n) max i=1..9 {|p0 - log_10(1+1/i)|}
    array = []
    for n in range(0, 9):
        O = data_frequency_percent[n]
        E = benford_frequency_percent[n]
        value = abs(O-E)
        array.append(value)
    max_m = max(array)
    testM = math.sqrt(length) * max_m
    return testM

