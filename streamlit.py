###Import Benford
#import random
from functionBenford import *
from calculateBenford import *
from loadData import *
from generateGraph import *

###Import blib aux data
#from tkinter import *
#from tkinter.filedialog import askopenfilename
#import os

###Import Interface
import streamlit as st
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px

############################### streamlit header ###############################

st.set_page_config(page_title="Newcomb-Benford Law", page_icon="📊", layout="centered")
lateral_bar = st.sidebar.empty()
st.sidebar.subheader('Upload the results of your experiment to see the importance of using the Newcomb-Benford Law')
st.title('''📊 Newcomb-Benford's Law''')
st.markdown("""---""")

############################### load data via os ###############################

try:
    csv_file_path = st.sidebar.file_uploader("📂Upload file", type='csv')
    if csv_file_path is None:
        st.stop()
        raise ValueError('Represents a hidden bug, do not catch this')
    elif csv_file_path is not None:
        st.sidebar.write('You selected `%s`' % csv_file_path)
        data_and_column = streamlit_upload(csv_file_path) # function
        keyscolumn = data_and_column[1] #save columns
        data = data_and_column[0] #save data
        keyscolumn_select = st.sidebar.selectbox("Select column:", keyscolumn) #select column
        
except Exception as error:
    print('Caught this error: ' + repr(error))
    
############################ data clean ###################################
data_clean = data.info()


############################ Use Benford ###################################

specific_column = data[keyscolumn_select] #get columns
specific_column_transform_to_list = tolist(data, keyscolumn_select) #transform column
benford_table = calculate(specific_column_transform_to_list)


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
bar = px.bar(benford_table, x="n", y=["data_frequency_percent", "benford_frequency_percent"], barmode='group', height=500, width = 1000, title="This graph shows the difference between the percentage of the sample and the percentage compared")
bar.update_yaxes(title_text="Frequency Percent")
bar.update_xaxes(title_text="Number")

######## line chart ########

lin = px.line(data_graph, x="n", y=["data_frequency_percent", "benford_frequency_percent"], height=500, width = 1000)
lin.update_yaxes(title_text="Frequency Percent")
lin.update_xaxes(title_text="Number")

try:
    graph_bar_chart = st.plotly_chart(bar)
    graph_bar_chart = st.plotly_chart(lin)
except Exception as e:
     st.stop(e) 


########################See all#############################

st.markdown("""---""")

expander = st.expander("See all benford data")  

with expander :
    st.markdown("""
    ***📑Sample percentage***
    - Data frequency
    - Data frequency percent
    ---
    """)
    data_frequency = st.write(data_graph.iloc[:, [0,1,2]])
    st.markdown("""
    ---
    ***📑Newcomb-Benford percentage***
    - Benford frequency
    - Benford frequency percent
    ---
    """)
    data_frequency = st.write(data_graph.iloc[:, [0,3,4]])
    st.markdown( """
    ---
    ***📑Difference between sample***
    - benford frequency
    - benford frequency percent
    ---
    """)
    data_frequency = st.write(data_graph.iloc[:, [0,5,6]])    

######################### Statistics ######################################


#scipy.stats.zscore(a, axis=0, ddof=0, nan_policy='propagate')
#scipy.stats.chisquare(f_obs, f_exp=None, ddof=0, axis=0)
#scipy.stats.median_abs_deviation(x, axis=0, center=<function median>, scale=1.0, nan_policy='propagate')

######################### Main ######################################


def main():
    
    print("| Benford's Law |")
    print(lin) 
    print(data_clean)
    
main()

