#import libraries
import numpy as np
import pandas as pd
import sys
import math
import matplotlib.pyplot as plt
import collections
import random
#Function calculate codedrome --> https://www.codedrome.com/benfords-law-in-python/
BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
BENFORD_PERCENTAGES_SECOND_DIGIT = [0.1197, 0.1139, 0.1088, 0.1043, 0.1003, 0.0967, 0.0934, 0.0904, 0.0876, 0.0850]
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

def calculateSecondDigit(data):
    
    """
    Calculates a set of values from the numeric list
    input data showing how closely the first digits
    fit the Benford Distribution.
    Results are returned as a list of dictionaries.
    """

    results = []
    
    #first_digits = list(map(lambda n: str(n)[0], data))
    second_digits = list(map(lambda n: str(n)[1], data))
    #first_and_second_digits = first_digits + second_digits
    #first_digit_frequencies = collections.Counter(first_and_second_digits)
    first_digit_frequencies = collections.Counter(second_digits)

    for n in range(1, 10):

        data_frequency = first_digit_frequencies[str(n)]
        data_frequency_percent = data_frequency / len(data)
        benford_frequency = len(data) * BENFORD_PERCENTAGES_SECOND_DIGIT[n]
        benford_frequency_percent = BENFORD_PERCENTAGES_SECOND_DIGIT[n]
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
def get_random_data():
    
    """
    Returns a list of 1000 numbers approximately
    following the uniform distribution NOT the
    Benford Distribution.
    """

    random_data = [0] * 1000

    random_data = list(map(lambda n: n + random.randint(1, 1000), random_data))


    return random_data


def get_benford_data():

    """
    Returns a list of about 1000 numbers
    approximately following the Benford Distribution.
    """

    benford_data = []

    for first_digit in range(1, 10):
        random_factor = random.uniform(0.8, 1.2)
        for num_count in range(1, int(1000 * BENFORD_PERCENTAGES[first_digit] * random_factor)):
            start = first_digit * 1000
            benford_data.append({"example": random.randint(start, start + 1000)})
    return benford_data 

#Script create base benford
#df = pd.DataFrame(get_benford_data())
#df.to_csv(r'C:\Users\Ricardo\Downloads\\benford5.csv', index = False)