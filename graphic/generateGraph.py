import matplotlib.pyplot as plt
import pandas as pd
#creating bar graphs
def graph_bar(number, data_frequency_percent):
    plt.bar(number, data_frequency_percent)
    plt.xlabel('Números')
    plt.ylabel('Porcetagem')
    plt.title('Plot')
    plt.show()

def graph_bar_benford(number, benford_frequency_percent):
    plt.bar(number, benford_frequency_percent)
    plt.xlabel('Números')
    plt.ylabel('Porcetagem')
    plt.title('Plot')
    plt.show()    

def graph_bar_join(number, keycolumn):
    join_bar = pd.DataFrame(keycolumn, number)
    return join_bar
