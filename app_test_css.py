from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(className = 'top_metrics')

if __name__ == '__main__':
    app.run_server(debug=True)