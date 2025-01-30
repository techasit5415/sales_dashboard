import pandas as pd

# อ่านข้อมูลจาก CSV
df = pd.read_csv("Sales_Data.csv")

# คำนวณข้อมูล Aggregated
monthly_sales = df.groupby('Month').sum()['Sales'].reset_index()
city_sales = df.groupby('City').sum()['Sales'].reset_index()
hourly_sales = df.groupby('Hour').sum()['Sales'].reset_index()

# บันทึกผลลัพธ์ลงในไฟล์ CSV
monthly_sales.to_csv('monthly_sales.csv', index=False)
city_sales.to_csv('city_sales.csv', index=False)
hourly_sales.to_csv('hourly_sales.csv', index=False)
