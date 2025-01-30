from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, TabPanel, Tabs, HoverTool,NumeralTickFormatter
from bokeh.plotting import figure
import pandas as pd

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

# กราฟ Monthly Sales
plot_monthly = figure(title="Monthly Sales", x_axis_label="Month", y_axis_label="Sales", x_range=list(map(str, monthly_sales['Month'])), width=1200, height=800)
plot_monthly.vbar(x='Month', top='Sales', width=0.5, source=source_monthly, color="blue")

# ตั้งค่า formatter ให้แสดงผลยอดขายในรูปแบบธรรมดา
plot_monthly.yaxis.formatter = NumeralTickFormatter(format="0,0")

# เพิ่ม HoverTool ให้กับกราฟ Monthly Sales
hover_monthly = HoverTool()
hover_monthly.tooltips = [("Month", "@Month"), ("Sales", "@Sales{0,0}")]
plot_monthly.add_tools(hover_monthly)

# กราฟ Sales by City
plot_city = figure(title="Sales by City", x_axis_label="City", y_axis_label="Sales", x_range=city_sales['City'], width=1000, height=800)
plot_city.vbar(x='City', top='Sales', width=0.5, source=source_city, color="green")

# ตั้งค่า formatter ให้แสดงผลยอดขายในรูปแบบธรรมดา
plot_city.yaxis.formatter = NumeralTickFormatter(format="0,0")

# เพิ่ม HoverTool ให้กับกราฟ Sales by City
hover_city = HoverTool()
hover_city.tooltips = [("City", "@City"), ("Sales", "@Sales{0,0}")]
plot_city.add_tools(hover_city)

# กราฟ Sales by Hour
plot_hourly = figure(title="Sales by Hour", x_axis_label="Hour", y_axis_label="Sales", width=1000, height=800)
plot_hourly.line(x='Hour', y='Sales', line_width=4, source=source_hourly, color="orange")

# ตั้งค่า formatter ให้แสดงผลยอดขายในรูปแบบธรรมดา
plot_hourly.yaxis.formatter = NumeralTickFormatter(format="0,0")

# เพิ่ม HoverTool ให้กับกราฟ Sales by Hour
hover_hourly = HoverTool()
hover_hourly.tooltips = [("Hour", "@Hour"), ("Sales", "@Sales{0,0}")]
plot_hourly.add_tools(hover_hourly)

# # Tabs
# tab1 = TabPanel(child=plot_monthly, title="Monthly Sales")
# tab2 = TabPanel(child=plot_city, title="Sales by City")
# tab3 = TabPanel(child=plot_hourly, title="Sales by Hour")

# tabs = Tabs(tabs=[tab1, tab2, tab3])

# Theme
curdoc().theme = "dark_minimal"

# Layout และ Title
# curdoc().add_root(tabs)
# curdoc().title = "Interactive Sales Dashboard"
