import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server)

credit_data = pd.read_csv('credit_data.csv') 
# columns: client_id, credit_exposure
client_data = pd.read_csv('client_data.csv')
# columns: client_id, client_type
merged_data = pd.merge(credit_data, client_data, on='client_id', how='left')

#############################################################
# Task 1 
# Add SQl database connection and rewrite lines above to fetch "merged_data" as a SQL single request
#############################################################

app.layout = html.Div(children=[
    html.H1(children='Credit Exposure by Client Type'),
    html.Button('Generate Graph', id='generate-graph-button'),
    dcc.Graph(id='credit-exposure')
])

@app.callback(
    Output('credit-exposure', 'figure'),
    Input('generate-graph-button', 'n_clicks')
)
def generate_graph_credit_amount_by_type(n_clicks):
    if n_clicks is None:
        return dash.no_update
    
    result = 
#############################################################
# Task 2
# Output sum of credit by type of client
#############################################################
    fig = px.bar(result, x=result.index, y='credit_exposure')
    return fig

#############################################################
# Task 3
# Add Flask HTTP endpoint that outputs 10% and 90% quantile credit exposure clients as JSON
#############################################################

#############################################################
# Task 4
# How we can estimate credit risks of such credit portfolio
#############################################################

if __name__ == '__main__':
    app.run_server(debug=True)

    
    
############################################################################
############################################################################

# You are given a list of student's grades ranging from 2 to 5. 
# Grades can only be natural number from 2 to 5

marks = [2,2,3,4,2,4,2,4,3,2,3,5,2,4,3,2,2,2,3,3,2,4]

#############################################################
# Task 5
# Calculate mean, median, std
#############################################################

#############################################################
# Task 6
# What kind of distribution this can be? 
# What are fat-tail distributions and how can measure the "tail"?
#############################################################

#############################################################
# Task 7
# Sort this list and explain O()-difficulty of algrorithm
#############################################################

