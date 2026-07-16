import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_excel("data/Sales_Data_Visualization_Dataset.xlsx")

print("Dataset Loaded Successfully!\n")

print(df.head())

# Set style
sns.set_style("whitegrid")

# -----------------------------
# 1. Bar Chart - Sales by Category
# -----------------------------
plt.figure(figsize=(8,5))
df.groupby("Category")["Sales"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/sales_by_category.png")
plt.show()

# -----------------------------
# 2. Pie Chart - Sales by Region
# -----------------------------
plt.figure(figsize=(6,6))
df.groupby("Region")["Sales"].sum().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/sales_by_region.png")
plt.show()

# -----------------------------
# 3. Histogram - Sales Distribution
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=8)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("images/sales_histogram.png")
plt.show()

# -----------------------------
# 4. Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("images/sales_vs_profit.png")
plt.show()

# -----------------------------
# 5. Heatmap
# -----------------------------
plt.figure(figsize=(6,4))
sns.heatmap(
    df[["Sales", "Profit", "Quantity"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/heatmap.png")
plt.show()

# -----------------------------
# 6. Box Plot
# -----------------------------
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Sales"])
plt.title("Sales Box Plot")
plt.tight_layout()
plt.savefig("images/boxplot.png")
plt.show()

print("\nProject Completed Successfully!")
print("Charts have been saved in the 'images' folder.")