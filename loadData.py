import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas_datareader.data as web
import datetime

def import_csv_data():
    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path)
    return df

#teste datareader
def import_data_reader(yyyy,m,d,zzzz,n,e):
    start = datetime.datetime(yyyy,m,d)
    end = datetime.datetime(zzzz,n,e)
    df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
                    'stooq', start=start, end=end)
    df = df.stack().reset_index()
    return df[:15]

#dados = import_data_reader(2020, 1, 1,2020, 12, 3)

#data = import_csv_data()

