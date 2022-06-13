from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
# import pyodbc
# import setting

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

data = {
	
	'PNM_KP' : 1824
	,'PNM_ULAMM' : 5917
	,'PNM_MEKAAR' : 51263
	,'PNM_PERSERO' : 59004
	,'PNM_IM' : 67
	,'PNM_VC' : 81
	,'PNM_VS' : 40 
	,'PNM_MUM' : 141
	,'PNM_MMI' : 148
	,'PNM_MNM' : 68
	,'PNM_MBM' : 70
	,'PNM_MTM' : 47
	,'PNM_MPM' : 74
	,'PNM_MDM' : 50
	,'PNM_SUBSIDIARY' : 786
	,'TOTAL' : 59790
}


data_holding = {
	
	'company_holding' : ['Kantor Pusat' ,'UlaMM' ,'Mekaar']
	,'value_holding' : [1824, 5917, 59004]

}

data_afiliasi = {
	
	'company_afiliasi' : ['IM','VC','VS','MUM','MMI','MNM','MBM','MTM','MPM','MDM']
	,'value_afiliasi' : [67, 81, 40, 141, 148, 68, 70, 47, 74, 50]


}

data_holding = pd.DataFrame(data=data_holding)
data_afiliasi = pd.DataFrame(data=data_afiliasi)

print(data_holding)


fig_holding = px.bar(data_holding, x='company_holding', y= 'value_holding', labels = {'company_holding' : 'Karyawan', 'value_holding' : 'Jumlah'})

fig_afiliasi = px.bar(data_afiliasi
					  ,x='company_afiliasi'
					  ,y='value_afiliasi'
					  ,labels = {'company_afiliasi' : 'Perusahaan', 'value_afiliasi' : 'Jumlah'}
					  ,color='company_afiliasi'
					  ,color_discrete_map={'IM' : 'red'}
					  )

app = Dash(external_stylesheets=[dbc.themes.FLATLY])

# app.layout = html.Div([
#
# 		# dcc.Graph(figure = fig_holding)
# 		# dcc.Graph(figure = fig_afiliasi)
#
# 		dbc.Container(
#
#
# 				dbc.Row(
# 						 [
# 			                # dbc.Col(dcc.Graph(figure = fig_holding), width=6)
# 			                # ,dbc.Col(dbc.Table.from_dataframe(data_holding, striped=True, bordered=True, hover=True), width=6, align='center')
#
#
# 							 dbc.Col(
#
# 								dbc.Card(
#
# 									[
# 										dbc.CardHeader("Karyawan PNM Group", style={'text-align' : 'center'})
# 										,dbc.CardBody(
# 											[
# 												dcc.Graph(figure = fig_holding)
# 												,dbc.Table.from_dataframe(data_holding, striped=True, bordered=True, hover=True)
#
# 											]
# 										)
# 									]
# 								)
# 								 ,width=6
# 							 )
# 							 ,dbc.Col(
#
# 								dbc.Card(
#
# 									[
# 										dbc.CardHeader("Karyawan PNM Afiliasi", style={'text-align' : 'center'})
# 										,dbc.CardBody(
# 											[
# 												dcc.Graph(figure = fig_afiliasi)
# 												,dbc.Table.from_dataframe(data_afiliasi, striped=True, bordered=True, hover=True)
#
# 											]
# 										)
# 									]
# 								)
# 							 	,width=6
# 						 )
#            				 ]
#
#
# 					)
#
#
# 		        )
#
# 		]
#
# )

sidebar = html.Div(
    [
        html.H2("HRIS", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content_children = dbc.Container(
                [
                    dbc.Row(
                        dbc.CardGroup(
                            [
                                dbc.Card([
                                    dbc.CardHeader("Karyawan PNM Kantor Pusat", className="card-title")
                                    ,dbc.CardBody(
                                        [
                                            #html.H5("Karyawan Kantor Pusat", className="card-title"),
                                            html.P(
                                              data['PNM_KP'],
                                                className="card-text",
                                            )
                                        ]
                                    )

                                ]

                                )
                                ,dbc.Card([
                                    dbc.CardHeader("Karyawan PNM Cabang UlaMM", className="card-title")
                                    ,dbc.CardBody(
                                        [
                                            #html.H5("Karyawan Cabang UlaMM", className="card-title"),
                                            html.P(
                                              data['PNM_ULAMM'],
                                                className="card-text",
                                            )
                                        ]
                                    )
                                ]

                                )
                                ,dbc.Card([
                                    dbc.CardHeader("Karyawan Cabang Mekaar", className="card-title")
                                    ,dbc.CardBody(
                                        [
                                           # html.H5("Karyawan Cabang Mekaar", className="card-title"),
                                            html.P(
                                                data['PNM_MEKAAR'],
                                                className="card-text",
                                            )
                                        ]
                                    )

                                ]

                            )
                            ]
                        )
                    )
                    ,dbc.Row(
                        [
                            dbc.Col(
                                [
                                        #dbc.CardHeader("Karyawan PNM Group", style={'text-align' : 'center'})
										dbc.CardBody(
											[
												dcc.Graph(figure = fig_holding)
												#,dbc.Table.from_dataframe(data_holding, striped=True, bordered=True, hover=True)
 											]
 										)
                                ]
                            )

                        ]
                    )
                ]



)


content = html.Div(id="page-content", style=CONTENT_STYLE
                        ,children=[content_children]

           			)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == '__main__':
    app.run_server(debug=True)

# df = pd.read_csv("daily_pnm_group.csv")

# print(df)