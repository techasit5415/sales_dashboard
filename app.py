import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter
from bokeh.embed import components
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# อ่านข้อมูลจาก CSV
df = pd.read_csv("Sales_Data.csv")

# เตรียมข้อมูล Aggregated
monthly_sales = df.groupby('Month').sum()['Sales'].reset_index()
city_sales = df.groupby('City').sum()['Sales'].reset_index()
hourly_sales = df.groupby('Hour').sum()['Sales'].reset_index()

# ColumnDataSource
source_monthly = ColumnDataSource(monthly_sales)
source_city = ColumnDataSource(city_sales)
source_hourly = ColumnDataSource(hourly_sales)

# สร้างกราฟ Bokeh
def create_bokeh_figure(title, x_label, y_label, x_range, source, x_col, y_col, color):
    plot = figure(title=title, x_axis_label=x_label, y_axis_label=y_label, x_range=x_range, width=1000, height=600)
    plot.vbar(x=x_col, top=y_col, width=0.5, source=source, color=color)
    plot.yaxis.formatter = NumeralTickFormatter(format="0,0")
    plot.y_range.start = 0
    plot.add_tools(HoverTool(tooltips=[(x_label, f"@{x_col}"), (y_label, f"@{y_col}{{0,0}}")]))
    return plot

plot_monthly = create_bokeh_figure("Monthly Sales", "Month", "Sales", list(map(str, monthly_sales['Month'])), source_monthly, 'Month', 'Sales', "blue")
plot_city = create_bokeh_figure("Sales by City", "City", "Sales", city_sales['City'], source_city, 'City', 'Sales', "green")
plot_hourly = figure(title="Sales by Hour", x_axis_label="Hour", y_axis_label="Sales", width=1000, height=600)
plot_hourly.line(x='Hour', y='Sales', line_width=4, source=source_hourly, color="orange")
plot_hourly.yaxis.formatter = NumeralTickFormatter(format="0,0")
plot_hourly.y_range.start = 0
plot_hourly.add_tools(HoverTool(tooltips=[("Hour", "@Hour"), ("Sales", "@Sales{0,0}")]))


# แปลง Bokeh เป็น HTML components สำหรับ Dash
script1, div1 = components(plot_monthly)
script2, div2 = components(plot_city)
script3, div3 = components(plot_hourly)

# สร้าง Dash App
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Interactive Sales Dashboard", className="text-center text-light mb-4"), width=12)
    ]),
    dbc.Tabs([
        dbc.Tab(dbc.Container([html.Div(id="monthly-sales", children=[html.Script(script1), html.Div(div1, className="bokeh-plot")])]), label="Monthly Sales"),
        dbc.Tab(dbc.Container([html.Div(id="sales-by-city", children=[html.Script(script2), html.Div(div2, className="bokeh-plot")])]), label="Sales by City"),
        dbc.Tab(dbc.Container([html.Div(id="sales-by-hour", children=[html.Script(script3), html.Div(div3, className="bokeh-plot")])]), label="Sales by Hour"),
    ])
], fluid=True)

# รันเซิร์ฟเวอร์
if __name__ == "__main__":
    app.run_server(debug=True)
