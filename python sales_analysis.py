import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

df = pd.read_csv("supermarket_sales.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

df['Dates'] = pd.to_datetime(df['Dates'], format="%d-%m-%Y")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

df['Year'] = df['Dates'].dt.year
df['Month'] = df['Dates'].dt.month
df['Month_Name'] = df['Dates'].dt.strftime('%b')

total_revenue = df['Total'].sum()
print("\nTotal Revenue:", round(total_revenue, 2))

monthly_revenue = df.groupby('Month_Name')['Total'].sum().sort_values()

print("\nMonthly Revenue:")
print(monthly_revenue)

monthly_revenue.plot(kind='bar', color='purple')
plt.title("Monthly Revenue")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

product_profit = df.groupby('product_line')['gross_income'].sum().sort_values(ascending=False)

print("\nTop Product Lines by Profit:")
print(product_profit)

sns.barplot(x=product_profit.values, y=product_profit.index, palette="viridis")
plt.title("Profit by Product Line")
plt.xlabel("Total Profit")
plt.show()

city_revenue = df.groupby('city')['total'].sum().sort_values(ascending=False)

print("\nCity-wise Revenue:")
print(city_revenue)

city_revenue.plot(kind='bar', color='teal')
plt.title("Revenue by City")
plt.ylabel("Revenue")
plt.show()

avg_order_value = df['total'].sum() / df['invoice_id'].nunique()
print("\nAverage Order Value:", round(avg_order_value, 2))

top_10 = df[['invoice_id', 'total']].sort_values(by='total', ascending=False).head(10)

print("\nTop 10 Transactions:")
print(top_10)

payment_analysis = df.groupby('payment')['total'].sum()

payment_analysis.plot(kind='pie', autopct='%1.1f%%')
plt.title("Revenue by Payment Method")
plt.ylabel("")
plt.show()

monthly_revenue.to_csv("monthly_revenue_output.csv")

print("\nProject Completed Successfully ✅")

