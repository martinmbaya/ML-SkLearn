import pandas as pd
import numpy as np

name = "Automobile.csv"
# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv(name,header=None, names=headers, na_values="?" )
print(df.head())
print(df.dtypes)

"""
#Build a new dataframe containing only the object columns
obj_df = df.select_dtypes(include=['object']).copy()
print(obj_df.head())
"""

#Check for null values
print(df[df.isnull().any(axis=1)])

#Check how many of each variables are in the attribute num_doors
print(df["num_doors"].value_counts())

#Fill the NaN attributes in num_doors with 4
df = df.fillna({"num_doors": "four"})

df["num_cylinders"].value_counts()
cleanup_nums = {"num_doors":     {"four": 4, "two": 2},
                "num_cylinders": {"four": 4, "six": 6, "five": 5, "eight": 8,
                                  "two": 2, "twelve": 12, "three":3 }}

#Replacing values with numbers directly
#Done when the attributes are a direct measure of the values being used to replace them
df.replace(cleanup_nums, inplace=True)
# print(obj_df.head())

print(df.dtypes)

#One Hot Encoding
df=pd.get_dummies(df, columns=["body_style", "drive_wheels"], prefix=["body", "drive"])

print(df.dtypes)
df.to_csv("Automobile_edit.csv", sep=',', encoding='utf-8')