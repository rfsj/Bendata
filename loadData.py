import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas_datareader.data as web
import datetime


#Abrir aquivo com caixa de seleção(simples)
def import_csv_data():
    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path)
    return df

#teste datareader base da dados para testar futuramente
def import_data_reader(yyyy,m,d,zzzz,n,e):
    start = datetime.datetime(yyyy,m,d)
    end = datetime.datetime(zzzz,n,e)
    df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
                    'stooq', start=start, end=end)
    df = df.stack().reset_index()
    return df[:15]
    
#mais complexo
#def load_data(var):
#   csv_file_path = askopenfilename()
 #  df = pd.read_csv(csv_file_path)
 #  data=df[var]
 #  return df,data

#teste de resultado
#dados = load_data()
#print(dados[1].describe())
#print(dados.describe().transpose)
#dados.info()
#dados.isnull().sum()
#dados = import_data_reader(2020, 1, 1,2020, 12, 3)
#data = load_data()
#print(data[1].describe())

