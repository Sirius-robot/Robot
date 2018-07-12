import botcontrol
from DataBase import *
import threading
#database.data[i][1][j][1]
x = database.gesture(gesname)

p=0
l=0
m=0
u=0
y = []
c = []
z = []
v = []

#database.del_gesture(TITLE, gesname)
for k in x:
    y.append(x[u])
  #  print(y)
    for f in y:
        z.append(y[p])
        #print(z[p])
        p=p+1
        for g in z:
            c.append(z[l])
            print(c[l])
            l=l+1
            for h in c:
                v.append(c[m])
                m=m+1




y0=x[0]
y1=x[1]
y2=x[2]
z1=y0[1]
c0=z1[1] #module
v0=z1[2] #var
print(z1[1])

database.del_gesture(TITLE, gesname)

#botcontrol.multiInt((1,2,3,4))
#botcontrol.robotControl((1,2,3,4),(1023,6000,10000,20000),(30,300,300,300))

def timer():
    threading.Timer(0.04,botcontrol.robotControl((1,2,3,4),(1023,6000,10000,20000),(30,300,300,300))).start()
    threading.Timer(0.04,timer).start()
    print("Hi")
#timer()
