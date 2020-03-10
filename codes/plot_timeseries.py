import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
import re
from scipy.interpolate import spline




def star_rating(df):
    for i in range(len(df['review_date'])):
        df['review_date'][i] = df['review_date'][i][:6]+'20'+df['review_date'][i][6:]
    df['review_date']=pd.to_datetime(df['review_date'], format = '%m/%d/%Y')

    # min = 2002
    # max = 2015
    
    print(df['review_date'].describe())
    Mean = []
    temp=[]
    for i in range(len(df['review_date'])):
            if df['review_date'][i].year <=2007 : temp.append(i)
    Mean.append(df.loc[temp]['star_rating'].mean())

    for year in range(2008, 2016, 1):
        temp= []
        for i in range(len(df['review_date'])):
            if df['review_date'][i].year == year: temp.append(i)
        Mean.append(df.loc[temp]['star_rating'].mean())
    T = np.array(range(2007, 2016,1))
    xnew = np.linspace(T.min(), T.max(), 300)  

    power_smooth = spline(T, Mean, xnew)

    plt.plot(xnew,power_smooth)

    # plt.plot(range(2007, 2016, 1),Mean)
    plt.title('Microwave')
    plt.ylabel(u'Mean Star Rating')
    plt.xlabel(u'Year')
    plt.grid(True)
    plt.show()

def main():
    data = pd.read_csv("~/Desktop/MCM2020/data_csv/hair_dryer_csv.csv")
    df = pd.DataFrame(data)
    star_rating(df)

if __name__ == "__main__":
    main()