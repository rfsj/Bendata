import pandas as pd

# force NaN in df
def force_to_numeric(data_clean, keyscolumn_select): #???
    data_clean = pd.to_numeric(data_clean[keyscolumn_select], errors="coerce")
    return data_clean


# negative protocol
def remove_lines_with_negatives(data, keyscolumn_select):
    data_loc_negative = data.loc[(data[keyscolumn_select][0] != "-")]
    data_without_negative = data.drop(data_loc_negative.index)
    return data_without_negative

def remove_negative_from_each_cell(data, keyscolumn_select): #pop[0]
    #data_loc_negative = data.loc[(data[keyscolumn_select][0] != "-")]
    ###########
    #Indices=[x for x in df.index if #as condições que vc quer#]
    #df.drop(índices)
    #########
    #como mexe com a celula dos numeros???????? tipo tenho que pegar uma celular int -543 e transformar em 543
    return 

def separate_negative_lines_for_analysis(data, keyscolumn_select):
    data_remove = data.loc[(data[keyscolumn_select][0] != "-")]
    return data_remove

#remove null lines
def remove_null_lines(data, keyscolumn_select):
    data.dropna(axis = 0, subset = keyscolumn_select) # duvida dropando linhas, onde na coluna selecionada existe NaN(Qm sabe usar uma comparação com o nome ou numero do documento para verificar se há)
    return data

#remove duplicate lines
def remove_duplicate_lines(data):
    data.drop_duplicates()
    return data

######Na teoria, creio que não haja a necessidade de retirar os outlier, pois eles já podem ser uma anomalia(ou fraude) 