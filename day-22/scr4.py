# Data Cleaning : Removing all the Unwanted Values

data = ["orange", "", "", "banana", "", "apple", "", "", "", "kiwi", ""]
clean_data = [item for item in data if item]

print(f"UnCleaned Data : {data}")
print(f"Cleaned Data : {clean_data}")
