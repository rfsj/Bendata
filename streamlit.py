import streamlit as st
import plotly.graph_objs as go
import random
from benford.functionBenford import *
from benford import calculateBenford
from data import loadData
from graphic.generateGraph import *
from tkinter import *
from tkinter.filedialog import askopenfilename
import streamlit as st
import os

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

lateral_bar = st.sidebar.empty()
filename = file_selector()
st.sidebar.write('You selected `%s`' % filename)

data_and_column = loadData.import_data_find_column_os(filename)
#benford_table = calculateBenford.calculate(data[0])
keyscolumn = data_and_column[1]
data = data_and_column[0]





keyscolumn_select = st.sidebar.selectbox("Selecione a coluna:", keyscolumn)

specific_column = data[keyscolumn_select]
benford_table = calculateBenford.calculate(specific_column)

carregar_dados = st.sidebar.checkbox('Carregar dados')

number = data_number(benford_table)
data_frequency = data_freq(benford_table)
data_frequency_percent = data_freq_perc(benford_table)
benford_frequency = benford_freq(benford_table)          
benford_frequency_percent = benford_freq_perc(benford_table)
difference_frequency = data_freq_difference(benford_table)
difference_frequency_percent = data_freq_difference_perc(benford_table)

graph_bar(number, data_frequency_percent)
graph_bar_benford(number, benford_frequency_percent)



def main():
    
    print("| Benford's Law |")
        
main()
