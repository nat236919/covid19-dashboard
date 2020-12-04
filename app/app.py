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
import plotly.express as px
import pandas as pd

from utils.helper import DataFrameHelper
from models.covid19_model import Covid19Model


# Init app and modules
dataframe_helper = DataFrameHelper()
covid19_model = Covid19Model()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Prepare data and Create graph
df = covid19_model.get_current()
df = dataframe_helper.clean_df_current(df)
fig_scatter = px.scatter(df, x='deaths', y='active',
                 size='confirmed', color="continent", hover_name='location',
                 log_x=True, size_max=80)
fig_bar = px.bar(df, x='continent', y='confirmed', color='location')


# Create layout
app.layout = html.Div([
    html.H1(children='COVID-19 DASHBOARD'),
    html.Div(children='''
        Dashbord for exploring covid-19 cases around the globe powered by DASH framework.
    '''),
    dcc.Graph(
        id='Global Data',
        figure=fig_scatter
    ),
    dcc.Graph(
        id='Global Data 2',
        figure=fig_bar
    )
])


if __name__ == '__main__':
    """ Run this app with `python app.py` and
        Visit http://127.0.0.1:8050/ in your web browser.
    """
    app.run_server(debug=True)
