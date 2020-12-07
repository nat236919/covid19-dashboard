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
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from models.covid19_model import Covid19Model
from utils.helper import DataFrameHelper, DashHelper

# Init app and modules
dataframe_helper = DataFrameHelper()
dash_helper = DashHelper()
covid19_model = Covid19Model()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Prepare data and Create graph
# Total data
df_total = covid19_model.get_total()
df_total = dataframe_helper.clean_df_total(df_total)
fig_pie = px.pie(df_total, values='total', names='category')


# Current data
df_current = covid19_model.get_current()
df_current = dataframe_helper.clean_df_current(df_current)
fig_scatter = px.scatter(df_current, x='deaths', y='active',
                 size='confirmed', color="continent", hover_name='location',
                 log_x=True, size_max=80)
fig_bar = px.bar(df_current, x='continent', y='confirmed', color='location')


# Create layout
app.layout = html.Div([
    # Head
    html.Div(children=[
        html.H1('COVID-19 DASHBOARD'),
        html.P('Dashbord for exploring covid-19 cases around the globe powered by DASH framework.'),
        html.Button('API doc', id='api_btn'),
        html.Button('GitHub', id='github_btn'),
    ], style={'textAlign': 'center'}),

    # Tabs
    html.Div([
        dcc.Tabs(id="tabs", value='tab-table', children=[
            dcc.Tab(label='Total Data - Table', value='tab-table'),
            dcc.Tab(label='Total Data - Pie Chart', value='tab-pie')
        ]),
        html.Div(id='tabs-content')
    ], style={'margin': 'auto', 'width': '60%', 'padding': '10px'}),

    # Other Graphs
    dcc.Graph(
        id='Global Data',
        figure=fig_scatter
    ),
    dcc.Graph(
        id='Global Data 2',
        figure=fig_bar
    )
])


# Callbacks
@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-table':
        return html.Div([
            dash_helper.generate_table(df_total)
        ])
    elif tab == 'tab-pie':
        return html.Div([
            dcc.Graph(
                id='Total Data',
                figure=fig_pie
            )
        ])


if __name__ == '__main__':
    """ Run this app with `python app.py` and
        Visit http://127.0.0.1:8050/ in your web browser.
    """
    app.run_server(debug=True)
