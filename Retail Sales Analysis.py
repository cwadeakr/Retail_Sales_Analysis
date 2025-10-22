#  Import python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load csv file
df = pd.read_csv("Retail and wherehouse Sale.csv")
# Display first few rows
print(df.head())
print(df.columns)
print(df.isnull().sum())
print("Columns in dataset:", df.columns.tolist())

# Inspect and clean data
df.columns = df.columns.str.strip().str.upper()
df.drop_duplicates(inplace=True)
df.dropna(subset=["RETAIL SALES", "SUPPLIER"], inplace=True)

# Basic info and summary
print(df.info())
print(df.describe())
print("Missing values:\n", df.isna().sum())

df["TOTAL SALES"] = df["RETAIL SALES"] + df["WAREHOUSE SALES"]
df["YEAR_MONTH"] = df["YEAR"].astype(str) + "-" + df["MONTH"].astype(str).str.zfill(2)

# Key Performance Indicators (KPIs)
total_sales = df["TOTAL SALES"].sum()
avg_monthly_sales = df.groupby(["YEAR", "MONTH"])["TOTAL SALES"].sum().mean()
top_supplier = df.groupby("SUPPLIER")["TOTAL SALES"].sum().idxmax()
top_item = df.groupby("ITEM DESCRIPTION")["TOTAL SALES"].sum().idxmax()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Monthly Sales: ${avg_monthly_sales:,.2f}")
print(f"Top Supplier: {top_supplier}")
print(f"Top Selling Item: {top_item}")

# Visualization setup
plt.style.use("default")

# Monthly Sales Trend
monthly_sales = df.groupby("YEAR_MONTH")["TOTAL SALES"].sum().reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_sales, x="YEAR_MONTH", y="TOTAL SALES", marker="o")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Supplier Performance
top_suppliers = df.groupby("SUPPLIER")["TOTAL SALES"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_suppliers.values, y=top_suppliers.index)
plt.title("Top 10 Suppliers by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Supplier")
plt.tight_layout()
plt.show()

# Category (Item Type) Performance
item_type_sales = df.groupby("ITEM TYPE")["TOTAL SALES"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=item_type_sales.index, y=item_type_sales.values)
plt.title("Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()

# Warehouse vs Retail Comparison
sales_compare = df[["RETAIL SALES", "WAREHOUSE SALES"]].sum()
plt.figure(figsize=(6,5))
sns.barplot(x=sales_compare.index, y=sales_compare.values)
plt.title("Retail vs Warehouse Sales Comparison")
plt.tight_layout()
plt.show()





