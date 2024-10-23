import random #importing module
import time
def getRandomDate(startDate, endDate): #defining function
    print("printing random dates between", startDate "and" endDate) randomGenerator = random.random()
    dateFormat ='%m%d%y'
    startTime = time.mktime