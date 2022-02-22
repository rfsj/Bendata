import random
from benford.functionBenford import *
from benford import calculateBenford
from data import loadData
from graphic.generateGraph import *

#import full database
##data = loadData.import_csv_data()

#import specific column
data = loadData.import_by_column()

#use the first digit function(benford) --> dictionary with {"n","data_frequency","data_frequency_percent","benford_frequency","benford_frequency_percent","difference_frequency","difference_frequency_percent"}
benford_table = calculateBenford.calculate(data)

#extract information with aux fuctions
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
    graph_bar_benford(number, benford_frequency_percent)

main()
