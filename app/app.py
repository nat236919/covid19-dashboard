"""
FILE: Covid19 Dashboard
DESCRIPTION: covid19 dashboard powered by Dash
AUTHOR: Nuttaphat Arunoprayoch
DATE: 01-DEC-2020
"""
# Import libs
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from models.covid19_model import Covid19Model
from utils.helper import DashHelper, DataFrameHelper


# Init modules
dataframe_helper = DataFrameHelper()
dash_helper = DashHelper()
covid19_model = Covid19Model()


# Init app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'COVID-19 DASHBOARD'


# Prepare data and Create graph
## Total data (dataframe and charts)
df_total = covid19_model.get_total()
df_total = dataframe_helper.clean_df_total(df_total)

fig_pie = px.pie(df_total, values='total', names='category')


## Current data (dataframe and charts)
df_current = covid19_model.get_current()
df_current = dataframe_helper.clean_df_current(df_current)

fig_choropleth = px.choropleth(df_current, locations='country_code_iso3', color='confirmed',
                hover_name='location')

fig_treemap = px.treemap(df_current, path=[px.Constant('world'), 'continent', 'location'], values='confirmed',
                color='active', hover_data=['country_code_iso3'], color_continuous_scale='RdBu',
                color_continuous_midpoint=np.average(df_current['active'], weights=df_current['confirmed']))

fig_bubble = px.scatter(df_current, x='deaths', y='active',
                 size='confirmed', color="continent", hover_name='location',
                 log_x=True, size_max=80)


# Create layout
app.layout = html.Div([
    # Head
    html.Div(children=[
        html.H1('COVID-19 DASHBOARD'),
        html.P('Dashbord for exploring covid-19 cases around the globe powered by DASH framework.'),
        dcc.Link(html.Button('API doc'), href='https://covid19.nuttaphat.com/'),
        dcc.Link(html.Button('GitHub'), href='https://github.com/nat236919/covid19-dashboard'),
        html.Div(id='container-button')
    ], style={'textAlign': 'center'}),

    # Tabs
    html.Div([
        dcc.Tabs(id="tabs", value='tab-choropleth', children=[
            dcc.Tab(label='World-Wide Infection (Map)',             value='tab-choropleth'),
            dcc.Tab(label='World-Wide Infection (Bubble Chart)',    value='tab-bubble'),
            dcc.Tab(label='Total Data - Pie Chart',                 value='tab-pie'),
            dcc.Tab(label='Total Data - Table',                     value='tab-table'),
        ]),
        html.Div(id='tabs-content')
    ], style={'margin': 'auto', 'width': '60%', 'padding': '10px'}),

    # Other Graphs
    dcc.Graph(
        id='treemap_graph',
        figure=fig_treemap
    )
])


## Callbacks
# Tabs
@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-choropleth':
        return html.Div([
            dcc.Graph(
                id='choropleth_graph',
                figure=fig_choropleth
            )
        ])
    elif tab == 'tab-bubble':
        return html.Div([
            dcc.Graph(
                id='bubble_graph',
                figure=fig_bubble
            )
        ])
    elif tab == 'tab-pie':
        return html.Div([
            dcc.Graph(
                id='pie_graph',
                figure=fig_pie
            )
        ])
    elif tab == 'tab-table':
        return html.Div([
            dash_helper.generate_table(df_total)
        ])


if __name__ == '__main__':
    """ Run this app with `python app.py` and
        Visit http://127.0.0.1:8080/ in your web browser.
    """
    app.run_server(host='0.0.0.0', port=8080, debug=False)
