import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from rowingconditions.resources.arkansas_data import last_30_days

df = last_30_days()

def create_dashboard(server):
    
    dash_app = dash.Dash(server=server,
                         routes_pathname_prefix='/dashapp/',
                         external_stylesheets=['/static/css/styles.css']
                         )

    trace1 = go.Scatter(x=df['date_time'],
                        y=df['gage_height'],
                        name='Gage Height',
                        mode='lines+markers',
                        yaxis='y1'
    )

    trace2 = go.Scatter(x=df['date_time'],
                        y=df['stream_flow'],
                        name='Stream Flow',
                        mode='lines+markers',
                        yaxis='y2'
    )

    data = [trace1, trace2]

    layout = go.Layout(title='Stream Flow and Gage Height Last 30 Days',
                        yaxis=dict(title='Gage Height (ft)'),
                        yaxis2=dict(title='Stream Flow (cfs)',
                                    overlaying='y',
                                    side='right')
    )

    dash_app.layout = html.Div(children=[
        html.H1(children='Arkansas River'),

        html.P(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(figure=go.Figure(data=data, layout=layout))
    ])

    return dash_app.server