#Import Benford
import random
from functionBenford import *
from calculateBenford import *
from loadData import file_selector
from loadData import import_data_find_column_os_data_open
from loadData import tolist
from generateGraph import *


#Import blib aux data

from tkinter.filedialog import askopenfilename
import os

#Import Interface
import streamlit as st
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px



############################### streamlit part 1 ###############################

lateral_bar = st.sidebar.empty()
st.title('''Benford Law's''')
#st.header('text')
#st.subheader('text')


############################### load data via os part 1 ###############################

filename = file_selector()
try: 
    os.makedirs(filename)
except OSError:
    if os.path.isdir(filename):
        st.write('Cannot access this entry')
        st.write("Try to change file in -- 'Select a file'")
        st.stop()
    #elif not pd.errors.ParserError:
     #   st.write('Caaa')
#except Exception as e:    
 #       errortype = e.message.split('.')[0].strip()                                
  #      if errortype == 'Error tokenizing data. C error': 
  #          st.stop()

############################ streamlit part 2 ###################################

st.sidebar.write('You selected `%s`' % filename)

############################ load data via os part 2 ###################################


data_and_column = import_data_find_column_os_data_open(filename) #Option 1 --> sep = ";", encoding='latin-1', on_bad_lines='skip'
#data_and_column = loadData.import_data_find_column_os(filename) #Option 2 
#benford_table = calculateBenford.calculate(data[0]) #Option 3

########################### data analysis --> df and keyscolumn ####################################


keyscolumn = data_and_column[1]
data = data_and_column[0]

########################### Streamlit ####################################

#streamlit() select column
keyscolumn_select = st.sidebar.selectbox("Selecione a coluna:", keyscolumn)

############################ Data Processing ###################################


specific_column = data[keyscolumn_select]
specific_column_transform_to_list = tolist(data, keyscolumn_select)

############################ Use Benford ###################################

benford_table = calculate(specific_column_transform_to_list)

#streamlit() select column
#carregar_dados = st.sidebar.checkbox('Carregar dados')

############################ Data Processing Aux Function ###################################


number = data_number(benford_table)
data_frequency = data_freq(benford_table)
data_frequency_percent = data_freq_perc(benford_table)
benford_frequency = benford_freq(benford_table)          
benford_frequency_percent = benford_freq_perc(benford_table)
difference_frequency = data_freq_difference(benford_table)
difference_frequency_percent = data_freq_difference_perc(benford_table)

######################### Graphics ######################################

#chart_bar = graph_bar_join(number, data_frequency_percent)
graph_bar_chart = st.empty()
graph_pie = st.empty()

data_graph = pd.DataFrame(benford_table)

######## bar chart ########
bar = px.bar(benford_table, x="n", y=["data_frequency_percent", "benford_frequency_percent"], barmode='group', height=500, width = 1000, title="Data Frequency Percent VS Benford Frequency Percent")
bar.update_yaxes(title_text="Frequency Percent")
bar.update_xaxes(title_text="Number")


#bar chart
#bar_f = px.bar(benford_table, x="n", y=["data_frequency_percent", "difference_frequency_percent"], barmode='group', height=500, width = 1000, title="Data Frequency Percent VS Benford Frequency Percent")
#bar_f.update_yaxes(title_text="Frequency Percent")
#bar_f.update_xaxes(title_text="Number")

######## line ########

lin = px.line(data_graph, x="n", y=["data_frequency_percent", "benford_frequency_percent"], height=500, width = 1000)

######## pie chart ########

pie1 = fig = px.pie(data_graph, values='data_frequency_percent')
pie2 = fig = px.pie(data_graph, values='benford_frequency_percent')
#st.plotly_chart(fig)
# st.dataframe(df) # if need to display dataframe
#fig = px.bar(trace1, x='number', y='data_frequency_percent')

try:
    graph_bar_chart = st.plotly_chart(bar)
    graph_bar_chart = st.plotly_chart(lin)
    graph_pie = st.plotly_chart(pie1)
    graph_pie = st.plotly_chart(pie2)
except Exception as e:
     st.stop(e) 
        

######################### Statistics ######################################
#scipy.stats.zscore(a, axis=0, ddof=0, nan_policy='propagate')






######################### Main ######################################


def main():
    
    print("| Benford's Law |")
    print(lin) 
main()
