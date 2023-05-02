import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server)

credit_data = pd.read_csv('credit_data.csv')
client_data = pd.read_csv('client_data.csv')

merged_data = pd.merge(credit_data, client_data, on='client_id', how='left')
result = merged_data.groupby('client_type').agg({'credit_exposure': 'sum'})

fig = px.bar(result, x=result.index, y='credit_exposure')

app.layout = html.Div(children=[
    html.H1(children='Credit Exposure by Client Type'),
    dcc.Graph(
        id='credit-exposure',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

    
# add Flask HTTP endpoint that outputs 10% and 90% qiantile clients as JSON
# add SQl database connection and fetch "merged_data" as a single request
# how we can estimate credit risks of such credit portfolio

############################################################################

marks = [2,2,3,5,2,4,4,3,3,5,2,4,3]

# calc mean, median, std
# what kind of distribution this can be?
# sort this list and explain O()-difficulty of algrorithm
