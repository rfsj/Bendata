#import libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

#Conectando
from loadData import import_csv_data
tudo = import_csv_data()
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(tudo)
])

if __name__ == '__main__':
    app.run_server()