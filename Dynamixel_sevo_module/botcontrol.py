import dynamixel

def multiInt(ID):
    '''
    :param ID: input: ID massive
    :return:   initialization dynamixel
    '''

    for x in ID:
        dynamixel.init(ID[x])

def robotControl(ID, TimeR, Dego):
    '''
    this function make syncmove with servo's
    :param ID:    input: ID massive
    :param TimeR: input: Time massive, in ms
    :param Dego:  input: Degrees
    :return:servo move
    '''
    n=0
    Time = []
    for x in ID:
        Time.append(int(TimeR[n]/1000))
        n=n+1
    y = 0
    for k in ID:
        y = y + 1
    y = int(y / 2)
    q=0#Massive position index
    w=1#ID index
    pos=[0,0,0,0,0,0]
    for x in ID:
        rpos = dynamixel.read(w)
        dgd = int(rpos/1023*300)
        pos[q] = dgd
        print(pos[q])
        q=q+1
        w=w+1
    q=0#Massive position index
    w=1#ID index
    Deg=[0,0,0,0,0,0]
    for f in ID:
        Deg[q]=abs(Dego[q]-pos[q])
        print(Deg[q])
        q = q + 1
    q=0 #Massive position index
    dgs=[] #dynamixel goal speed
    dgd=[] #dynamixel goal deg

    for h in ID:
        dgp=Deg[q]
        dgt=Time[q]
        dgts = Dego[q]
        dgs.append(int((dgp*1023/300)/(dgt*2)))
        dgd.append(int(dgts*1023/300))
        if dgd[q] > 1023: dgd[q] = 1023
        if dgs[q] > 1023: dgs[q] = 1023
        if dgd[q] <= 0: dgd[q] = 1
        if dgs[q] <= 0: dgs[q] = 1
        q=q+1
        w=w+1
    dynamixel.multiMove(ID,dgd,dgs)