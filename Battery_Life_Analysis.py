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

# Swift 2 Camera
camCurrent = 0.07 #A
camVolts = 12 #volts 

# Life 
totalDrawmin = raspiCurrent + txCurrent + 6*motorDrawMin + camCurrent
totalDrawmax = raspiCurrent + txCurrent + 6*motorDrawMax + camCurrent
totalDrawavg = raspiCurrent + txCurrent + 6*motorDraw
# Add second battery
lifeMax = int(60*(2*capacity/totalDrawmin))
lifeMin = int(60*(2*capacity/totalDrawmax))
lifeAvg = int(60*(2*capacity/totalDrawavg))

print(str(lifeMax) + ' minutes to ' + str(lifeMin) + ' minutes')
print(str(lifeAvg) + ' minutes')