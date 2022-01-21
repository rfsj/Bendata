Benford law's

reference:
https://www.codedrome.com/benfords-law-in-python/ --> function calculate

lateral_bar = st.sidebar.empty()
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
