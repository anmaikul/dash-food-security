import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()


app.layout = html.Div([
    dcc.Input(id='my-id', value='Dash App', type='text'),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')


# app.layout = html.Div([
#     html.Label('Multi-Select Dropdown', style={'backgroundColor': 'red', 'textAlign': 'center',}),
#     dcc.RadioItems(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL',
#     ),
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure={
#             'data': [
#                 go.Scatter(
#                     x=df[df['continent'] == i]['gdp per capita'],
#                     y=df[df['continent'] == i]['life expectancy'],
#                     text=df[df['continent'] == i]['country'],
#                     mode='markers',
#                     opacity=0.8,
#                     marker={
#                         'size': 15,
#                         'line': {'width': 0.5, 'color': 'white'}
#                     },
#                     name=i
#                 ) for i in df.continent.unique()
#             ],
#             'layout': go.Layout(
#                 xaxis={'type': 'log', 'title': 'GDP Per Capita'},
#                 yaxis={'title': 'Life Expectancy'},
#                 margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                 legend={'x': 0, 'y': 1},
#                 hovermode='closest'
#             )
#         }
#     )
# ])



# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }
# app.layout = html.Div(style={
#     'backgroundColor': colors['background'],
#     'display': 'grid',
#     'gridTemplateColumns': '1fr 1fr', 
# }, 
# children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),
#     html.P(children='Dash: A web application framework for Python.', style={
#         'margin-top': '20px',
#         'textAlign': 'center',
#         'color': colors['text']
#     }),
#     dcc.Graph(
#         id='Graph1',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'plot_bgcolor': colors['background'],
#                 'paper_bgcolor': colors['background'],
#                 'font': {
#                     'color': colors['text']
#                 }
#             }
#         }
#     )
# ])

if __name__ == '__main__':
    app.run_server(debug=True)