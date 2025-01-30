import streamlit as st
import pandas as pd
import plotly.express as px

# อ่านข้อมูลจาก CSV
df = pd.read_csv("Sales_Data.csv")

# สร้างกราฟจาก Plotly
fig_monthly = px.bar(df.groupby('Month').sum().reset_index(), x='Month', y='Sales', title='Monthly Sales')
fig_city = px.bar(df.groupby('City').sum().reset_index(), x='City', y='Sales', title='Sales by City')
fig_hourly = px.line(df.groupby('Hour').sum().reset_index(), x='Hour', y='Sales', title='Sales by Hour')

# สร้างหน้าจอของแอป Streamlit
st.title('Interactive Sales Dashboard')

tabs = st.selectbox("Select a category", ['Monthly Sales', 'Sales by City', 'Sales by Hour'])

if tabs == 'Monthly Sales':
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
    
    # สร้างกราฟที่กรองข้อมูล
    fig_filtered = px.bar(filtered_data, x='Month', y='Sales', title=f'Sales for Month: {selected_month}')

    # เปลี่ยนสีแถบทั้งหมดเป็นสีเทา
    fig_filtered.update_traces(marker=dict(color='lightgray'))
    
    # ไฮไลท์แค่แถบที่เลือก
    selected_month_data = df[df['Month'] == selected_month]
    fig_filtered.update_traces(marker=dict(color='red'),
                               selector=dict(x=selected_month_data['Month'].values))  # ไฮไลท์แถบที่เลือก
    
    # แสดงกราฟที่กรอง
    st.plotly_chart(fig_filtered)

elif tabs == 'Sales by City':
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
    
    # สร้างกราฟที่กรองข้อมูล
    fig_filtered = px.bar(filtered_data, x='City', y='Sales', title=f'Sales for City: {selected_city}')

    # เปลี่ยนสีแถบทั้งหมดเป็นสีเทา
    fig_filtered.update_traces(marker=dict(color='lightgray'))
    
    # ไฮไลท์แค่แถบที่เลือก
    selected_city_data = df[df['City'] == selected_city]
    fig_filtered.update_traces(marker=dict(color='red'),
                               selector=dict(x=selected_city_data['City'].values))  # ไฮไลท์แถบที่เลือก
    
    # แสดงกราฟที่กรอง
    st.plotly_chart(fig_filtered)

elif tabs == 'Sales by Hour':
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
    
    # สร้างกราฟที่กรองข้อมูล
    fig_filtered = px.line(filtered_data, x='Hour', y='Sales', title=f'Sales for Hour: {selected_hour}')

    # เปลี่ยนสีแถบทั้งหมดเป็นสีเทา
    fig_filtered.update_traces(marker=dict(color='lightgray'))
    
    # ไฮไลท์แค่แถบที่เลือก
    selected_hour_data = df[df['Hour'] == selected_hour]
    fig_filtered.update_traces(marker=dict(color='red'),
                               selector=dict(x=selected_hour_data['Hour'].values))  # ไฮไลท์แถบที่เลือก
    
    # แสดงกราฟที่กรอง
    st.plotly_chart(fig_filtered)
