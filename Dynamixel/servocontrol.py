import dynamixel

def multiInt(ID):
    '''
    :param ID: input: ID massive
    :return:   initialization dynamixel
    '''
    for x in ID:
        dynamixel.init(x)

def robotControl(ID, TimeR, Dego):
    '''
    this function make syncmove with servo's
    :param ID:    input: ID massive
    :param TimeR: input: Time massive, in ms
    :param Dego:  input: Degrees
    :return:servo move
    '''
    Time = []
    for x in TimeR:
        Time.append(x)
    pos=[]
    for x in ID:
        rpos = dynamixel.read(x)
        pos.append(rpos/1023*300)
    Deg=[]
    for x in range(len(ID)):
        Deg.append(abs(Dego[x]-pos[x]))
    dgs=[] #dynamixel goal speed
    dgd=[] #dynamixel goal deg

    for q in range(len(ID)):
        dgp=Deg[q]
        dgt=Time[q]
        dgts = Dego[q]
        dgs.append(int((dgp*1023/300)/(dgt*0.004)))
        dgd.append(int(dgts*1023/300))
        if dgd[q] > 1023: dgd[q] = 1023
        if dgs[q] > 1023: dgs[q] = 1023
        if dgd[q] <= 0: dgd[q] = 1
        if dgs[q] <= 0: dgs[q] = 1
    dynamixel.multiMove(ID,dgd,dgs)