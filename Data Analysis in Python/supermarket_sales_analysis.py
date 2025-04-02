import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('synthetic_sales_data_extended.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# --- 🔹 Sales Trend Analysis ---
sales_over_time = df.groupby('Date')['Total'].sum()
sales_over_time.plot(figsize=(10,5), title="Total Sales Over Time", ylabel="Total Sales", xlabel="Date", grid=True)
plt.show()

# --- 🔹 Profitability Analysis ---
df['Profit'] = df['Total'] * df['Profit_Margin']
profit_by_category = df.groupby('Product_Line')['Profit'].sum()
profit_by_category.plot(kind='bar', title="Profit by Product Category", ylabel="Profit", figsize=(8,5))
plt.show()

# --- 🔹 Customer Segmentation ---
customer_segments = df['Customer_Segment'].value_counts()
customer_segments.plot(kind='pie', autopct='%1.1f%%', title="Customer Segments Distribution", figsize=(6,6))
plt.show()

# --- 🔹 City-Wise Performance ---
city_sales = df.groupby('City')['Total'].sum()
city_sales.plot(kind='bar', title="Total Sales by City", ylabel="Total Sales", figsize=(8,5))
plt.show()

# --- 🔹 Payment Methods ---
payment_counts = df['Payment_Method'].value_counts()
sns.barplot(x=payment_counts.index, y=payment_counts.values)
plt.title("Payment Method Popularity")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.show()
