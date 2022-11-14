#all module will be imported here

import pandas as pd
import statistics 
import plotly.express as px
import csv
import plotly.graph_objects as go
import numpy as np
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt

#ploting the graph
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df,y="quant_saved",color="rem_any")
fig.show()

#Making bar graph and calculation of Mean mode and median

with open("savings_data_final.csv", newline = "" ) as f:
    reader = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

# Finding Total number of people and number of people who were reminded

total_entries = len(savings_data)
total_people_given_reminded = 0

for data in savings_data:
    if int(data[3]) == 1:
        total_people_given_reminded +=1

fig = go.Figure(go.Bar(x = ["Reminded","Not Reminded"], y = [total_people_given_reminded,(total_entries-total_people_given_reminded)]))
fig.show()

#Mean,Median and Mode of savings
all_savings = []
for data in savings_data:
    all_savings.append(float(data[0]))

print(f"Mean of savings - {statistics.mean(all_savings)}")
print(f"Median of savings - {statistics.median(all_savings)}")
print(f"Mode of savings - {statistics.mode(all_savings)}")


print("\n")
#Calculating the Mean,Median and Mode of savings which are reminded and not reminded
reminded_savings = []
not_reminded_savings = []

for data in savings_data:
    if int(data[3]) == 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))

print(f"Results for people who was reminded to save")
print(f"Mean of savings - {statistics.mean(reminded_savings)}")
print(f"Median of savings - {statistics.median(reminded_savings)}")
print(f"Mode of savings - {statistics.mode(reminded_savings)}")
#To add new lines
print("")
print("Results for people who ws not reminded to save")
print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")
print(f"Median of savings - {statistics.median(not_reminded_savings)}")
print(f"Mode of savings - {statistics.mode(not_reminded_savings)}")

print("")

#Calculating the Standard Deviation
print(f"Standard deviation of all the data - {statistics.stdev(all_savings)}")
print(f"Standard Deviation of people who were reminded - {statistics.stdev(reminded_savings)}")
print(f"Standard Deviation of people who wre not reminded - {statistics.stdev(not_reminded_savings)}")

print("")
#Calculating the Correlation between age of person and there savings
age = []
savings = []

for data in savings_data:
    if float(data[5]) !=0:
        age.append(float(data[5]))
        savings.append(float(data[0]))

correlation = np.corrcoef(age,savings)
print(f"Correlation between age of person and there savings - {correlation[0,1]}")

# Making and displot
fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist=False)
fig.show()

#creating and Boxplot
plt.boxplot(data=df, x=df["quant_saved"])






