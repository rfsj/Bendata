#import libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

#Conectando
import random
import benford.calculateBenford as calculateBenford
import data.loadData as loadData

data = loadData.import_csv_data()
#df = import_data_reader(2020, 1, 1,2020, 12, 3)
BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets = [BS], 
    meta_tags = [{'name':'viewport',
        'content':'width=device-width, initial-scale = 1.0'}])

app.layout = dbc.Container([

dbc.Row(
        dbc.Col(html.H1("benford",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

])

    

if __name__ == '__main__':
    app.run_server()