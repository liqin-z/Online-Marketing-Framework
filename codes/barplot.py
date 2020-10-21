import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcdefaults()

dryer = open("dryer.txt","r")
micro = open("microwave.txt","r")
pacif = open("pacifier.txt","r")

score = [20.7, 18.89, 18.5, 18.24,17.89]
x = [0,1,2,3,4]

saled = []
salem = []
salep = []
strd="Top5 Sales of Hair Dryer"
strm="Top10 Sales of Microwave"
strp="Top10 Sales of Pacifier"

for i in dryer:
    saled.append(int(i))

for i in micro:
    salem.append(int(i))

for i in pacif:
    salep.append(int(i))
    
print(saled)

def plot(sale, str):
    labels = [i for i in range(1,6)]
    y_pos = np.arange(len(labels))
    plt.bar(y_pos, sale, align='center', alpha=0.5)
    plt.xlabel('Product index')
    
    plt.title(str)
    plt.xticks(range(len(sale)), labels)
    plt.bar(range(len(sale)), sale)
    
    ax2 = plt.twinx()
    ax2.plot(x, score, 'g', linewidth = 5)
    ax2.set_xlim([-1, 5])
    # ax2.set_ylabel('Y values for ln(x)')
    # ax2.set_xlabel('Same X for both exp(-x) and ln(x)')
        
    plt.show()

plot(saled,strd)
# plot(salem,strm)
# plot(salep,strp)