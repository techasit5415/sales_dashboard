from flask import Flask
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from bokeh.embed import server_document

# สร้าง Flask app
flask_app = Flask(__name__)

# สร้าง Dash app
app = Dash(__name__, server=flask_app, external_stylesheets=[dbc.themes.DARKLY])

# ฝัง Bokeh ด้วย iframe
bokeh_app_url = "http://localhost:5006/sales_dashboard"

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Interactive Sales Dashboard", className="text-center text-light mb-4"), width=12)
    ]),
    dbc.Tabs([
        dbc.Tab(html.Iframe(src=bokeh_app_url, width="100%", height="800px"), label="Monthly Sales"),
        dbc.Tab(html.Iframe(src=bokeh_app_url, width="100%", height="800px"), label="Sales by City"),
        dbc.Tab(html.Iframe(src=bokeh_app_url, width="100%", height="800px"), label="Sales by Hour"),
    ])
], fluid=True)

# รัน Flask
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
