
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\data\\retail_sales_dataset.csv")

# Convert 'Date' column to datetime objects
df["Date"] = pd.to_datetime(df["Date"])

# --- Data Cleaning (re-run for visualization script) ---
# (As identified in previous step, no missing values or duplicates, and outliers are kept)
df.drop_duplicates(inplace=True)

# --- Data Visualization ---

# Set style for plots
sns.set_style("whitegrid")

# 1. Sales trends over time
plt.figure(figsize=(12, 6))
df.set_index("Date")["Total Amount"].resample("M").sum().plot()
plt.title("Monthly Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\graphs\\monthly_sales_trend.png")
plt.close()

# 2. Product category performance
plt.figure(figsize=(10, 6))
sns.barplot(x="Product Category", y="Total Amount", data=df, estimator=sum, ci=None)
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\graphs\\sales_by_product_category.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(x="Product Category", y="Quantity", data=df, estimator=sum, ci=None)
plt.title("Total Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Quantity Sold")
plt.tight_layout()
plt.savefig("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\graphs\\quantity_by_product_category.png")
plt.close()

# 3. Profit and quantity sold (assuming Total Amount is revenue, and we don't have cost, so we'll visualize Total Amount and Quantity)
# Already covered in product category performance, but can also look at distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df["Total Amount"], bins=30, kde=True)
plt.title("Distribution of Total Amount")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
sns.histplot(df["Quantity"], bins=10, kde=True)
plt.title("Distribution of Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\graphs\\distribution_total_amount_quantity.png")
plt.close()

# 4. Region-wise sales (Assuming 'Customer ID' can be grouped to infer regions, or if there was a 'Region' column. 
# Since there isn't a 'Region' column, we'll skip this for now or infer later if possible. 
# For now, let's assume 'Customer ID' doesn't directly map to region for aggregate analysis.)
# If a region column existed, the code would be similar to product category performance.

# 5. Correlation heatmaps (for numerical columns)
plt.figure(figsize=(8, 6))
sns.heatmap(df[["Age", "Quantity", "Price per Unit", "Total Amount"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.savefig("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\graphs\\correlation_heatmap.png")
plt.close()

# --- Key Insights (will be summarized in README.md) ---

# Export the final cleaned dataset as a CSV for Power BI
df.to_csv("C:\\Users\\ahsan\\Downloads\\Retail Sales Project\\Final\\home\\ubuntu\\retail_sales_project\\data\\cleaned_retail_sales_dataset.csv", index=False)

print("EDA completed and visualizations saved to retail_sales_project/docs/")
print("Cleaned dataset saved to retail_sales_project/data/cleaned_retail_sales_dataset.csv")


