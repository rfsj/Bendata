import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename


def import_csv_data():
    csv_file_path = askopenfilename()
    df = pd.read_csv(csv_file_path)
    return df

#data = import_csv_data()

