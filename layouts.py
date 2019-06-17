import dash_core_components as dcc
import dash_html_components as html
import dash_table
# from components import Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd

import plotly.graph_objs as go


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

dt_columns = ['Placement type', 'Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY', 'Spend YoY (%)', \
                        'Sessions - TY', 'Sessions - LP', 'Sessions - LY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
                        'Bookings - TY', 'Bookings - LP', 'Bookings PoP (%)', 'Bookings PoP (Abs)', 'Bookings - LY', 'Bookings YoY (%)', 'Bookings YoY (Abs)', \
                        'Revenue - TY', 'Revenue - LP', 'Revenue PoP (Abs)', 'Revenue PoP (%)', 'Revenue - LY', 'Revenue YoY (%)', 'Revenue YoY (Abs)',]

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

df_columns_calculated = ['Placement type', 'CPS - TY', 
                        'CPS - LP', 'CPS PoP (Abs)', 'CPS PoP (%)',
                        'CPS - LY',  'CPS YoY (Abs)',  'CPS YoY (%)', 
                        'CVR - TY', 
                        'CVR - LP', 'CVR PoP (Abs)', 'CVR PoP (%)',
                        'CVR - LY',  'CVR YoY (Abs)',  'CVR YoY (%)',
                        'CPA - TY', 
                        'CPA - LP', 'CPA PoP (Abs)', 'CPA PoP (%)',
                        'CPA - LY', 'CPA YoY (Abs)',  'CPA YoY (%)']

conditional_columns_calculated_calculated = ['CPS_PoP_abs_conditional', 'CPS_PoP_percent_conditional', 'CPS_YoY_abs_conditional', 'CPS_PoP_percent_conditional', 
'CVR_PoP_abs_conditional', 'CVR_PoP_percent_conditional', 'CVR_YoY_abs_conditional', 'CVR_YoY_percent_conditional',
'CPA_PoP_abs_conditional', 'CPA_PoP_percent_conditional', 'CPA_YoY_abs_conditional', 'CPA_YoY_percent_conditional']

DEFAULT_COLORSCALE = ["#2a4858", "#265465", "#1e6172", "#106e7c", "#007b84", \
	"#00898a", "#00968e", "#19a390", "#31b08f", "#4abd8c", "#64c988", \
	"#80d482", "#9cdf7c", "#bae976", "#d9f271", "#fafa6e"]

mapbox_access_token = "pk.eyJ1IjoiamFja3AiLCJhIjoidGpzN0lXVSJ9.7YK6eRwUNFwd3ODZff6JvA"


# layout_county_choropleth = html.Div([
#     dcc.Graph(
# 			id ='county-choropleth',
# 			figure=dict(
# 				data=dict(
#                     type='scattermapbox',
#                     lat=[0],
#                     lon=[0],
#                     mode='markers',
#                     marker=dict(size=0.5, color='#a490bd'),
#                     showscale=True,
#                     autocolorscale=False,
#                     color=range(0,101),
#                     # colorscale=DEFAULT_COLORSCALE
# 				),
#                 layout=dict(
#                     mapbox=dict(
#                         layers=[
#                             dict(
#                                 sourcetpye='geojson',
#                                 source='data/gz_2010_us_050_00_500k.json',
#                                 type='fill',
#                                 color='rgba(163,22,19,0.8)'
#                             )
#                         ],
#                         accesstoken=mapbox_access_token,
#                         style='light',
#                         center=dict(lat=38.72490, lon=-95.61446),
#                         zoom=2.5
#                     ),
#                     hovermode='closest',
#                     margin=dict(r=0, l=0, t=0, b=0),
#                     dragmode='lasso'
#                 )
# 			)
# 		)
# ])

data = go.Data([
    go.Scattermapbox(
        lat=[0],
        lon=[0],
        mode='markers',
    )
])
layout = go.Layout(
    mapbox=dict(
        layers=[
            dict(
                sourcetype='geojson',
                source='/assets/data/gz_2010_us_050_00_500k.json',
                type='fill',
                color='rgba(163,22,19,0.7)'
            )
        ],
        accesstoken=mapbox_access_token,
        style='dark',
        center=dict(lat=38.72490, lon=-95.61446),
        zoom=2.5
    ),
    hovermode='closest',
    margin=dict(r=0, l=0, t=0, b=0),
    # dragmode='lasso'
)

fig = go.Figure(data=data, layout=layout)

layout_county_choropleth = html.Div([
    dcc.Graph(id='county_choropleth', figure=fig)
])

######################## START Paid Search Layout ########################
layout_paid_search =  html.Div([
    html.Div([
        # # CC Header
        # Header(),
        # Date Picker
        html.Div([
            dcc.DatePickerRange(
              id='my-date-picker-range-paid-search',
              min_date_allowed=dt(2018, 1, 1),
              max_date_allowed=df['Date'].max().to_pydatetime(),
              initial_visible_month=dt(current_year,df['Date'].max().to_pydatetime().month, 1),
              start_date=(df['Date'].max() - timedelta(6)).to_pydatetime(),
              end_date=df['Date'].max().to_pydatetime(),
            ),
            html.Div(id='output-container-date-picker-range-paid-search')
            ], className="row ", style={'marginTop': 30, 'marginBottom': 15}),
        # Header Bar
        html.Div([
          html.H6(["Paid Search"], className="gs-header gs-text-header padded",style={'marginTop': 15})
          ]),
        # Radio Button
        html.Div([
          dcc.RadioItems(
            options=[
                {'label': 'Condensed Data Table', 'value': 'Condensed'},
                {'label': 'Complete Data Table', 'value': 'Complete'},
            ], value='Condensed',
            labelStyle={'display': 'inline-block', 'width': '20%', 'margin':'auto', 'marginTop': 15, 'paddingLeft': 15},
            id='radio-button-paid-search'
            )]),
        # First Data Table
        html.Div([
            dash_table.DataTable(
                id='datatable-paid-search',
                columns=[{"name": i, "id": i, 'deletable': True} for i in dt_columns] 
                + [{"name": j, "id": j, 'hidden': 'True'} for j in conditional_columns], 
                editable=True,
                n_fixed_columns=2,
                style_table={'maxWidth': '1500px'},
                row_selectable="multi",
                selected_rows=[0],
                ),
            ], className=" twelve columns"),
        # Download Button
        html.Div([
          html.A(html.Button('Download Data', id='download-button'), id='download-link-paid-search-1')
          ]),
        # Second Data Table
        html.Div([
            dash_table.DataTable(
              id='datatable-paid-search-2',
              columns=[{"name": i, "id": i} for i in df_columns_calculated] + 
              [{"name": k, "id": k, 'hidden': 'True'} for k in conditional_columns_calculated_calculated],
              editable=True,
              n_fixed_columns=1,
              css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
              style_table={'maxWidth': '1500px'}, 
                ),
            ], className=" twelve columns"),
        # GRAPHS
        html.Div([
            html.Div([
              dcc.Graph(id='paid-search'),
              ], className=" twelve columns"
              )
            ], className="row ")
        ], className="subpage")
    ], className="page")
