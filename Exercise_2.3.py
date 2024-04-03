#Read from CSV-file weight-height.csv to numpy-table information about the lengths and weights (in inches and pounds) of a group of students. Collect the lengths for the variable "length" and the weights for the variable "weight" by cutting the table.
#Convert lengths from inches to centimeters and weights from pounds to kilograms.
#Finally, calculate the means, medians, standard deviations, and variances of the lengths and weights.

import pandas as pd
import seaborn as sns
import matpotlib.pyplot as plt
sns.set()

df = pd.read_csv(r'C:\***\weight.csv',sep=";")

df1["Weight"] = df["Weight"] * 0.45
df2["Height"] = df["Height"] * 2.45

print.(df.head))
print.(df.columns))
print.(df.describe))
