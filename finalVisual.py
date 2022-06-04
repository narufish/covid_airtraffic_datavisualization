import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.read_csv("covid_impact_on_airport_traffic.csv")
print(df.head())

