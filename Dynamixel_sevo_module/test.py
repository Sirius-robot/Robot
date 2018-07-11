import dynamixel
from time import sleep
z=[1,2,3,4,5,6]
for x in z:
 dynamixel.init(x)
dynamixel.multiMove([1],[1000],[500])
sleep(1)
dynamixel.multiMove([1],[100],[500])
sleep(1)
dynamixel.multiMove([1],[1000],[500])
sleep(1.4)
dynamixel.multiMove([2,3],[750,750],[1000,900])
sleep(0.8)
dynamixel.multiMove([2,3],[500,500],[1000,1000])
sleep(0.8)
dynamixel.multiMove([2,3],[250,250],[1000,1000])
sleep(1)
dynamixel.multiMove([2,3],[500,500],[1000,1000])
sleep(0.8)
dynamixel.multiMove([2,3],[750,750],[1000,1000])
sleep(0.4)
dynamixel.multiMove([2,3],[1000,1000],[1000,1000])
sleep(1)
