# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:22:19 2023

@author: sr22aar
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

d = pd.read_excel(r'C:/Users/sr22aar/Downloads/Book3.xlsx')
# print(d.columns)


def count_of_cve(data):
    """The given code defines a function named count_of_cve that takes a single argument data, which is the path of an Excel file containing vulnerability data. The function reads the Excel file and extracts the 'YEAR' column, then adds a new column named 'count of cve' and sets its value to 1. It then groups the data by year and sums the count of vulnerabilities for each year.

The function then plots the data using Matplotlib library. It creates a line plot of year vs. count of vulnerabilities, with dots representing each year's count. It also sets the x-axis label as "Year of cve", the y-axis label as "Count of cve", and the title of the plot as "Count_of_Vulnerability".

The function does not return anything and instead prints the resulting DataFrame and shows the plot using the plt.show() function. The path of the Excel file must be passed as an argument to the function in order to run it successfully."""
    df = pd.read_excel(data)
    df = df[['YEAR']]
    df['count of cve'] = 1
    df = df.groupby("YEAR").sum()
    print(df)
    name = df.index
    price = df['count of cve']
    plt.figure(figsize=(10, 7))
    plt.plot(name, price)
    plt.xlabel("Year of cve")
    plt.ylabel("Count of cve")
    plt.title("Count_of_Vulnerability")
    plt.scatter(name, price)
    plt.plot(color='r')
    plt.show()


count_of_cve(r'C:/Users/sr22aar/Downloads/Book3.xlsx')


df = d[['YEAR']]
df['count of cve'] = 1
df = df.groupby("YEAR").sum()
# print(df)
name = df.index
price = df['count of cve']

# Figure Size
#fig = plt.figure(figsize =(10, 7))


# Horizontal Bar Plot
"""plt.bar(name, price)
fig, ax = plt.subplots(figsize =(16, 9))
ax.barh(name, price)
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks


# Add padding between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# Add x, y gridlines
ax.grid(b=True, color='grey',
        linestyle='-.', linewidth=0.5,
        alpha=0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
             str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold',
             color='red')

# Add Plot Title
ax.set_title('Vulnerability count',
             loc='center', )


#plt.yticks(y, df.index)
# Show Plot
plt.show()"""


def plot_vulnerability_count(name, price):
    plt.bar(name, price)
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.barh(name, price)

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='red')

    # Add Plot Title
    ax.set_title('Vulnerability count',
                 loc='center', )

    # Show Plot
    plt.show()


plot_vulnerability_count(name, price)


t = d[["status"]]
t['count of cve'] = 1
t = t.groupby("status").sum()
y = list(t['count of cve'])
mylabels = list(t.index)

"""plt.pie(y, labels = mylabels, startangle = 90,autopct='%1.1f%%')
plt.title("status of each vulnerability")
plt.show()"""


def plot_vulnerability_status(y, mylabels):
    plt.pie(y, labels=mylabels, startangle=90, autopct='%1.1f%%')
    plt.title("Status of each vulnerability")
    plt.show()


`plot_vulnerability_status(y, mylabels)


f = d[['YEAR', 'status']]
f['RESERVED'] = 0
f['PUBLIC'] = 0
f['REJECTED'] = 0
f['DISPUTED'] = 0

for i in range(len(f)):
    print(i)
    if f['status'][i] == "RESERVED":
        f['RESERVED'][i] = 1
    elif f['status'][i] == "REJECTED":
        f['REJECTED'][i] = 1
    elif f['status'][i] == "PUBLIC":
        f['PUBLIC'][i] = 1
    elif f['status'][i] == "DISPUTED":
        f['DISPUTED'][i] = 1
f = f.groupby("YEAR").sum()
# print(f)
# create data
x = list(f.index)
y1 = np.array(list(f['PUBLIC']))
y2 = np.array(list(f['RESERVED']))
y3 = np.array(list(f['DISPUTED']))
y4 = np.array(list(f['REJECTED']))
# print(len(x),len(y1),len(y2),len(y3),len(y4))
# print(y2+y1)
# plot bars in stack manner

plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')
plt.xlabel("Year")
plt.ylabel("Count of Vulnerability")
plt.legend(["PUBLIC", "RESERVED", "DISPUTED", "REJECTED"])
plt.title("Count of Vulnerability year wise with its respective status")
plt.show()
