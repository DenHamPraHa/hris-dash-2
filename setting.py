import pyodbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.11.102;'
                      'Database=rahmad;'
                      'Trusted_Connection=no;'
                      'UID=sdm_hris;'
                      'PWD=@qu4GaloN...--...;'
                      )

def get_data(date):

    sql_query = f"""
                    SELECT TOP 1 PNM_KP, PNM_ULAMM, PNM_MEKAAR
                    FROM TDAILYPNMGROUP
                    WHERE CONVERT(DATE,CREATE_AT) = '{date}'
                    ORDER BY CREATE_AT DESC
                """
    read_query = pd.read_sql_query(sql_query,conn)
    #read_query = conn.execute(sql_query)

    return read_query


data = get_data('2020-06-06')

print(data)

# app = Dash(__name__)
#
# data = get_data('2020-06-06')
#
# graph = px.bar(data,x=['PNM_KP', 'PNM_ULAMM', 'PNM_MEKAAR'] , y=[data['PNM_KP'],data['PNM_ULAMM'], data['PNM_MEKAAR']])
#
# app.layout = html.Div(
#
#                dcc.Graph(figure=graph)
#
#
#             )
#
# if __name__ == '__main__':
#     app.run_server(debug=True)







