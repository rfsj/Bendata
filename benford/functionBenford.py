def data_freq(benford_table):
    data = []
    for n in benford_table:
        data.append(n["data_frequency"])
    return data

def data_freq_perc(benford_table):
    data = []
    for n in benford_table:
        data.append(n["data_frequency_percent"])
    return data

def benford_freq(benford_table):
    data = []
    for n in benford_table:
        data.append(n["benford_frequency"])
    return data

def benford_freq_perc(benford_table):
    data = []
    for n in benford_table:
        data.append(n["benford_frequency_percent"])
    return data


def data_freq_difference(benford_table):
    data = []
    for n in benford_table:
        data.append(n["difference_frequency"])
    return data

def data_freq_difference_perc(benford_table):
    data = []
    for n in benford_table:
        data.append(n["difference_frequency_percent"])
    return data

def data_number(benford_table):
    data = []
    for n in benford_table:
        data.append(str(n["n"]))
    return data


    