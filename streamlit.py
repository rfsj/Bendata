from functionBenford import *
from calculateBenford import *
from loadData import *
from generateGraph import *
from clean import *
from stats import *

from statsmodels.stats.weightstats import ztest as ztest
import streamlit as st
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px

import scipy
import scipy.stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize
from scipy.stats import mannwhitneyu
# streamlit header

st.set_page_config(page_title="Newcomb-Benford Law", page_icon="📊", layout="centered")
lateral_bar = st.sidebar.empty()
st.sidebar.subheader('Upload the results of your experiment to see the importance of using the Newcomb-Benford Law')
st.title('''📊 Newcomb-Benford's Law''')
st.markdown("""---""")

# load data via os

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

# data clean

#data.drop_duplicates(inplace = True)
#data.dropna(subset = keyscolumn_select, inplace = True)

# negative protocol

option_negative_protocol = st.sidebar.expander("Negative Protocol")
with option_negative_protocol:
    radio_option_negative_protocol = st.sidebar.radio("What will be the negative protocol?", ('remove lines with negatives', 'remove negative from each cell', 'separate negative lines for analysis', 'no conditions'))

if radio_option_negative_protocol == "remove lines with negatives":
    if data[keyscolumn_select].dtypes == float64:
        data_remove = data.loc[data[keyscolumn_select] < 0]
        data = data.drop(data_remove.index)

elif radio_option_negative_protocol == "remove negative from each cell":
    data[keyscolumn_select] = data[keyscolumn_select].apply(lambda x: str(x).replace("-","")) #Quando precisar de um valor absoluto (Ex: resposta veio negativa mas o valor precisa ser positivo), usar o método abs(n).

elif radio_option_negative_protocol == "separate negative lines for analysis":
    if data[keyscolumn_select].dtypes == float64:
        data_remove = data.loc[data[keyscolumn_select] > 0] #
        data = data.drop(data_remove.index)
        data[keyscolumn_select] = data[keyscolumn_select].apply(lambda x: str(x).replace("-",""))

# Use Benford

specific_column_transform_to_list = tolist(data, keyscolumn_select) #transform column
benford_table = calculate(specific_column_transform_to_list)

# Data Processing Aux Function

#number = data_number(benford_table)
#data_frequency = data_freq(benford_table)
#data_frequency_percent = data_freq_perc(benford_table)
#benford_frequency = benford_freq(benford_table)
#benford_frequency_percent = benford_freq_perc(benford_table)
#difference_frequency = data_freq_difference(benford_table)
#difference_frequency_percent = data_freq_difference_perc(benford_table)



data_calculate = pd.DataFrame(benford_table)
length = len(data[keyscolumn_select])
# Graphics

graph_bar_chart = st.empty()
graph_pie = st.empty()

# bar chart #

bar = px.bar(benford_table, x="n", y=["data_frequency_percent", "benford_frequency_percent"], barmode='group', height=500, width = 1000, title="This graph shows the difference between the percentage of the sample and the percentage compared")
bar.update_yaxes(title_text="Frequency Percent")
bar.update_xaxes(title_text="Number")

# line chart #

lin = px.line(data_calculate, x="n", y=["data_frequency_percent", "benford_frequency_percent"], height=500, width = 1000)
lin.update_yaxes(title_text="Frequency Percent")
lin.update_xaxes(title_text="Number")

try:
    graph_bar_chart = st.plotly_chart(bar)
    graph_bar_chart = st.plotly_chart(lin)
except Exception as e:
     st.stop(e)

# Statistics

data_frequency = data_freq(benford_table) #aux function
data_frequency_percent = data_freq_perc(benford_table) #aux function
benford_frequency =  benford_freq(benford_table) #aux function
benford_frequency_percent = benford_freq_perc(benford_table) #aux function
#zscore
z = pd.DataFrame(zscore(length, data_frequency_percent, benford_frequency_percent))
#chisquare
chi = chi_square(data_frequency, benford_frequency)
pd_chi = pd.DataFrame(chi[0])
sum_chi = chi[1]
#mad
m_a_d = mad(data_frequency_percent, benford_frequency_percent)


# See all

st.markdown("""---""")

expander = st.expander("See all benford data")

with expander :
    st.markdown("""***📑Details***""")
    data_len = st.write('- Name Column:', keyscolumn_select)
    data_len = st.write('- Length:', length)
    data_len = st.write('- Type:', data[keyscolumn_select].dtypes)
    st.markdown("""
    ***📑Sample percentage***
    - Data frequency
    - Data frequency percent
    ---
    """)
    data_frequency = st.write(data_calculate.iloc[:, [0,1,2]])
    st.markdown("""
    ---
    ***📑Newcomb-Benford percentage***
    - Benford frequency
    - Benford frequency percent
    ---
    """)
    benford_frequency = st.write(data_calculate.iloc[:, [0,3,4]])
    st.markdown( """
    ---
    ***📑Difference between sample***
    - benford frequency
    - benford frequency percent
    ---
    """)
    difference_frequency = st.write(data_calculate.iloc[:, [0,5,6]])
########################################################################
    st.markdown( """
    ---
    ***📑Statistical Test***
    * ##### Zscore
    """)

    st.markdown( """
        The Z-statistic is used to test whether the actual proportion for a specific
    digit differs significantly (in the statistical sense) from the expectation of Benford’s
    Law. The formula takes into account the absolute magnitude of the difference, the
    number of records, and the expected proportion. We usually use a significance level
    of 5 percent which has a critical value of 1.96(Negrini, 2012).
    """)
    st.markdown("""
    | Comparative values:   |                |
    |-----------------------|----------------|
    | Accepted                | Below 1.96 |
    | Rejected              | Above 1.96 |
    &nbsp;
        """)   
    st.info("However, with the excess power problem, we know that as the data set becomes larger, the Z-statistic tolerates smaller and smaller deviations.")
    zwrite = st.write(z.iloc[:, [0,1]])
########################################################################
    st.markdown("""
    ---
    * ##### Chi Square Test
    """)
    st.markdown("""
    The chi-square test is used to compare a set of actual results with the expected results. The expected result is that  data conforms to Benford’s Law. The null hypothesis is that the digits conform to Benford’s Law(Negrini, 2012).
    """)    
    st.markdown("""
    | Comparative values:   |                |
    |-----------------------|----------------|
    | Accepted              | 0.000 to 15,51 |
    | Rejected              | Above 15,51    |
    &nbsp;
        """)       
    
    st.info("The chi-square test unfortunately also suffers from the excess power problem in that when the number of records becomes large, the calculated chi-square will almost always be higher than the critical value, leading us to conclude that the data does not conform to Benford’s Law. This problem starts being noticeable for data sets with more than 5,000 records(Negrini, 2012). ")
    
    chiwrite = st.write(pd_chi.iloc[:, [0,1]])
    help = st.write("Total:")
    chisumwrite = st.write(sum_chi)
    st.warning("This means that if the calculated chi-square value exceeds 15,51, the null hypothesis of conformity must be rejected and we would conclude that the data does not conform to Benford’s Law(Negrini, 2012). ")
########################################################################
    st.markdown( """
    ---
    * ##### Mean absolute deviation
    """)
    st.markdown( """

    This is a measure of conformity to Benford’s Law that takes into account the expected proportions and the actual proportions for each digit but ignores the number of records, N. This test is the preferred measure of conformity and it is based on the average absolute deviation of the actual proportions from the Benford proportions. A high MAD signals a low level of conformity to Benford. This book includes a table of MAD critical values based on a sample of real-world data sets(Negrini, 2012).
    """)
    
    st.markdown("""
| Comparative values:   |                |
|-----------------------|----------------|
| Close                 | 0.000 to 0.006 |
| Acceptable            | 0.006 to 0.012 |
| Marginally Acceptable | 0.012 to 0.015 |
| Nonconformity         | Above 0.015    |
        """)
    st.markdown( """
    Total:
    """)         
    madwrite = st.write(m_a_d)

# Main
@st.cache
def main():
    print("| Benford's Law |")
    print(z)
    print(chi)
    print(m_a_d)
main()

