
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import collections
import datetime
import random
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt

import numpy as np

import warnings
warnings.filterwarnings('ignore')


def get_random_data():
    
    """
    Returns a list of 1000 numbers approximately
    following the uniform distribution NOT the
    Benford Distribution.
    """

    random_data = [0] * 1000

    random_data = list(map(lambda n: n + random.randint(1, 1000), random_data))

    return random_data

BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def calculate(data):

    """
    Calculates a set of values from the numeric list
    input data showing how closely the first digits
    fit the Benford Distribution.
    Results are returned as a list of dictionaries.
    """

    results = []
    
    first_digits = list(map(lambda n: str(n)[0], data))
    first_digit_frequencies = collections.Counter(first_digits)

    for n in range(1, 10):

        data_frequency = first_digit_frequencies[str(n)]
        data_frequency_percent = data_frequency / len(data)
        benford_frequency = len(data) * BENFORD_PERCENTAGES[n]
        benford_frequency_percent = BENFORD_PERCENTAGES[n]
        difference_frequency = data_frequency - benford_frequency
        difference_frequency_percent = data_frequency_percent - benford_frequency_percent

        results.append({"n": n,
                        "data_frequency":               data_frequency,
                        "data_frequency_percent":       data_frequency_percent,
                        "benford_frequency":            benford_frequency,
                        "benford_frequency_percent":    benford_frequency_percent,
                        "difference_frequency":         difference_frequency,
                        "difference_frequency_percent": difference_frequency_percent})

    return results

data = get_random_data()

benford_table = calculate(data)
print(type(benford_table))
def data_freq(data_norm):
    data = []
    for n in benford_table:
        data.append(n["data_frequency"])
    return data

def data_freq_perc(data_norm):
    data = []
    for n in benford_table:
        data.append(n["data_frequency_percent"])
    return data

def benford_freq(data_norm):
    data = []
    for n in benford_table:
        data.append(n["benford_frequency"])
    return data

def benford_freq_perc(data_norm):
    data = []
    for n in benford_table:
        data.append(n["benford_frequency_percent"])
    return data


def data_freq_difference(data_norm):
    data = []
    for n in benford_table:
        data.append(n["difference_frequency"])
    return data

def data_freq_difference_perc(data_norm):
    data = []
    for n in benford_table:
        data.append(n["difference_frequency_percent"])
    return data

def data_number(data_norm):
    data = []
    for n in benford_table:
        data.append(str(n["n"]))
    return data

number = data_number(benford_table)
data_frequency = data_freq(benford_table)
data_frequency_percent = data_freq_perc(benford_table)
benford_frequency = benford_freq(benford_table)          
benford_frequency_percent = benford_freq_perc(benford_table)
difference_frequency = data_freq_difference(benford_table)
difference_frequency_percent = data_freq_difference_perc(benford_table)

plt.bar(number, data_frequency_percent)
plt.xlabel('Números')
plt.ylabel('Porcetagem')
plt.title('Plot')
plt.show()

