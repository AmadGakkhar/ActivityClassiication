import pandas as pd
import numpy as np
from math import exp
from math import sqrt
from math import pi
import matplotlib.pyplot as plt
import operator 



def dataMean(x):
    return np.mean(x)

def dataStd(x):
    return np.std(x)

def gaussianP(x,mu,sigma):
    exponent = exp(-((x - mu) ** 2 / (2 * sigma ** 2)))
    return (1 / (sqrt(2 * pi) * sigma)) * exponent


pitchData = pd.read_csv("~/Documents/Lectures Stochastic/Project/P.csv")
pitchData.columns = ['X', 'Y', 'Z', 'Class']
pitchDataX = pitchData['X'].to_numpy()
pitchDataY = pitchData['Y'].to_numpy()
pitchDataZ = pitchData['Z'].to_numpy()

rollData = pd.read_csv("~/Documents/Lectures Stochastic/Project/R.csv")
rollData.columns = ['X', 'Y', 'Z', 'Class']
rollDataX = rollData['X'].to_numpy()
rollDataY = rollData['Y'].to_numpy()
rollDataZ = rollData['Z'].to_numpy()

yawData = pd.read_csv("~/Documents/Lectures Stochastic/Project/Y.csv")
yawData.columns = ['X', 'Y', 'Z', 'Class']
yawDataX = yawData['X'].to_numpy()
yawDataY = yawData['Y'].to_numpy()
yawDataZ = yawData['Z'].to_numpy()

testx = float(input("Enter X value    "))
testy = float(input("Enter Y value    "))
testz = float(input("Enter Z value    "))

# print("You Entered  ", testx, " ", testy, " ", testz)

PXgivenPitch = gaussianP( testx, dataMean(pitchDataX), dataStd(pitchDataX))
PXgivenRoll = gaussianP( testx, dataMean(rollDataX), dataStd(rollDataX))
PXgivenYaw = gaussianP( testx, dataMean(yawDataX), dataStd(yawDataX))

PYgivenPitch = gaussianP( testy, dataMean(pitchDataY), dataStd(pitchDataY))
PYgivenRoll = gaussianP( testy, dataMean(rollDataY), dataStd(rollDataY))
PYgivenYaw = gaussianP( testy, dataMean(yawDataY), dataStd(yawDataY))

PZgivenPitch = gaussianP( testz, dataMean(pitchDataZ), dataStd(pitchDataZ))
PZgivenRoll = gaussianP( testz, dataMean(rollDataZ), dataStd(rollDataZ))
PZgivenYaw = gaussianP( testz, dataMean(yawDataZ), dataStd(yawDataZ))

PofPitch = PXgivenPitch * PYgivenPitch * PZgivenPitch
PofRoll = PXgivenRoll * PYgivenRoll * PZgivenRoll
PofYaw = PXgivenYaw * PYgivenYaw * PZgivenYaw

probs = {"Pitch": PofPitch, "Roll" : PofRoll, "Yaw" : PofYaw}

print ("P of Pitch ",PofPitch)
print ("P of Roll ",PofRoll)
print ("P of Yaw ",PofYaw)

print(max(probs.items(), key=operator.itemgetter(1))[0])


# print(np.max(test))

# plt.hist(pitchDataX)
# plt.show()

