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

from models.covid19_model import Covid19Model


# Init app and modules
covid19_model = Covid19Model()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Prepare data and Create graph
df = covid19_model.get_current()
fig = px.scatter(df, x='deaths', y='active',
                 size='confirmed', color="location", hover_name='location',
                 log_x=True, size_max=60)


# Create layout
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    """ Run this app with `python app.py` and
        Visit http://127.0.0.1:8050/ in your web browser.
    """
    app.run_server(debug=True)
