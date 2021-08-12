import pandas as pd
import plotly.express as px
import codecs
import os
import sys

'''
DOCUMENTATION - https://plotly.com/python/bar-charts/
'''

df = pd.read_excel("raw.xlsx")

# renaming dataframe columns
df.columns = ['Rank', 'Country', 'Gold', 'Silver', 'Bronze', 'Total']

# renaming country values to list
countries = df['Country'].to_list()

csv_file = codecs.open("medals.csv","w",encoding="utf8")
head = "Country,medal,count\n"
csv_file.write(head)
for country in countries:
    # medal counts
    g = df[df['Country']==country]['Gold'].to_list()[0]
    s = df[df['Country']==country]['Silver'].to_list()[0]
    b = df[df['Country']==country]['Bronze'].to_list()[0]
    country = country.replace(",", "|")
    genstr = country + "," + "gold" + "," + str(g) + "\n" + country + "," + "Silver" + "," + str(s) + "\n" + country + "," + "Bronze" + "," + str(b) + "\n"
    csv_file.write(genstr)

csv_file.close()

medal_df = pd.read_csv("medals.csv")
medal_df.to_excel("2004.xlsx")
