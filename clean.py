from numpy import float64
import pandas as pd

# negative protocol
def remove_lines_with_negatives(data, keyscolumn_select):
    if data[keyscolumn_select].dtypes == float64:
        data_remove = data.loc[data[keyscolumn_select] < 0]
        data = data.drop(data_remove.index)
    return data


def remove_negative_from_each_cell(data, keyscolumn_select): #ok
    data[keyscolumn_select] = data[keyscolumn_select].apply(lambda x: str(x).replace("-","")) #Quando precisar de um valor absoluto (Ex: resposta veio negativa mas o valor precisa ser positivo), usar o método abs(n).
    #data[keyscolumn_select] = data[keyscolumn_select].astype("float64")
    return data

def separate_negative_lines_for_analysis(data, keyscolumn_select):
    if data[keyscolumn_select].dtypes == float64:
        data_remove = data.loc[data[keyscolumn_select] < 0]
        return data_remove
    else:
        return data


#remove null lines
def remove_null_lines(data, keyscolumn_select):
    data.dropna(axis = 0, subset = keyscolumn_select) # duvida dropando linhas, onde na coluna selecionada existe NaN(Qm sabe usar uma comparação com o nome ou numero do documento para verificar se há)
    return data

#remove duplicate lines
def remove_duplicate_lines(data):
    data.drop_duplicates()
    return data

# force NaN in df
def force_to_numeric(data_clean, keyscolumn_select): #???
    data_clean = pd.to_numeric(data_clean[keyscolumn_select], errors="coerce")
    return data_clean

def all_clean():
    return
######Na teoria, creio que não haja a necessidade de retirar os outlier, pois eles já podem ser uma anomalia(ou fraude) 