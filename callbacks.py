from dash.dependencies import Input, Output
from app import app
import plotly.graph_objs as go
from plotly import tools

from datetime import datetime as dt
from datetime import date, timedelta
from datetime import datetime

import numpy as np
import pandas as pd

from components.functions import formatter_currency, formatter_currency_with_cents, formatter_percent, formatter_percent_2_digits, formatter_number
from components.functions import update_first_datatable, update_first_download, update_second_datatable, update_graph


pd.options.mode.chained_assignment = None

# Read in Travel Report Data
df = pd.read_csv('assets/data/performance_analytics_cost_and_ga_metrics.csv')

df.rename(columns={
 'Travel Product': 'Placement type', 
  'Spend - This Year': 'Spend TY', 
  'Spend - Last Year': 'Spend LY', 
  'Sessions - This Year': 'Sessions - TY',
  'Sessions - Last Year': 'Sessions - LY',
  'Bookings - This Year': 'Bookings - TY',
  'Bookings - Last Year': 'Bookings - LY',
  'Revenue - This Year': 'Revenue - TY',
  'Revenue - Last Year': 'Revenue - LY',
  }, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
current_year = df['Year'].max()
current_week = df[df['Year'] == current_year]['Week'].max()

now = datetime.now()
datestamp = now.strftime("%Y%m%d")

columns = ['Spend TY', 'Spend LY', 'Sessions - TY', 'Sessions - LY', 'Bookings - TY', 'Bookings - LY', 'Revenue - TY', 'Revenue - LY']

columns_complete = ['Placement type', 'Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY', 'Spend YoY (%)', \
                        'Sessions - TY', 'Sessions - LP', 'Sessions - LY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
                        'Bookings - TY', 'Bookings - LP', 'Bookings PoP (%)', 'Bookings PoP (Abs)', 'Bookings - LY', 'Bookings YoY (%)', 'Bookings YoY (Abs)', \
                        'Revenue - TY', 'Revenue - LP', 'Revenue PoP (Abs)', 'Revenue PoP (%)', 'Revenue - LY', 'Revenue YoY (%)', 'Revenue YoY (Abs)']

columns_condensed = ['Placement type', 'Spend TY', 'Spend PoP (%)', 'Spend YoY (%)', 'Sessions - TY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
                        'Bookings - TY',  'Bookings PoP (%)', 'Bookings YoY (%)',]

conditional_columns = ['Spend_PoP_abs_conditional', 'Spend_PoP_percent_conditional', 'Spend_YoY_percent_conditional',
'Sessions_PoP_percent_conditional', 'Sessions_YoY_percent_conditional', 
'Bookings_PoP_abs_conditional', 'Bookings_YoY_abs_conditional', 'Bookings_PoP_percent_conditional', 'Bookings_YoY_percent_conditional',
'Revenue_PoP_abs_conditional', 'Revenue_YoY_abs_conditional', 'Revenue_PoP_percent_conditional', 'Revenue_YoY_percent_conditional',]

dt_columns_total = ['Placement type', 'Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY', 'Spend YoY (%)', \
                        'Sessions - TY', 'Sessions - LP', 'Sessions - LY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
                        'Bookings - TY', 'Bookings - LP', 'Bookings PoP (%)', 'Bookings PoP (Abs)', 'Bookings - LY', 'Bookings YoY (%)', 'Bookings YoY (Abs)', \
                        'Revenue - TY', 'Revenue - LP', 'Revenue PoP (Abs)', 'Revenue PoP (%)', 'Revenue - LY', 'Revenue YoY (%)', 'Revenue YoY (Abs)',
                        'Spend_PoP_abs_conditional', 'Spend_PoP_percent_conditional', 'Spend_YoY_percent_conditional',
'Sessions_PoP_percent_conditional', 'Sessions_YoY_percent_conditional', 
'Bookings_PoP_abs_conditional', 'Bookings_YoY_abs_conditional', 'Bookings_PoP_percent_conditional', 'Bookings_YoY_percent_conditional',
'Revenue_PoP_abs_conditional', 'Revenue_YoY_abs_conditional', 'Revenue_PoP_percent_conditional', 'Revenue_YoY_percent_conditional',]


## choropleth map layout

mapbox_access_token = "pk.eyJ1IjoiamFja3AiLCJhIjoidGpzN0lXVSJ9.7YK6eRwUNFwd3ODZff6JvA"

stores_df = pd.read_csv('assets/data/stores.csv')

BINS = ['0-2', '2.1-4', '4.1-6', '6.1-8', '8.1-10', '10.1-12', '12.1-14', \
		'14.1-16', '16.1-18', '18.1-20', '20.1-22', '22.1-24',  '24.1-26', \
		'26.1-28', '28.1-30', '>30']

DEFAULT_COLORSCALE = ["#2a4858", "#265465", "#1e6172", "#106e7c", "#007b84", \
	"#00898a", "#00968e", "#19a390", "#31b08f", "#4abd8c", "#64c988", \
	"#80d482", "#9cdf7c", "#bae976", "#d9f271", "#fafa6e"]

# data = [dict(type='scattermapbox',
#     lat=[0],
#     lon=[0],
#     mode='markers',
#     marker=dict(size=0.5, color='#a490bd'),
#     showscale=True,
#     autocolorscale=False,
#     color=range(0,101),
#     colorscale=DEFAULT_COLORSCALE
# )]

# layout = dict(
#     mapbox = dict(
#         layers = [],
#         accesstoken = mapbox_access_token,
#         style = 'light',
#         center=dict(lat=38.72490, lon=-95.61446),
#         zoom=2.5
#     ),
#     hovermode = 'closest',
#     margin = dict(r=0, l=0, t=0, b=0),
#     dragmode = 'lasso'
# )

# # for bin in BINS:
# geo_layer = dict(
#     sourcetype = 'geojson',
#     source = 'data/gz_2010_us_050_00_500k.json'
#     type = 'fill',
#     color = "#19a390", # cm[bin]
#     opacity = opacity
# )
# layout['mapbox']['layers'].append(geo_layer)

# fig = dict(data=data, layout=layout)



######################## Paid Search Callbacks ######################## 

#### Date Picker Callback
@app.callback(Output('output-container-date-picker-range-paid-search', 'children'),
	[Input('my-date-picker-range-paid-search', 'start_date'),
	 Input('my-date-picker-range-paid-search', 'end_date')])
def update_output(start_date, end_date):
	string_prefix = 'You have selected '
	if start_date is not None:
		start_date = dt.strptime(start_date, '%Y-%m-%d')
		start_date_string = start_date.strftime('%B %d, %Y')
		string_prefix = string_prefix + 'a Start Date of ' + start_date_string + ' | '
	if end_date is not None:
		end_date = dt.strptime(end_date, '%Y-%m-%d')
		end_date_string = end_date.strftime('%B %d, %Y')
		days_selected = (end_date - start_date).days
		prior_start_date = start_date - timedelta(days_selected + 1)
		prior_start_date_string = datetime.strftime(prior_start_date, '%B %d, %Y')
		prior_end_date = end_date - timedelta(days_selected + 1)
		prior_end_date_string = datetime.strftime(prior_end_date, '%B %d, %Y')
		string_prefix = string_prefix + 'End Date of ' + end_date_string + ', for a total of ' + str(days_selected + 1) + ' Days. The prior period Start Date was ' + \
		prior_start_date_string + ' | End Date: ' + prior_end_date_string + '.'
	if len(string_prefix) == len('You have selected: '):
		return 'Select a date to see it displayed here'
	else:
		return string_prefix

# Callback and update first data table
@app.callback(Output('datatable-paid-search', 'data'),
	[Input('my-date-picker-range-paid-search', 'start_date'),
	 Input('my-date-picker-range-paid-search', 'end_date')])
def update_data_1(start_date, end_date):
	data_1 = update_first_datatable(start_date, end_date, 'Paid Search', 'Placement type')
	return data_1

# Callback and update data table columns
@app.callback(Output('datatable-paid-search', 'columns'),
    [Input('radio-button-paid-search', 'value')])
def update_columns(value):
    if value == 'Complete':
    	column_set=[{"name": i, "id": i, 'deletable': True} for i in columns_complete] + [{"name": j, "id": j, 'hidden': 'True'} for j in conditional_columns]
    elif value == 'Condensed':
        column_set=[{"name": i, "id": i, "deletable": True} for i in columns_condensed]
    return column_set

# Callback and update second data table
@app.callback(
	Output('datatable-paid-search-2', 'data'),
	[Input('my-date-picker-range-paid-search', 'start_date'),
	 Input('my-date-picker-range-paid-search', 'end_date')])
def update_data_2(start_date, end_date):
	data_2 = update_second_datatable(start_date, end_date, 'Paid Search', 'Placement type')
	return data_2

# Callback for the Graphs
@app.callback(
   Output('paid-search', 'figure'),
   [Input('datatable-paid-search', "selected_rows"),
   Input('my-date-picker-range-paid-search', 'end_date')])
def update_paid_search(selected_rows, end_date):
	travel_product = []
	travel_product_list = df[(df['Category'] == 'Paid Search')]['Placement type'].unique().tolist()
	for i in selected_rows:
		travel_product.append(travel_product_list[i])
		# Filter by specific product
	filtered_df = df[(df['Placement type'].isin(travel_product))].groupby(['Year', 'Week']).sum()[['Spend TY', 'Spend LY', 'Sessions - TY', 'Sessions - LY', 'Bookings - TY', 'Bookings - LY', 'Revenue - TY', 'Revenue - LY']].reset_index()
	fig = update_graph(filtered_df, end_date)
	return fig

