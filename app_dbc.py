import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
   html.Div(
        children = [

            dbc.Row(
                     dbc.Col("Single Column")
                )

            ,dbc.Row(
                      [
                        dbc.Col("Column 1")
                        ,dbc.Col("Column 2")
                        ,dbc.Col("Column 3")

                      ]

                )

        ]


    )
)

if __name__ == "__main__":
    app.run_server()