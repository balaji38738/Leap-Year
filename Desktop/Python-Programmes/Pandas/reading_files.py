import pandas as pd
casts = pd.read_csv("cast.csv", index_col=None)

# Prints first 5 entries
print(casts.head())
print("First 5 entries", casts.tail(), sep="\n")

# Prints last 5 entries
print("Last 5 entries", casts.tail(), sep="\n")

pd.set_option("max_rows", 2, "max_columns", 2)
print(casts)

# Prints no of rows in casts
print(len(casts))