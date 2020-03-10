
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import csv
#
with open('theta0.3/p1.csv') as csvfile:
    reader = csv.reader(csvfile)
    times = ['20'+row[0].strip()+'/'+row[1].strip() for row in reader]

with open('theta0.3/p1.csv') as csvfile:
    reader = csv.reader(csvfile)
    score3 = [float(row[2]) for row in reader]

with open('theta0.5/p1.csv') as csvfile:
    reader = csv.reader(csvfile)
    score5 = [float(row[2]) for row in reader]

with open('theta0.7/p1.csv') as csvfile:
    reader = csv.reader(csvfile)
    score7 = [float(row[2]) for row in reader]
#
# print(score)
print(times)
# x=[i for i in range(1,len(score)+1)]
#
# # fig = plt.figure()
# #设置X轴标签
# # plt.xlabel('X')
# #设置Y轴标签
# plt.ylabel('Y')
# plt.scatter(x,score,c='orange',marker = 'o',alpha=0.6,label='theta = 0.3')
# #设置图标
# plt.legend('theta')
# #显示所画的图
# # plt.show()

from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# 生成横纵坐标信息
xs = [datetime.strptime(d, '%Y/%m').date() for d in times]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())

xnew = np.linspace(xs.min(), xs.max(), 300)  # 300 represents number of points to make between T.min and T.max

p3 = BSpline(xs, score3, xnew)

plt.plot(xs, p3,label='0.3')
plt.plot(xs, score5)
plt.plot(xs, score7)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()