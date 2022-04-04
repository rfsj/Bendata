from numpy import float64
import pandas as pd
# obsolete
# negative protocol
def remove_lines_with_negatives(data, keyscolumn_select): 
    if data[keyscolumn_select].dtypes == float64:
        data_remove = data.loc[data[keyscolumn_select] < 0]
        #data_remove = data.loc[lambda data: data[keyscolumn_select] < 0]
        data = data.drop(data_remove.index)
        print(data)
        return data

def remove_negative_from_each_cell(data, keyscolumn_select): 
    data[keyscolumn_select] = data[keyscolumn_select].apply(lambda x: str(x).replace("-","")) #Quando precisar de um valor absoluto (Ex: resposta veio negativa mas o valor precisa ser positivo), usar o método abs(n).
    #data[keyscolumn_select] = data[keyscolumn_select].astype("float64")
    print(data)
    return data


def separate_negative_lines_for_analysis(data, keyscolumn_select): #data remove recolhe os dados certos, mas n alterar
    if data[keyscolumn_select].dtypes == float64:
        #data = data[keyscolumn_select].apply(lambda x: x < 0) # retorna true e false
        data_remove = data.loc[data[keyscolumn_select] > 0] #
        data = data.drop(data_remove.index)
        print(data)
        return data
    
 
#function option

def function_option_negative_protocol(radio_option_negative_protocol, data, keyscolumn_select):
    if radio_option_negative_protocol == "remove lines with negatives":
        remove_lines_with_negatives(data, keyscolumn_select)
    elif radio_option_negative_protocol == "remove negative from each cell":
        remove_negative_from_each_cell(data, keyscolumn_select)
    elif radio_option_negative_protocol == "separate negative lines for analysis": 
        separate_negative_lines_for_analysis(data, keyscolumn_select)

#remove null lines
def remove_null_lines(data, keyscolumn_select):
    data.dropna(subset = keyscolumn_select, inplace = True) # duvida dropando linhas, onde na coluna selecionada existe NaN(Qm sabe usar uma comparação com o nome ou numero do documento para verificar se há)
    return data

#remove duplicate lines
def remove_duplicate_lines(data):
    data.drop_duplicates(inplace = True)
    return data

######Na teoria, creio que não haja a necessidade de retirar os outlier, pois eles já podem ser uma anomalia(ou fraude) 