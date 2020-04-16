# Imports 
import numpy as np

# Vars
motorDrawMin = 0.52 # amps
motorDrawMax = 20 # amps 

torqueAtMin = 0 # Oz-In
torqueAtMax = 416.6 # Oz-In 

# torqure needed for climbing 45 degrees 
x = 75

motorDraw = (motorDrawMax/torqueAtMax)*x + motorDrawMin

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
totalDrawavg = raspiCurrent + txCurrent + 6*motorDraw
# Add second battery
lifeMax = np.round(2*capacity/totalDrawmin,2)
lifeMin = np.round(2*capacity/totalDrawmax,2)
lifeAvg = np.round(2*capacity/totalDrawavg,2)

print(str(lifeMax) + ' hrs to ' + str(lifeMin) + ' hrs')
print(str(lifeAvg) + ' hrs')