import sys
sys.path.insert(0, 'Dynamixel_sevo_module')
import dynamixel

def multiread(ID):
    pos = {}
    for x in ID:
        rpos = dynamixel.read(x)
        pos[x] = (rpos/1023*300)        
    return pos

def multiInt(ID):
    for x in ID:
        dynamixel.init(x)

def robotControl(ID, TimeR, Dego,pos):

    Time = []
    dgs  = []
    dgd  = []
    Deg  = []
    for i in range(len(TimeR)):
        if TimeR[i] == 0: TimeR[i] = 1  

    for x in TimeR:
        Time.append(x)
    for x in range(len(ID)):
        Deg.append(abs(Dego[x]-pos[ID[x]]))

    for q in range(len(ID)):
        dgp=Deg[q]
        dgt=Time[q]
        dgts = Dego[q]
        dgs.append(int((dgp*1023/300)/(dgt*0.002)))
        dgd.append(int(dgts*1023/300))
        if dgd[q] > 1023: dgd[q] = 1023
        if dgs[q] > 1023: dgs[q] = 1023
        if dgd[q] <= 0: dgd[q] = 1
        if dgs[q] <= 0: dgs[q] = 1
    dynamixel.multiMove(ID,dgd,dgs)