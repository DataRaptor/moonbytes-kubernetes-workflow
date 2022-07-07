
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def generate_header(title: str, description: str):
    header = [
        html.Br(),
        html.Div([
            html.H1(
                children=title,
                className="two columns",
                style={"color": "#000", "width": "58%", "fontSize": "1.5em", "paddingLeft": "70px"}),
            dcc.Link(
                html.Button(
                    '🏠 Home',
                    id='personal-data',
                    className="five columns",
                    style={"backgroundColor": "#FFFFFF", "width": "auto", "fontSize": "17px", "margin": "2.5px", "border-radius": "20px"}),
                href='/'),
            dcc.Link(
                html.Button(
                    '👁️ Insights',
                    id='personal-data',
                    className="five columns",
                    style={"backgroundColor": "#FFFFFF", "width": "auto", "fontSize": "17px", "margin": "2.5px", "border-radius": "20px"}),
                href='/insights'),
            dcc.Link(
                html.Button(
                    '📦 Raw Signals',
                    id='personal-data',
                    className="five columns",
                    style={"backgroundColor": "#FFFFFF", "width": "auto", "fontSize": "17px", "margin": "2.5px", "border-radius": "20px"}),
                href='/raw_signals'),
            dcc.Link(
                html.Button(
                    '⚖️ Normalized Signals',
                    id='personal-data',
                    className="five columns",
                    style={"backgroundColor": "#FFFFFF", "width": "auto", "fontSize": "17px", "margin": "2.5px", "border-radius": "20px"}),
                href='/normalized_signals'),
        ], style={"paddingTop": "15px"}),
        html.Br(),
        html.Div(id='output-text', style={"color": "#FFFFFF"}),
        html.Br(),
        html.Div(
            id='personal-data-container-button',
            children='',
            style={"color": "#FFFFFF"}),
        html.Br(),
        html.Div(
            id='loading-container',
            children='',
            style={"background-color": "#FFFFFF"}),
        html.Div(
            id='fund-data-container-button',
            children=''),
        html.Br(),
        html.P(
            children=description,
            style={"margin": "40px", "font-size": "0.99em"}),
        html.Br()
    ]
    return header