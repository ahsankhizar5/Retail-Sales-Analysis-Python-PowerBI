# Retail Sales Analysis & Power BI Dashboard

This project performs an in-depth Exploratory Data Analysis (EDA) on a retail sales dataset and visualizes the findings in an interactive Power BI dashboard. The goal is to uncover key insights into sales performance, product trends, and customer behavior.

## Project Summary

This capstone project, completed as part of a Business Analytics program, demonstrates an end-to-end workflow for data analysis and visualization. It starts with raw data, proceeds through cleaning and analysis using Python, and culminates in a professional Power BI dashboard for effective communication of insights.

## 📊 Power BI Dashboard Preview

Here’s a snapshot of the interactive dashboard created in Power BI:

![Retail Dashboard](graphs/Dashboard%20Overview.png)

You can explore the full dashboard in Power BI Desktop by opening the `.pbix` file included in the repository.

### Key Features:
- **Data Cleaning & Preparation**: Handled missing values, removed duplicates, and ensured data quality.
- **Exploratory Data Analysis (EDA)**: Used Python libraries (Pandas, Matplotlib, Seaborn) to analyze trends and patterns.
- **Interactive Dashboard**: Created a Power BI dashboard with KPI cards, charts, and slicers for dynamic exploration.
- **Clear Insights**: Summarized key findings to support data-driven decision-making.

## Key Insights

- **Top Performing Category**: "Clothing" is the leading product category in both sales revenue and quantity sold.
- **Sales Trend**: Sales show a cyclical pattern, with peaks and troughs that suggest seasonal influences.
- **Customer Behavior**: The majority of transactions are for smaller quantities, indicating a pattern of frequent, small-scale purchases.
- **Gender Distribution**: Sales are almost evenly split between male and female customers, suggesting a broad market appeal.

## Setup and Usage

To run this project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    ```
2.  **Install Python dependencies**:
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  **Run the EDA script**:
    ```bash
    python notebooks/eda.py
    ```
4.  **View the Power BI Dashboard**:
    - Open `powerbi/Retail_Sales_Dashboard.pbix` in Power BI Desktop.
    - Ensure you have the `data/cleaned_retail_sales_dataset.csv` file in the correct path for the dashboard to load the data.

## File Structure

```
retail_sales_project/
├── data/
│   ├── retail_sales_dataset.csv (raw data)
│   └── cleaned_retail_sales_dataset.csv (cleaned data)
├── notebooks/
│   └── eda.py (Python script for EDA)
├── powerbi/
│   ├── Retail_Sales_Dashboard.pbix (Power BI file)
│   └── Retail_Sales_Dashboard.pdf (PDF of dashboard)
├── docs/
│   ├── power_bi_guide.md
│   ├── key_insights.md
│   └── ... (visualization images)
└── README.md
```


