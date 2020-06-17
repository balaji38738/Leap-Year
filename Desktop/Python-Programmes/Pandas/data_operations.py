import pandas as pd

movies = pd.read_csv("titles.csv", index_col=None)
casts = pd.read_csv("cast.csv", index_col=None)

# Print records of title column
titles = movies["title"]
print(titles)

# Prints movies released after 1985
after85 = movies[movies["year"] > 1985]
print(after85)

# Prints all movies named macbeth
macbeth =  movies[movies["title"] == "Macbeth"]
print(macbeth)

# Prints movies sorted in ascending order of year
sorted_by_year = movies.sort_values("year")
print(sorted_by_year)

# Prints maximum year
print(movies["year"].max())

# Prints minimum year
print(movies["year"].min())

# Prints mean year
print(movies["year"].mean())

# Prints null records
new_casts = casts[casts["n"].isnull()].fillna("NA")
print(new_casts)