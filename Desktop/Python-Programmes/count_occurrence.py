tupl = (50, 10, 60, 70, 50)
try:
    key = float(input("Enter search key: "))
    print(f"The number of occurrence of {key} = {tupl.count(key)}")
except ValueError:
    print("Key should be fractional value")