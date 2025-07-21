# Retail Sales Analysis & Power BI Dashboard

An end-to-end data analysis and dashboarding project using **Python** and **Power BI**. This project performs detailed Exploratory Data Analysis (EDA) on retail sales data and visualizes key trends and insights through an interactive Power BI dashboard.

📊 Includes a full `.pbix` Power BI file, EDA Python scripts, and visual assets.

**📦 Repository:** [https://github.com/ahsankhizar5/Retail-Sales-Analysis-Python-PowerBI](https://github.com/ahsankhizar5/Retail-Sales-Analysis-Python-PowerBI)

---
## 📊 Dashboard Preview

![Retail Dashboard](graphs/Dashboard%20Overview.png)

Explore the full dashboard by opening the `.pbix` file in Power BI Desktop. All visuals are interactive and support filtering by region, gender, and product categories.

---

## ✨ Features

* 🧹 **Data Cleaning**: Handled missing values and duplicates for clean insights  
* 📈 **Exploratory Data Analysis (EDA)**: Python-based EDA using `pandas`, `matplotlib`, and `seaborn`  
* 📊 **Interactive Dashboard**: Built with Power BI for dynamic KPI viewing and slicing  
* 📌 **Key Insights Highlighted**: Includes business-level summaries from sales and customer trends  
* 🖼️ **Dashboard Screenshot**: Visual preview inside README  
* 📁 **Organized Structure**: Includes `data/`, `code/`, `graphs/`, and `powerbi/` folders for clarity  
* 📄 Includes: `Retail_Sales_Dashboard.pbix`, EDA script, and optional PDF report

---

## 🧠 Key Insights

- **Top Performing Category**: *Clothing* led both in revenue and quantity sold  
- **Sales Pattern**: Clear cyclical/seasonal trends identified in monthly data  
- **Customer Behavior**: Most purchases are frequent and small-quantity based  
- **Gender Split**: Nearly equal male-female purchase behavior, indicating broad product appeal

---


## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/ahsankhizar5/Retail-Sales-Analysis-Python-PowerBI.git
cd Retail-Sales-Analysis-Python-PowerBI
````

### 2. **Install Python Requirements**

```bash
pip install pandas matplotlib seaborn
```

> ✅ Requires Python 3.x and Power BI Desktop installed.

### 3. **Run the EDA Script**

```bash
python code/eda.py
```

### 4. **Open the Power BI Dashboard**

* Launch Power BI Desktop
* Open `powerbi/Retail_Sales_Dashboard.pbix`
* Make sure `data/cleaned_retail_sales_dataset.csv` is in place

---

## 🗂 Folder Structure

```
Retail-Sales-Analysis-Python-PowerBI/
├── data/
│   ├── retail_sales_dataset.csv                # Raw data
│   └── cleaned_retail_sales_dataset.csv        # Processed data
├── code/
│   └── eda.py                                  # Python script for EDA
├── powerbi/
│   ├── Retail_Sales_Dashboard.pbix             # Power BI file
│   └── Retail_Sales_Dashboard.pdf              # Exported dashboard as PDF
├── docs/
│   └── power_bi_guide.md                       # Optional documentation
├── graphs/
│   └── Dashboard Overview.png                  # Dashboard preview image
└── README.md
```

---

## 🛠️ Tech Stack

* **Python** – Data manipulation & visualization
* **Pandas, Matplotlib, Seaborn** – For EDA
* **Power BI Desktop** – For dashboard building
* **CSV** – Flat-file based data storage

---

## 🤝 Want to Contribute?

1. **Fork this repository**
2. **Create a new feature branch**

```bash
git checkout -b feature/your-feature
```

3. **Commit your changes**

```bash
git commit -m "Add your feature"
```

4. **Push and submit a pull request**

```bash
git push origin feature/your-feature
```

---

## 📄 License

MIT License — free to use, reuse, and adapt with credit.

---

## 🌟 Give a Star

If you found this project useful, insightful, or inspiring — feel free to ⭐ it on GitHub!

---

> 💡 *"Great dashboards don’t just tell you what happened — they help you see what to do next."*

```