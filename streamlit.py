import streamlit as st
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px
import random
from benford.functionBenford import *
from benford import calculateBenford
from data import loadData
from graphic.generateGraph import *
from tkinter import *
from tkinter.filedialog import askopenfilename
import streamlit as st
import os

#streamlit() sidebar empty
lateral_bar = st.sidebar.empty()

#streamlit() text center element 
st.title('''Benford Law's''')

st.header('data')

st.subheader('graphic view')

#load data via os part 1
filename = loadData.file_selector()

#streamlit()text sidebar
st.sidebar.write('You selected `%s`' % filename)

#load data via os part 2
data_and_column = loadData.import_data_find_column_os(filename)

#############benford_table = calculateBenford.calculate(data[0])

#df and keyscolumn
keyscolumn = data_and_column[1]
data = data_and_column[0]

#streamlit() select column
keyscolumn_select = st.sidebar.selectbox("Selecione a coluna:", keyscolumn)

#data processing
specific_column = data[keyscolumn_select]
specific_column_transform_to_list = loadData.tolist(data, keyscolumn_select)

#use benford
benford_table = calculateBenford.calculate(specific_column_transform_to_list)

#streamlit() select column
carregar_dados = st.sidebar.checkbox('Carregar dados')

#data processing aux function
number = data_number(benford_table)
data_frequency = data_freq(benford_table)
data_frequency_percent = data_freq_perc(benford_table)
benford_frequency = benford_freq(benford_table)          
benford_frequency_percent = benford_freq_perc(benford_table)
difference_frequency = data_freq_difference(benford_table)
difference_frequency_percent = data_freq_difference_perc(benford_table)




#graphics
graph_bara = st.empty()




#fig = px.bar(trace1, x='number', y='data_frequency_percent')

try:
    graph_bara = st.bar_chart(data_frequency_percent)
except Exception as e:
    st.error(e)


def main():
    
    print("| Benford's Law |")
    #print(graph_bara) 
    print(data_frequency_percent)
    print(data_frequency)
    print(number)
main()
