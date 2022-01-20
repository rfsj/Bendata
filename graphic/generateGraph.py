import matplotlib.pyplot as plt

def graph_bar(number, data_frequency_percent):
    plt.bar(number, data_frequency_percent)
    plt.xlabel('Números')
    plt.ylabel('Porcetagem')
    plt.title('Plot')
    plt.show()