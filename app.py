import pandas as pd
import glob
import os

# Load all CSV files from the data directory
csv_dir = os.path.join(os.path.dirname(__file__), "data")
csv_files = sorted(glob.glob(os.path.join(csv_dir, "*.csv")))

# Read and concatenate all CSV files into a single DataFrame
df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Clean the price column (remove '$' sign) and convert to float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Calculate sales for each row
df["sales"] = df["price"] * df["quantity"]

# Print total number of sales
total_sales = df["sales"].sum()
print(f"Merged {len(csv_files)} CSV files ({len(df)} rows)")
print(f"Total Sales: ${total_sales:,.2f}")