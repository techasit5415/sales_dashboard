import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# อ่านข้อมูลจาก CSV
df = pd.read_csv("Sales_Data.csv")

# สร้างกราฟจาก Plotly
fig_monthly = px.bar(df.groupby('Month').sum().reset_index(), x='Month', y='Sales', title='Monthly Sales')
fig_city = px.bar(df.groupby('City').sum().reset_index(), x='City', y='Sales', title='Sales by City')
fig_hourly = px.line(df.groupby('Hour').sum().reset_index(), x='Hour', y='Sales', title='Sales by Hour')

# สร้างหน้าจอของแอป Streamlit
st.title('Interactive Sales Dashboard')

# st.subheader('Monthly Sales')
# st.plotly_chart(fig_monthly)

# st.subheader('Sales by City')
# st.plotly_chart(fig_city)

# st.subheader('Sales by Hour')
# st.plotly_chart(fig_hourly)

# option = st.radio('Choose a chart to display:', 
#                  ['Monthly Sales', 'Sales by City', 'Sales by Hour'])

# # แสดงกราฟตามตัวเลือกที่เลือก
# if option == 'Monthly Sales':
#     st.plotly_chart(fig_monthly)
# elif option == 'Sales by City':
#     st.plotly_chart(fig_city)
# else:
#     st.plotly_chart(fig_hourly)

tabs = st.tabs(["Monthly Sales", "Sales by City", "Sales by Hour"])

# แสดงกราฟในแต่ละแท็บ
# with tabs[0]:
#     st.plotly_chart(fig_monthly)
#     st.dataframe(df.groupby('Month').sum().reset_index())

# with tabs[1]:
#     st.plotly_chart(fig_city)
#     st.dataframe(df.groupby('City').sum().reset_index())

# with tabs[2]:
#     st.plotly_chart(fig_hourly)
#     st.dataframe(df.groupby('Hour').sum().reset_index())
# selected_data = None

# แสดงกราฟและตารางในแต่ละแท็บ
with tabs[0]:
    # กราฟ
    st.plotly_chart(fig_monthly)
    
    # ตาราง
    st.subheader('Monthly Sales Data')
    monthly_data = df.groupby('Month').sum().reset_index()
    st.dataframe(monthly_data)  # สร้างตารางที่สามารถเลือกได้

    # ใช้ selectbox ให้ผู้ใช้เลือกเดือน
    selected_month = st.selectbox('Select Month', monthly_data['Month'])
    
    # กรองข้อมูลที่เลือก
    filtered_data = monthly_data[monthly_data['Month'] == selected_month]
    
    # แสดงกราฟที่กรอง
    fig_filtered = px.bar(filtered_data, x='Month', y='Sales', title=f'Sales for Month: {selected_month}')
    st.plotly_chart(fig_filtered)

with tabs[1]:
    # กราฟ
    st.plotly_chart(fig_city)
    
    # ตาราง
    st.subheader('Sales by City Data')
    city_data = df.groupby('City').sum().reset_index()
    st.dataframe(city_data)

    # ใช้ selectbox ให้ผู้ใช้เลือกเมือง
    selected_city = st.selectbox('Select City', city_data['City'])
    
    # กรองข้อมูลที่เลือก
    filtered_data = city_data[city_data['City'] == selected_city]
    
    # แสดงกราฟที่กรอง
    fig_filtered = px.bar(filtered_data, x='City', y='Sales', title=f'Sales for City: {selected_city}')
    st.plotly_chart(fig_filtered)

with tabs[2]:
    # กราฟ
    st.plotly_chart(fig_hourly)
    
    # ตาราง
    st.subheader('Sales by Hour Data')
    hourly_data = df.groupby('Hour').sum().reset_index()
    st.dataframe(hourly_data)

    # ใช้ selectbox ให้ผู้ใช้เลือกชั่วโมง
    selected_hour = st.selectbox('Select Hour', hourly_data['Hour'])
    
    # กรองข้อมูลที่เลือก
    filtered_data = hourly_data[hourly_data['Hour'] == selected_hour]
    
    # แสดงกราฟที่กรอง
    fig_filtered = px.line(filtered_data, x='Hour', y='Sales', title=f'Sales for Hour: {selected_hour}')
    st.plotly_chart(fig_filtered)

