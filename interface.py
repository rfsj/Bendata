import random
from benford.functionBenford import *
from benford import calculateBenford
from data import loadData
from graphic.generateGraph import *

#codedrome
column = loadData.import_by_column()
benford_table = calculateBenford.calculate(column)

number = data_number(benford_table)
data_frequency = data_freq(benford_table)
data_frequency_percent = data_freq_perc(benford_table)
benford_frequency = benford_freq(benford_table)          
benford_frequency_percent = benford_freq_perc(benford_table)
difference_frequency = data_freq_difference(benford_table)
difference_frequency_percent = data_freq_difference_perc(benford_table)


def main():

    print("| Benford's Law |")

    graph_bar(number, data_frequency_percent)


main()