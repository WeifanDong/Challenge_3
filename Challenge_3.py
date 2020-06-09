#Challenge 3
#Name: Weifan Dong


#pip install pandas_datareader
import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'JP', 'CN'], start=2006, end=2010)
dat1 = wb.download(indicator='EG.USE.ELEC.KH.PC', country=['US', 'JP', 'CN'], start=2006, end=2010)

df=dat.merge(dat1, on=['country','year'], how='left')
df=df.reset_index()
df["year"]=pd.to_numeric(df["year"])
df=df.rename(columns={"NY.GDP.PCAP.KD":"GDP per capita",
                      "EG.USE.ELEC.KH.PC":"electic power cons per capita"})
df=df.sort_values(by="year")

grouped=df.groupby("country")
df["GDP percentage growth"]=grouped["GDP per capita"].pct_change()
china=df.loc[df["country"]=="China"]

# Finding 1
fig, ax = plt.subplots()
ax.plot(china["year"],china["GDP per capita"],marker='o', color='b',label="GDP")
ax.plot(np.NaN, marker='o', color='g',label="Electricity")
ax.legend(loc="best")

ax2=ax.twinx()
ax2.plot(china["year"],china["electic power cons per capita"], marker='o', color='g')

ax.set_ylabel("PC GDP ($)")
ax.set_xlabel("Year")
ax2.set_ylabel("PC Electricity Cons (kWh)")
ax.set_title("China PC GDP and Electricity Cons by Year")

print("Finding 1: Electrification is a good symbol of economic growth.")

# Finding 2
sns.set()
ax3=sns.lineplot(x="year",y="GDP percentage growth",hue="country",data=df)
ax3.axvspan(2008, 2009, alpha=0.5, color='red')
ax3.set_title("GDP Growth Difference in China, Japan and US")

print("During the financial crisis, US and Japan experienced negative GDP growth, whereas China was not really affected and was able to maintain relatively high growth in GDP per capita.")
