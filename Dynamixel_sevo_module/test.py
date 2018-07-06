import dynamixel
dynamixel.init(1)
dynamixel.move(DXL_ID = input(" ID ?"), dxl_goal_position = input("How much ?"), dxl_goal_speed = input("Wich speed ?"))
dynamixel.close(1)

