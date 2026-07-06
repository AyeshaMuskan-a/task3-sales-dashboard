# ==========================================
# SALES DATA ANALYSIS + ML PROJECT (FINAL)
# ==========================================

# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

plt.style.use('default')

# ==========================================
# 2. LOAD DATA
# ==========================================
df = pd.read_csv("product_sales_dataset.csv")

# ==========================================
# 3. CLEAN COLUMN NAMES (VERY IMPORTANT)
# ==========================================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n--- Columns ---")
print(df.columns)

# ==========================================
# 4. DATA CLEANING
# ==========================================

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['order_date'])

# Remove missing values
df.dropna(inplace=True)

# ==========================================
# 5. FEATURE ENGINEERING
# ==========================================
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['month_name'] = df['order_date'].dt.strftime('%b')
df['quarter'] = df['order_date'].dt.to_period('Q')

# ==========================================
# 6. KPI METRICS
# ==========================================
print("\n--- KPI METRICS ---")
print("Total Revenue:", df['revenue'].sum())
print("Total Orders:", df['order_id'].nunique())
print("Total Profit:", df['profit'].sum())
print("Average Order Value:", df['revenue'].mean())

# ==========================================
# 7. UNIVARIATE ANALYSIS
# ==========================================
plt.figure()
sns.histplot(df['revenue'], kde=True)
plt.title("Revenue Distribution")
plt.show()

plt.figure()
sns.boxplot(x=df['revenue'])
plt.title("Revenue Outliers")
plt.show()

# ==========================================
# 8. BIVARIATE ANALYSIS
# ==========================================
plt.figure()
sns.barplot(x='region', y='revenue', data=df)
plt.title("Revenue by Region")
plt.show()

plt.figure()
sns.barplot(x='category', y='revenue', data=df)
plt.title("Revenue by Category")
plt.xticks(rotation=45)
plt.show()

# ==========================================
# 9. MULTIVARIATE ANALYSIS
# ==========================================
plt.figure()
sns.heatmap(df[['revenue','profit','quantity']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(df[['revenue','profit','quantity']])
plt.show()

# ==========================================
# 10. MONTHLY TREND
# ==========================================
monthly = df.groupby(['year','month'])['revenue'].sum().reset_index()

plt.figure()
plt.plot(monthly['month'], monthly['revenue'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# ==========================================
# 11. TOP PRODUCTS
# ==========================================
top_products = df.groupby('product_name')['revenue'].sum().nlargest(10)

plt.figure()
top_products.sort_values().plot(kind='barh')
plt.title("Top 10 Products by Revenue")
plt.show()

# ==========================================
# 12. TOP CUSTOMERS
# ==========================================
top_customers = df.groupby('customer_name')['revenue'].sum().nlargest(10)

plt.figure()
top_customers.sort_values().plot(kind='barh')
plt.title("Top Customers by Revenue")
plt.show()

# ==========================================
# 13. CATEGORY SHARE
# ==========================================
category_sales = df.groupby('category')['revenue'].sum()

plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Contribution")
plt.ylabel('')
plt.show()

# ==========================================
# 14. MACHINE LEARNING (IMPROVED)
# ==========================================

# Add seasonality
monthly['month_sin'] = np.sin(2 * np.pi * monthly['month']/12)
monthly['month_cos'] = np.cos(2 * np.pi * monthly['month']/12)

# Features & target
X = monthly[['year','month','month_sin','month_cos']]
y = monthly['revenue']

# Train model
model = LinearRegression()
model.fit(X, y)

# Future prediction (2025)
future = pd.DataFrame({
    'year': [2025]*12,
    'month': range(1,13)
})

future['month_sin'] = np.sin(2 * np.pi * future['month']/12)
future['month_cos'] = np.cos(2 * np.pi * future['month']/12)

predictions = model.predict(future)

# Plot prediction
plt.figure()
plt.plot(monthly['month'], y, label='Actual', marker='o')
plt.plot(future['month'], predictions, label='Predicted', linestyle='--')
plt.title("Revenue Forecast (2025)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.show()

# ==========================================
# 15. SAVE CLEAN DATA
# ==========================================
df.to_csv("clean_sales_data.csv", index=False)

print("\n--- Clean Data Saved Successfully ---")
