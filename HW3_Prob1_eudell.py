# Activity 3.3.1: An introduction to Python. HW 3.1
# File: HW3_Prob1_eudell.py
# Date: 1 September 2018
# By: Emily Udell
# eudell
# Section: 3
# Team: 36
#
# ELECTRONIC SIGNATURE
# Emily Udell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
#  This program checks whether a given restraining system
# is safe according to the maximum overtuning moment

import math
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
towerHeight = input("Enter the height (in meters):")
pointAx = input("Enter the x coordinate of anchor point A (in meters):")
pointAy = input("Enter the y coordinate of anchor point A (in meters):")
pointBx = input("Enter the x coordinate of anchor point B (in meters):")
pointBy = input("Enter the y coordinate of anchor point B (in meters):")
pointCx = input("Enter the x coordinate of anchor point C (in meters):")
pointCy = input("Enter the y coordinate of anchor poitn C (in meters): ")
magnitudeDA = input("Enter the tensile force in cable DA (in newtons):")
magnitudeDB = input("Enter the tensile force in calbe DB (in newtons):")
magnitudeDC = input("Enter the tensile force in calbe DC (in newtons):")
maxValue = input("Enter maximum value for the overturning moment (in N-m):")
coordinateA = [pointAx,pointAy,towerHeight]
coordinateB = [pointBx,pointBy,towerHeight]
coordinateC = [pointCx,pointCy,towerHeight]


#---------------------------------------------------
#  Computations
#---------------------------------------------------
def unitVector (x,y,z):
  mag = (float(x) ** 2 + float(y) ** 2 +  float(z) ** 2) ** (1/2)
  unitVec = [float(x)/mag, float(y)/mag, float(z)/mag]
  return unitVec
uVectorA = unitVector (pointAx,pointAy,towerHeight)
uVectorB = unitVector (pointBx,pointBy,towerHeight)
uVectorC = unitVector (pointCx,pointCy,towerHeight)

vectorDAX = float(magnitudeDA) * float(uVectorA[0])
vectorDAY = float(magnitudeDA) * float(uVectorA[1])
vectorDAZ = float(magnitudeDA) * float(uVectorA[2])
vectorDBX = float(magnitudeDB) * float(uVectorB[0])
vectorDBY = float(magnitudeDB) * float(uVectorB[1])
vectorDBZ = float(magnitudeDB) * float(uVectorB[2])
vectorDCX = float(magnitudeDC) * float(uVectorC[0])
vectorDCY = float(magnitudeDC) * float(uVectorC[1])
vectorDCZ = float(magnitudeDC) * float(uVectorC[2])

vectorTotalX = vectorDAX + vectorDBX + vectorDCX
vectorTotalY = vectorDAY + vectorDBY + vectorDCY

vectorTotal = [vectorTotalX,vectorTotalY]

#---------------------------------------------------
#  Outputs
#---------------------------------------------------

fPerp = math.sqrt((vectorTotalX) ** 2 + (vectorTotalY) ** 2)
mOverturning = fPerp * float(towerHeight)

if (mOverturning > float(maxValue)):
    print("The overturning magnitude is:",mOverturning)
    print("The restraining system is not safe")

if (mOverturning < float(maxValue)):
    print("The overturning magnitude is:",mOverturning)
    print("The restraining system is safe")


