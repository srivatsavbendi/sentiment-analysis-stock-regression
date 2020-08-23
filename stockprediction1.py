import numpy
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
import sys
import requests
import json
import math
import threading
import random
from firebase import firebase

a,b,c,d,e,f,g = numpy.loadtxt("AXL.csv", delimiter=",", unpack=True)

closemodel = numpy.poly1d(numpy.polyfit(a, e, 3))


myline = numpy.linspace(1, 39, 100)

closestockweek = closemodel (40)
closestockday = closemodel (41)

stockweekstr = str(closestockweek)
print("Estimated Stock on 8/31/2020= " + stockweekstr)

stockdaystr = str(closestockday)
print("Estimated Stock on 8/24/2020= " + stockdaystr)

alphavantage = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AXL&apikey=TB81Z6OL86BE8YJN'

AlphaVantage = requests.get(alphavantage).json()
closestock = AlphaVantage['Time Series (Daily)']['2020-08-21']["4. close"]
closestocktoday = str(closestock)
print("Stock Price= " + closestocktoday)


plt.scatter(a, e, color="green")
plt.plot(myline, closemodel(myline), color="purple", label="Daily close", linewidth="3")
plt.show()