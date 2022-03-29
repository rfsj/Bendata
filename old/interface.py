#import random
#from benford.functionBenford import *
#from benford import calculateBenford
#from data import loadData
#from graphic.generateGraph import *

#import full database
##data = loadData.import_csv_data()

#import specific column
#data = loadData.import_by_column()

#use the first digit function(benford) --> dictionary with {"n","data_frequency","data_frequency_percent","benford_frequency","benford_frequency_percent","difference_frequency","difference_frequency_percent"}
#benford_table = calculateBenford.calculate(data)

#extract information with aux fuctions
#number = data_number(benford_table)
#data_frequency = data_freq(benford_table)
#data_frequency_percent = data_freq_perc(benford_table)
#benford_frequency = benford_freq(benford_table)          
#benford_frequency_percent = benford_freq_perc(benford_table)
#difference_frequency = data_freq_difference(benford_table)
#difference_frequency_percent = data_freq_difference_perc(benford_table)


#def main():

   # print("| Benford's Law |")

    #graph_bar(number, data_frequency_percent)
    #graph_bar_benford(number, benford_frequency_percent)

#main()

col1,col2 = st.columns(2)
with col1 :
    graph_bar_chart = st.plotly_chart(bar)
with col2 :
    graph_bar_chart = st.plotly_chart(lin)

############################ load data via os part 2 ###################################


 #Option 1 --> sep = ";", encoding='latin-1', on_bad_lines='skip'
#data_and_column = loadData.import_data_find_column_os(filename) #Option 2 
#benford_table = calculateBenford.calculate(data[0]) #Option 3
    
class loadData:
    def __init__(self):
        self.sep = ','
        self.df = None
        self.col = []
        self.keyscolumn_select = None
        self.data_list = None

    def check_separator(self):
            sep_dict = {'comma': ',', 'semicolon': ';', 'space': ' ','tab':'\t'}
            sep = st.selectbox('Select the separator used in the file', list(sep_dict.keys()))
            if sep:
                self.separator = sep_dict[sep]

    def file_selector(folder_path='.'):
        filenames = os.listdir(folder_path)
        selected_filename = st.sidebar.selectbox('Select a file', filenames)
        return os.path.join(folder_path, selected_filename)

    def streamlit_upload(csv_file_path, self):
        self.df = pd.read_csv(csv_file_path, sep = self.separator, encoding='latin-1', on_bad_lines='skip') #sep usando quando a separação é em ;
        column = self.df.keys()
        for n in column:
            self.col.append(n)
        self.keyscolumn_select = st.sidebar.selectbox("Select column:", self.col) #select column
        

    #turn into list separade
    def tolist(keyscolumn_select,self):
        self.data_list = self.df[self.keyscolumn_select].astype(str).tolist() 
        