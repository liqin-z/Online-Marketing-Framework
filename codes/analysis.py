import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline, BSpline

plt.rcdefaults()

dryer = open("dryer.txt", "r")
micro = open("microwave.txt", "r")
pacif = open("pacifier.txt", "r")

dryscore = [20.2, 19.7, 19.5, 18.6, 18.1, 18, 17.85, 17.55, 17.38, 17.3]
pacscore = [19.5, 19.0, 18.4, 17.85, 17.73, 17.62, 17.55, 17.4, 17.32, 17.3]
score = [16.4, 13.82, 13.77, 13.7, 13.55, 13.44, 13.33, 12.55, 12.36, 12.11]

saled = []
salem = []
salep = []
strd = "Top10 Sales of Hair Dryer"
strm = "Top10 Sales of Microwave"
strp = "Top10 Sales of Pacifier"

for i in dryer:
    saled.append(int(i))

for i in micro:
    salem.append(int(i))

for i in pacif:
    salep.append(int(i))



def plot(sale, str):
    labels = [i for i in range(1, 11)]
    y_pos = np.arange(len(labels))
    plt.bar(y_pos, sale, align='center', alpha=0.5, color=['r'])

    plt.xlabel('Product index')
    plt.ylabel('Product Sales')
    plt.title(str)
    plt.xticks(range(len(sale)), labels)
    plt.bar(range(len(sale)), sale, color='r',alpha=0)

    ax2 = plt.twinx()
    xnew = np.linspace(0, 10, 300)
    T = np.array(range(0, 10, 1))
    spl = make_interp_spline(T, score, k=3)
    power_smooth = spl(xnew)

    ax2.plot(xnew, power_smooth, 'slateblue', alpha=0.8, linewidth = 3)
    ax2.set_xlim([-1, 11])
    ax2.set_ylim([8.7,17.5])
    ax2.set_ylabel('Comprehensive Score')
    # ax2.set_xlabel('Same X for both exp(-x) and ln(x)')

    plt.show()


# plot(saled, strd)
plot(salem,strm)
# plot(salep,strp)