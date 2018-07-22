import os
import configparser
from dynamixel_sdk import *
if os.name == 'nt':
    import msvcrt
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

config = configparser.ConfigParser()
config.read("settings.ini")

ADDR_MX_GOAL_SPEED          = 32
ADDR_MX_TORQUE_ENABLE       = 24
ADDR_MX_GOAL_POSITION       = 30
ADDR_MX_PRESENT_POSITION    = 36
LEN_MX_GOAL_SPEED           = 2
LEN_MX_GOAL_POSITION        = 2
LEN_MX_PRESENT_POSITION     = 4
PROTOCOL_VERSION            = 1.0
BAUDRATE                    = 1000000
DEVICENAME                  = config.get("Settings", "COM")
TORQUE_ENABLE               = 1
TORQUE_DISABLE              = 0
DXL_MINIMUM_POSITION_VALUE  = 0
DXL_MAXIMUM_POSITION_VALUE  = 1023

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
groupBulkRead = GroupBulkRead(portHandler, packetHandler)

def init(ID):
    if portHandler.openPort():
       print("Succeeded to open the port")
    if portHandler.setBaudRate(BAUDRATE):
       print("Succeeded to change the baudrate")
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
       print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
       raise Exception("Something went wrong, probably one of the servos is't connected or out of power supply")
    elif dxl_error != 0:
       print("%s" % packetHandler.getRxPacketError(dxl_error))
       raise Exception("Something went wrong error code :", dxl_error)
    else:
       print("Dynamixel#%d has been successfully connected" % ID)

def multiMove(ID,pos,speed):
    groupSyncPos = GroupSyncWrite(portHandler, packetHandler, ADDR_MX_GOAL_POSITION, LEN_MX_GOAL_POSITION)
    groupSyncSpeed = GroupSyncWrite(portHandler, packetHandler,ADDR_MX_GOAL_SPEED, LEN_MX_GOAL_SPEED)
    IDO = 0
    IDQ = 1
    for x in ID:
        param_goal_speed = [DXL_LOBYTE(speed[IDO]), DXL_HIBYTE(speed[IDO])]
        param_goal_position = [DXL_LOBYTE(pos[IDO]), DXL_HIBYTE(pos[IDO])]
        dxl_addparam_result = groupSyncSpeed.addParam(ID[IDO], param_goal_speed)
        dxl_addparam_result = groupSyncPos.addParam(ID[IDO], param_goal_position)
        IDO = IDO + 1
        IDQ = IDQ + 1
    groupSyncSpeed.txPacket()
    groupSyncPos.txPacket()
    dxl_comm_result = groupSyncSpeed.txPacket()
    dxl_comm_result = groupSyncPos.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
         raise Exception("Something went wrong")

def stop(ID):
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
    if dxl_comm_result != COMM_SUCCESS:
         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
         raise Exception("Something went wrong, servo did not respond")
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
        raise Exception("Something went wrong error code :", dxl_error)
    portHandler.closePort()

def read(ID):

    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, ID, 36)
    if dxl_comm_result != COMM_SUCCESS:
         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
         raise Exception("Something went wrong ", dxl_error)
    return dxl_present_position
