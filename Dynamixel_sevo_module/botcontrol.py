import dynamixel
from time import sleep
z=[1,2,3,4,5,6]
for x in z:
 dynamixel.init(x)
pos=[0,0,0,0,0,0]
q=0
w=1
for x in z:
 rpos = dynamixel.read(w)
 dgd = int(rpos/1023*300)
 pos[q] = dgd
 print(pos[q])
 q=q+1
 w=w+1
def robotControl(ID,Time,Dego):
    q=0
    w=1
    Deg=[0,0,0,0,0,0]
    for f in pos:
        Deg[q]=abs(Dego[q]-pos[q])
        print(Deg[q])
        q = q + 1
    q=0
    w=0
    e=1
    r=0
    t=1
    for h in range(3):
        dgp=Deg[q]
        dgt=Time[q]
        dgts = Dego[q]
        dgp2 = Deg[t]
        dgt2 = Time[t]
        dgts2 = Dego[t]
        dgs = int((dgp*1023/300)/(dgt*2))
        dgd = int(dgts*1023/300)
        dgs2 = int((dgp2*1023/300)/(dgt2*2))
        dgd2 = int(dgts2*1023/300)
        dynamixel.multiMove((ID[w],ID[e]),(dgd,dgd2),(dgs,dgs2))
        q=q+2
        w=w+2
        e=e+2
        r=r+2
        t=t+2