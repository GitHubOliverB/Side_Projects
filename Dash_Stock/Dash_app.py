# !/usr/bin/python

"""
Summary:

Here we run all functions.
Runs only one classifier and does a cross-validation(k=2).
"""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reference for the code of this script
# Block 0 - Library Imports
# 	Block 0.1 - Defining functions and globals...
#	Block 0.2 - Paths
# Block 1.0 - Dash App

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Block 0 - Library Imports

# Basic Python Libs
import os
import sys
import time
import datetime
import importlib
import requests
import csv
import pydotplus
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import pandas_datareader as web
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats
from dateutil.relativedelta import relativedelta
from collections import deque

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

# Outside Stuff
from iexfinance.stocks import get_historical_data
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
from mini_yahoo_finance import get_stock_df

# 	Block 0.1 - Defining functions and globals...

# iexfinance stuff
start_date = datetime.datetime.today() - relativedelta(years=5)
end_date = datetime.datetime.today()

# Yahoo stuff
start_date_yahoo = '01-01-2000'

# morningstar Stuff
start_date_morningstar = datetime.datetime.now() - relativedelta(years=5)
end_date_morningstar = datetime.datetime.now()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Block 1.0 - Dash App

# Start Dash
app = dash.Dash(__name__)

# Set Layout
app.layout = html.Div([
    html.Div([
        html.H2(children="Dash Stock Example"),
        html.Img(src="/assets/stock-icon.png")
    ], className="banner"),

    html.Div([
        dcc.Input(
            id="stock-input",
            value="Gold",
            type="text"),
        html.Button(id="submit-buttom", n_clicks=0, children="Submit")
    ]),

    html.Div([
        html.Div([
            dcc.Graph(
                id="graph_close",
            )
        ], className="twelve columns"),

    ], className="row")
])

# Append css from web.
app.css.config.serve_locally = False
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

# Dash Callback
@app.callback(Output("graph_close", "figure"),
              [Input("submit-buttom", "n_clicks")],
              [State("stock-input", "value")]
              )
def update_fig(n_clicks, input_value):
    # Morningstar
    # df = web.DataReader(input_value, 'morningstar', start_date_morningstar, end_date_morningstar)
    # df.reset_index(inplace=True)
    # df.set_index("Date", inplace=True)
    # df = df.drop("Symbol", axis=1)

    # Yahoo
    df = get_stock_df(input_value,
                       start_date=start_date_yahoo,
                       interval='1d')
    data = []

    # Get points to plot from dataset
    trace_line = go.Scatter(x=list(df.Date),
                            y=list(df.Close),
                            # visible=False,
                            name="Close",
                            showlegend=False)

    trace_candle = go.Candlestick(x=df.Date,
                                  open=df.Open,
                                  high=df.High,
                                  low=df.Low,
                                  close=df.Close,
                                  # increasing=dict(line=dict(color="#00ff00")),
                                  # decreasing=dict(line=dict(color="white")),
                                  visible=False,
                                  showlegend=False)

    trace_bar = go.Ohlc(x=df.Date,
                        open=df.Open,
                        high=df.High,
                        low=df.Low,
                        close=df.Close,
                        # increasing=dict(line=dict(color="#888888")),
                        # decreasing=dict(line=dict(color="#888888")),
                        visible=False,
                        showlegend=False)

    data = [trace_line, trace_candle, trace_bar]

    updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Line',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False]}],
                    label='Candle',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True]}],
                    label='Bar',
                    method='update'
                ),
            ]),
            direction='down',
            pad={'r': 5, 't': 5},
            showactive=True,
            x=0.13,
            xanchor='left',
            y=1.03,
            yanchor='bottom'
        ),
    ])
    layout = dict(
        title=input_value,
        updatemenus=updatemenus,
        autosize=False,
        ylabel=dict(title="Stock Value [€]"),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(count=3,
                         label='3y',
                         step='year',
                         stepmode='backward'),
                    dict(count=5,
                         label='5y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )
    return {"data": data, "layout": layout}

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)