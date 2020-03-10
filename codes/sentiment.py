import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import re

from scipy.interpolate import make_interp_spline, BSpline

data = pd.read_csv("hair_dryer_csv.csv")
df = pd.DataFrame(data)
for i in range(len(df['review_date'])):
    df['review_date'][i] = df['review_date'][i][:6] + '20' + df['review_date'][i][6:]
df['review_date'] = pd.to_datetime(df['review_date'], format='%m/%d/%Y')

print(df['review_date'].describe())
Mean = []
temp = []
for i in range(len(df['review_date'])):
    if df['review_date'][i].year <= 2007: temp.append(i)
Mean.append(df.loc[temp]['star_rating'].mean())

for year in range(2008, 2016, 1):
    temp = []
    for i in range(len(df['review_date'])):
        if df['review_date'][i].year == year: temp.append(i)
    Mean.append(df.loc[temp]['star_rating'].mean())
T = np.array(range(2007, 2016, 1))
xnew = np.linspace(T.min(), T.max(), 1000)
spl = make_interp_spline(T, Mean, k=3)
power_smooth = spl(xnew)
# plt.figure()
plt.subplot(1,3,1)
plt.plot(xnew, power_smooth)

plt.title('Pacifier')
plt.ylabel(u'Mean Star Rating')
plt.xlabel(u'Year')
plt.ylim([1,5])

data = pd.read_csv("microwave_csv.csv")
df = pd.DataFrame(data)
for i in range(len(df['review_date'])):
    df['review_date'][i] = df['review_date'][i][:6] + '20' + df['review_date'][i][6:]
df['review_date'] = pd.to_datetime(df['review_date'], format='%m/%d/%Y')

print(df['review_date'].describe())
Mean = []
temp = []
for i in range(len(df['review_date'])):
    if df['review_date'][i].year <= 2007: temp.append(i)
Mean.append(df.loc[temp]['star_rating'].mean())

for year in range(2008, 2016, 1):
    temp = []
    for i in range(len(df['review_date'])):
        if df['review_date'][i].year == year: temp.append(i)
    Mean.append(df.loc[temp]['star_rating'].mean())
T = np.array(range(2007, 2016, 1))
xnew = np.linspace(T.min(), T.max(), 1000)
spl = make_interp_spline(T, Mean, k=3)
power_smooth = spl(xnew)
# plt.figure()
plt.subplot(1,3,2)
plt.plot(xnew, power_smooth)

plt.title('Pacifier')
plt.ylabel(u'Mean Star Rating')
plt.xlabel(u'Year')
plt.ylim([1,5])

data = pd.read_csv("pacifier_csv.csv")
df = pd.DataFrame(data)
for i in range(len(df['review_date'])):
    df['review_date'][i] = df['review_date'][i][:6] + '20' + df['review_date'][i][6:]
df['review_date'] = pd.to_datetime(df['review_date'], format='%m/%d/%Y')

print(df['review_date'].describe())
Mean = []
temp = []
for i in range(len(df['review_date'])):
    if df['review_date'][i].year <= 2007: temp.append(i)
Mean.append(df.loc[temp]['star_rating'].mean())

for year in range(2008, 2016, 1):
    temp = []
    for i in range(len(df['review_date'])):
        if df['review_date'][i].year == year: temp.append(i)
    Mean.append(df.loc[temp]['star_rating'].mean())
T = np.array(range(2007, 2016, 1))
xnew = np.linspace(T.min(), T.max(), 1000)
spl = make_interp_spline(T, Mean, k=3)
power_smooth = spl(xnew)
# plt.figure()
plt.subplot(1,3,3)
plt.plot(xnew, power_smooth)

plt.title('Pacifier')
plt.ylabel(u'Mean Star Rating')
plt.xlabel(u'Year')
plt.ylim([1,5])

plt.show()

