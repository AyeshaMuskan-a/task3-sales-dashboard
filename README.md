# task3-sales-dashboard
# 📊 Sales Performance & Revenue Insights Dashboard — Task 3

## 🚀 Project Summary

This is **Task 3 (Dashboard Design)** for the **DataX Labs Internship**. It presents an interactive, stakeholder-facing dashboard built to track sales performance, monitor revenue and profit trends, and support business decision-making — using SQL, Python, and Power BI end to end.

---

## 🎯 Objective

Design an interactive dashboard for business stakeholders that:

* Tracks key sales KPIs (Revenue, Profit, Orders, Growth)
* Uses slicers/filters for interactivity
* Includes time-series analysis
* Displays summary cards for quick insights
* Applies a consistent, professional color theme

---

## 🛠️ Tech Stack

* **SQL** → Data cleaning, transformation, and querying
* **Python** → Data analysis and visualization
  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
* **Power BI** → Interactive dashboard and stakeholder visuals

---

## 📂 Project Structure

```
task3-sales-dashboard/
│
├── dataset/
│   └── sales_sample_data.csv
│
├── sql/
│   └── sales_queries.sql
│
├── python/
│   └── analysis.py
│
├── dashboard/
│   └── Sales_Performance_Dashboard.pbix
│
├── ppt/
│   └── Task3_Sales_Dashboard_Summary.pptx
│
├── images/
│   └── dashboard_preview.png
│
└── README.md
```

**Note:** A sample dataset (~500 records) is included for reference and reproducibility.

---

## 🧹 Data Preparation

* Handled missing values and removed invalid records
* Standardized column names and formats
* Converted date columns into proper datetime format
* Engineered features: Year, Month, Quarter

---

## 📈 Dashboard Features (Power BI)

**KPI Cards**
* Total Revenue
* Total Orders
* Total Profit
* Average Order Value

**Interactive Slicers**
* Region
* Category
* Year / Month / Quarter

**Visualizations**
* Revenue trend over time (time-series analysis)
* Top products by revenue
* Revenue by region
* Category-wise contribution
* Top customers by revenue

---

## 📊 Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

---

## 📌 Key Insights

* Revenue shows strong growth, peaking in Q4
* A small group of products drives a large share of total revenue
* Regional performance varies significantly, guiding where to focus growth efforts
* A few key customers contribute a disproportionate share of revenue

---

## ⚙️ How to Run

**1. Clone the repository**
```
git clone https://github.com/AyeshaMuskan-a/task3-sales-dashboard.git
cd task3-sales-dashboard
```

**2. Run SQL queries**
* Open `/sql/sales_queries.sql` in your SQL client and execute

**3. Run Python analysis**
```
python python/analysis.py
```

**4. Open the Power BI dashboard**
* Open `/dashboard/Sales_Performance_Dashboard.pbix` in Power BI Desktop

**5. View the stakeholder summary**
* Open `/ppt/Task3_Sales_Dashboard_Summary.pptx`

---

## 📌 Business Impact

This dashboard helps stakeholders:

* Make faster, data-informed decisions
* Identify growth opportunities by region and category
* Spot top-performing products and customers
* Track performance trends over time

---

## 🚀 Future Enhancements

* Add a navigation menu for multi-page drill-through
* Incorporate time-series forecasting (ARIMA/Prophet)
* Add customer segmentation (RFM analysis)
* Automate the data refresh pipeline

---

## 📌 Conclusion

This project demonstrates an end-to-end analytics workflow — from data cleaning to an interactive, decision-ready dashboard — completed as part of the DataX Labs Data Analyst Internship, Task 3.
