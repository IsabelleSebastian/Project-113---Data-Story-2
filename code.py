import pandas
import numpy
import random
import plotly.graph_objects as pg
import plotly.figure_factory as pf
import plotly.express as pe
import statistics as st

# reading data / creating list
df = pandas.read_csv("data.csv")
data = df["quant_saved"].tolist()

# finding/displaying quartiles
q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
q2 = q3-q1
print(f"Q1: {q1} Q2: {q2} Q3: {q3}")

# finding/displaying outliers
lowerWhisker = q1 - 1.5*q2
upperWhisker = q3 + 1.5*q2
print(f"Lower Whisker: {lowerWhisker} Upper Whisker: {upperWhisker}")

# creating new data set w/o outliers
newDf = df[ df["quant_saved"] < upperWhisker]
newData = newDf["quant_saved"].tolist()
newMean = st.mean(newData)
newMode = st.mode(newData)
newMedian = st.median(newData)
newStdev = st.stdev(newData)
print(f"Statistics of New Dataset: Mean= {newMean}  Mode= {newMode}  Median= {newMedian}  St.Dev= {newStdev}")
print("Population Mean: ", st.mean(data))

#-------------------------------data distance graphs---------------------------
# dist plot of old data
dist1 = pf.create_distplot([data], ["Old Data Distance Graph"])
dist1.show()

# dist plot of new dataset w/o outliers
dist = pf.create_distplot([newData], ["New Data Distance Graph"])
dist.show()

#-------------------------------data sampling & statistics---------------------
sampleList = []
for i in range(1000):
    s = []
    for b in range(100):
        s.append(random.choice(newData))

    sampleList.append(st.mean(s))

print("Sample Mean: ", st.mean(sampleList))
print("Sample Mode: ", st.mode(sampleList))
print("Sample Median: ", st.median(sampleList))
print("Sample St.Dev: ", st.stdev(sampleList))

