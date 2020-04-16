# Vars
motorDrawMin = 0.52 # amps
motorDrawMax = 20 # amps 

# battery 
capacity = 8 #Ah
volts = 11.1 #volts 

# Raspberry Pi
raspiCurrent = 2.5 #A
raspiVolts = 5 #volts 

# Transmitter
txCurrent = .220 #A
txVotls = 12 #volts

# Life 
totalDrawmin = raspiCurrent + txCurrent + 6*motorDrawMin
totalDrawmax = raspiCurrent + txCurrent + 6*motorDrawMax
lifeMax = capacity/totalDrawmin
lifeMin = capacity/totalDrawmax
print(str(lifeMax) + ' hrs to ' + str(lifeMin) + ' hrs')