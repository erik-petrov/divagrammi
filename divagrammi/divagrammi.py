import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(-12,12,1)
y = -1/18*x**2+12

x1 = np.arange(-4,4,1)
y1 = -1/8*x1**2+6

x2 = np.arange(-12,-4,1)
y2 = -1/8*(x2+8)**2+6

x3 = np.arange(4,12,1)
y3 = -1/8*(x3-8)**2+6

x4 = np.arange(-4,-0.3,1)
y4 = 2*(x4+3)**2-9

x5 = np.arange(-4,0.2,1)
y5 = 1.5*(x5+3)**2-10

plt.subplots()
plt.title("Зонтик")
plt.tick_params(axis="x", direction="in",length=5, width=5,color="red",labelsize=7)
plt.grid(True)
plt.plot(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5 ,'-r',linewidth=5)
plt.show()
#-----------------------------------------------------------------------------------------
with open("dannie.txt","r") as f:
    strs=[]
    ints=[]
    for line in f:
        n=line.find(",")
        strs.append(line[0:n].strip())
        ints.append(int(line[n+1:len(line)].strip()))

title = "Survey of where is Python used."
explode = (0.07,0,0,0,0)
plt.grid(True)

ax = plt.subplot()
wedges, texts, autotexts = ax.pie(ints, explode=explode, autopct='%1.1f%%',pctdistance=1.13)
ax.set_title("What operating systems Python programmers use.")
plt.axis('equal')
plt.tight_layout()
plt.legend(wedges, strs, loc='center left')

plt.show()