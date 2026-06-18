# =========================
# RETAIL SALES ANALYSIS PROJECT
# Superstore Dataset
# =========================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------
# STEP 1: LOAD DATA
# -------------------------
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print(df.head())
print("\nDataset Shape:", df.shape)

# -------------------------
# STEP 2: CLEANING
# -------------------------
df.drop_duplicates(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df.isnull().sum())

# -------------------------
# STEP 3: BASIC INFO
# -------------------------
print(df.info())

# -------------------------
# STEP 4: GRAPH 1 - Sales by Category
# -------------------------
plt.figure()
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.savefig("graph1_sales_by_category.png")
plt.show()

# -------------------------
# STEP 5: GRAPH 2 - Profit by Region
# -------------------------
plt.figure()
sns.barplot(x="Region", y="Profit", data=df)
plt.title("Profit by Region")
plt.savefig("graph2_profit_by_region.png")
plt.show()

# -------------------------
# STEP 6: GRAPH 3 - Profit by Category
# -------------------------
plt.figure()
sns.barplot(x="Category", y="Profit", data=df)
plt.title("Profit by Category")
plt.savefig("graph3_profit_by_category.png")
plt.show()

# -------------------------
# STEP 7: TOP 10 PRODUCTS
# -------------------------
top_products = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

print(top_products)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Profitable Products")
plt.savefig("graph4_top_products.png")
plt.show()

# -------------------------
print("\nPROJECT COMPLETED SUCCESSFULLY!")
