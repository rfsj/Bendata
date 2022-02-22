import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilename
#import pandas_datareader.data as web
import datetime
import tkinter as tk
import os
import streamlit as st
#import full database
def import_csv_data():
    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path, sep = ",") #sep usando quando a separação é em ;
    return df

#import data and columns by askopenfilename
def import_data_find_column():
    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path, sep = ",") #sep usando quando a separação é em ;
    column = df.keys()
    col = []
    for n in column:
        col.append(n)
    return df, col

#import data and columns by os
def import_data_find_column_os(filename):
    csv_file_path = filename
    df = pd.read_csv(csv_file_path, sep = ",") #sep usando quando a separação é em ;
    column = df.keys()
    col = []
    for n in column:
        col.append(n)
    return df, col

#dados abertos
def import_data_find_column_os_data_open(filename):
    csv_file_path = filename
    df = pd.read_csv(csv_file_path, sep = ";", encoding='latin-1', on_bad_lines='skip') #sep usando quando a separação é em ;
    column = df.keys()
    col = []
    for n in column:
        col.append(n)
    return df, col


#turn into list separade
def tolist(data, keyscolumn_select):
    data_list = data[keyscolumn_select].astype(str).tolist() 
    return data_list


#import specific column
def import_by_column():
    csv_file_path = askopenfilename()
    data_import = pd.read_csv(csv_file_path, sep = ",") #separators (, and ;)
    name_column = input("digite o nome da coluna: ")
    column = data_import[name_column].astype(str).tolist() #transform into a list built into the function
    return column


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

#dialect.delimiter











#teste datareader base da dados para testar futuramente
def import_data_reader(yyyy,m,d,zzzz,n,e):
    start = datetime.datetime(yyyy,m,d)
    end = datetime.datetime(zzzz,n,e)
    df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
                    'stooq', start=start, end=end)
    df = df.stack().reset_index()
    return df[:15]
#dados = import_data_reader(2020, 1, 1,2020, 12, 3)


