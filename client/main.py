
import logging
import pandas as pd
from typing import Any
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px 
import plotly.graph_objects as go 
from dash import html, dcc
from flask_caching import Cache
from dash.exceptions import PreventUpdate
from src import api
from src.transformers import (
    get_collection_ids
)

class AppState():

    def __init__(self):
        self.data = {}

    def get(self, key):
        if key not in self.data:
            raise Exception("Key: {} DNE in AppState self.data".format(key))
        return self.data[key]

    def set(self, key, data):
        self.data[key] = data

state = AppState()

CACHE_DIR = 'temp'
TIMEOUT = 60

template = 'ggplot2'

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    dbc.themes.COSMO
]

logging.basicConfig(
    level=logging.INFO)

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True)

app.config.suppress_callback_exceptions = True
app.title = "Gradient"
app.description = "Development Dashboard"

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

header = html.Div(
    children=[
        html.Div(children=[
            html.H1(
                children='Pure Alpha',
                style={
                    'color': '#000',
                    'fontSize': '2.6em',
                    'display': 'inline'
                }
            ),
        ]),
        html.H3(children='A Gradient Admin Product',
                style={'color': '#000', 'fontSize': '1.4em'}),
    ],
    style={
        'marginTop': 50,
        'textAlign': 'center'
    }
)

collections = get_collection_ids(api.get_magic_eden_collections())
measurements = [
    "listed_count",
    "price_floor"
]
intervals = [
    "1s",
    "1m",
    "10m",
    "60m",
    "1d"
]

layout = html.Div(
    children=[
        header,
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(children=[
                    html.H2("", style={'fontSize': '1.3em'}),
                    dcc.Dropdown(
                        collections, 
                        [ collections[0] ], 
                        id="collection-selection",
                        multi=True,
                        style={'height': '15%', "width": "100%"}),
                    html.Br(),
                    html.H2("Measurement", style={'fontSize': '1.3em'}),
                    dcc.Dropdown(
                        measurements, 
                        [ measurements[0] ], 
                        id="measurement-selection",
                        multi=True,
                        style={'height': '15%', "width": "100%"}),
                    html.Br(),
                    html.H2("Interval", style={'fontSize': '1.3em'}),
                    dcc.Dropdown(
                        intervals, 
                        intervals[0], 
                        id="interval-selection",
                        multi=False,
                        style={'height': '15%', "width": "100%"}),
                    html.Br(),
                    dcc.Checklist(
                        ["Normalize"],
                        [],
                        id="options-selection"
                    ),
                ],
                width=4),
                dbc.Col(
                    html.Div(children=[
                        html.Div(id='body-div'),
                        html.Div(id='collection-name')
                    ]),
                    width=8
                ),
            ]
        ),
        
            
        
        html.Br(),
        # html.Button('Execute', id='show-secret'),
    ],
    style={
        'marginLeft': '5%',
        'marginRight': '5%'
        # 'overflow': 'scroll',
        # 'marginTop': '0px',
        # 'textAlign': 'center',
    }
)


@app.callback(
    Output('collection-name', 'children'),
    Input('collection-selection', 'value'),
    Input('measurement-selection', 'value'),
    Input('interval-selection', 'value'),
    Input('options-selection', 'value')
)
def update_collection_selection(
    collection_ids: list,
    measurements: list,
    interval: str,
    options: list):

    if not isinstance(collection_ids, list):
        collection_ids = [collection_ids]
    if not isinstance(measurements, list):
        measurements = [measurements]
    if not isinstance(options, list):
        options = [options]

    df = api.get_df(
        dataset="magic_eden",
        model="markets",
        ids=collection_ids,
        measurements=measurements
    )
    html_elem = None



    if not df.empty:
        df.set_index("_time", inplace=True)
        df = pd.DataFrame(df[["_value", "_measurement", "collection"]])

        fig = go.Figure()
        for measurement in measurements:
            for collection in collections:
                query_df = df[df["_measurement"] == measurement]
                query_df = df[df["collection"] == collection]
                query_df.drop(["_measurement", "collection"], axis=1, inplace=True)
                if "Normalize" in options:
                    query_df = (query_df-query_df.mean()) / query_df.std()
                fig_name: str = None
                if len(collections) > 1:
                    fig_name = "{} - {}".format(
                        collection,
                        measurement)
                else:
                    fig_name = measurement
                fig.add_trace(
                    go.Scatter(
                        x=query_df.index,
                        y=query_df["_value"],
                        mode='lines',
                        line=dict(width=1),
                        name=fig_name))
        fig.update_layout(title="{} - {}".format(
            "["+", ".join(collection_ids)+"]",
            "["+", ".join(measurements)+"]"
        ))
        fig.update_layout(template=template)
        html_elem = dcc.Graph(
            id="graph",
            figure=fig)
    else:
        return html.H1("No data available for collections: {} and measurements: {}".format(
            collection_ids,
            measurements))

    return html_elem


@app.callback(
    Output(component_id='body-div', component_property='children'),
    Input(component_id='show-secret', component_property='n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return "Elephants are the only animal that can't jump"

@app.callback(
    Output('cytoscape', 'responsive'),
    [Input('toggle-button', 'n_clicks')])
def toggle_responsive(n_clicks):
    n_clicks = 2 if n_clicks is None else n_clicks
    toggle_on = n_clicks % 2 == 0
    return toggle_on


@app.callback(
    Output('toggle-text', 'children'),
    [Input('cytoscape', 'responsive')])
def update_toggle_text(responsive):
    return '\t' + 'Responsive ' + ('On' if responsive else 'Off')


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layout

@server.route("/")
def personal_page():
    return app.index()

if __name__ == '__main__':
    print('💫 [spectral-technologies] trading:observer started')
    app.run_server(
        host='0.0.0.0',
        port=8080,
        debug=True,
        use_reloader=True)
