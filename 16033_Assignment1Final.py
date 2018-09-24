### imports

import numpy as np
import random as rnd
import pandas as pd

### Global Variables

sampleArr = []
S = 0
y = 0

### Functions

# Function getNextStream
def getNextStream(n):
    arr = []
    for i in range(n):
        arr.append("A"+str(i+1))
    return np.random.permutation(arr)

# Function updateSample
def updateSample(streamItem,itemNumber):
    if(itemNumber<=S):
        sampleArr.append(streamItem)
    else:
        var1 = rnd.randint(1,itemNumber)
        if(var1<=S):
            var2 = rnd.randint(0,S-1)
            sampleArr[var2]=streamItem

# Function getNextStreamANDupdateSample()
def getNextStreamANDupdateSample(n,s):
    global sampleArr
    global S
    global y
    sampleArr = []
    # N = eval(input("Enter the Size of Stream to be Generated \n"))
    N = n
    Arr = getNextStream(n=N)
    y = Arr
    # print("Stream generated is ")
    # print(Arr)
    # S = eval(input("Enter the Sample Size \n"))
    S = s
    for i in range(N):
        updateSample(Arr[i],i+1)
    sampleArr=np.array(sampleArr)
    return sampleArr

# Function getNextStreamANDupdateSample1() for size 20 
def getNextStreamANDupdateSample1(GenArr,s):
    global sampleArr
    global S
    sampleArr = []
    S = s
    for i in range(20):
        updateSample(GenArr[i],i+1)
    sampleArr=np.array(sampleArr)
    return sampleArr

# Function Counts streamItem. Taking Granted that only 20 stream items are there
def CountFunc(Array):
    global Count
    if "A1" in Array:
        Count[0]=Count[0]+1
    if "A2" in Array:
        Count[1]=Count[1]+1
    if "A3" in Array:
        Count[2]=Count[2]+1
    if "A4" in Array:
        Count[3]=Count[3]+1
    if "A5" in Array:
        Count[4]=Count[4]+1
    if "A6" in Array:
        Count[5]=Count[5]+1
    if "A7" in Array:
        Count[6]=Count[6]+1
    if "A8" in Array:
        Count[7]=Count[7]+1
    if "A9" in Array:
        Count[8]=Count[8]+1
    if "A10" in Array:
        Count[9]=Count[9]+1
    if "A11" in Array:
        Count[10]=Count[10]+1
    if "A12" in Array:
        Count[11]=Count[11]+1
    if "A13" in Array:
        Count[12]=Count[12]+1
    if "A14" in Array:
        Count[13]=Count[13]+1
    if "A15" in Array:
        Count[14]=Count[14]+1
    if "A16" in Array:
        Count[15]=Count[15]+1
    if "A17" in Array:
        Count[16]=Count[16]+1
    if "A18" in Array:
        Count[17]=Count[17]+1
    if "A19" in Array:
        Count[18]=Count[18]+1
    if "A20" in Array:
        Count[19]=Count[19]+1    

### Code Starting

N = eval(input("Enter the Size of Stream to be Generated \n"))
S = eval(input("Enter the Sample Size \n"))
Gen_Arr = getNextStreamANDupdateSample(N,S)
print("Stream Generated is ")
print(y)
print("Sample Stream Generated is ")
print(Gen_Arr)
print("\n")

CONTINUE = input("Press Enter to get Count for Sampling 100,500,1000,10000 times \n")

Gen_Arr1 = getNextStream(20)
print("Generated Stream of size 20 is \n")
print(Gen_Arr1)
print("\n")

 # Sampling Process for 100 times

Count = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(100):
    Temp = getNextStreamANDupdateSample1(Gen_Arr1,5)
    CountFunc(Temp)
# print("Count for Sampling 100 times ",Count)
Mean100 = np.mean(Count)
Median100 = np.median(Count)
Std100 = np.std(Count)
Count100 = Count
# print("\n")

 # Sampling Process for 500 times

Count = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(500):
    Temp = getNextStreamANDupdateSample1(Gen_Arr1,5)
    CountFunc(Temp)
# print("Count for Sampling 500 times ",Count)
Mean500 = np.mean(Count)
Median500 = np.median(Count)
Std500 = np.std(Count)
Count500 = Count
# print("\n")

 # Sampling Process for 1000 times

Count = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(1000):
    Temp = getNextStreamANDupdateSample1(Gen_Arr1,5)
    CountFunc(Temp)
# print("Count for Sampling 1000 times ",Count)
Mean1000 = np.mean(Count)
Median1000 = np.median(Count)
Std1000 = np.std(Count)
Count1000 = Count
# print("\n")

 # Sampling Process for 10000 times

Count = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for i in range(10000):
    Temp = getNextStreamANDupdateSample1(Gen_Arr1,5)
    CountFunc(Temp)
# print("Count for Sampling 10000 times ",Count)
Mean10000 = np.mean(Count)
Median10000 = np.median(Count)
Std10000 = np.std(Count)
Count10000 = Count
# print("\n")

# Craeting INDEX
Index = np.array(["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16","A17","A18","A19","A20"])

# Creating DataFrame

dataFrame = pd.DataFrame(data={"StreamItem": Index,"N=100": Count100,"N=500": Count500,"N=1000": Count1000,"N=10000": Count10000})
dataFrame = dataFrame.set_index("StreamItem")
print("Count Table \n")
print(dataFrame)
print("\n")

# Mean Median StandardDeviation Observations

Index = np.array(["Mean","Median","Standard Deviation"])
Obs1 =[]
Obs2 =[]
Obs3 =[]
Obs4 =[]
Obs1.append(str(int(Mean100)))
Obs1.append(str(Median100))
Obs1.append(str(Std100))
Obs2.append(str(int(Mean500)))
Obs2.append(str(Median500))
Obs2.append(str(Std500))
Obs3.append(str(int(Mean1000)))
Obs3.append(str(Median1000))
Obs3.append(str(Std1000))
Obs4.append(str(int(Mean10000)))
Obs4.append(str(Median10000))
Obs4.append(str(Std10000))

dataFrame = pd.DataFrame(data={"Observations":Index,"N=100":Obs1,"N=500":Obs2,"N=1000":Obs3,"N=10000":Obs4})
dataFrame = dataFrame.set_index("Observations")
print("Observation Table \n")
print(dataFrame.to_string())