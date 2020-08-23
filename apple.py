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

firebase = firebase.FirebaseApplication("https://nhacks-72453.firebaseio.com/")
a,b,c,d,e = numpy.loadtxt("AAPL.csv", delimiter=",", unpack=True)

openmodel = numpy.poly1d(numpy.polyfit(a, b, 3))
highmodel = numpy.poly1d(numpy.polyfit(a, c, 3))
lowmodel = numpy.poly1d(numpy.polyfit(a, d, 3))
closemodel = numpy.poly1d(numpy.polyfit(a, e, 3))


myline = numpy.linspace(1, 52, 100)

highstockweek = highmodel(52)
lowstockweek = lowmodel (52)
openstockweek = openmodel (52)
closestockweek = closemodel (52)

highstockday = highmodel(50)
lowstockday = lowmodel (50)
openstockday = openmodel (50)
closestockday = closemodel (50)

stockweek = (highstockweek + lowstockweek + openstockweek + closestockweek)/4
stockweekstr = str(stockweek)
print("Estimated Stock on 8/26/2020= " + stockweekstr)

stockday = (highstockday + lowstockday + openstockday + closestockday)/4
stockdaystr = str(stockday)
print("Estimated Stock on 8/24/2020= " + stockdaystr)

alphavantage = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=TB81Z6OL86BE8YJN'

AlphaVantage = requests.get(alphavantage).json()
closestock = AlphaVantage['Time Series (Daily)']['2020-08-21']["4. close"]
closestock1 = float(closestock)
closestocktoday = str(closestock)
print("Stock Price= " + closestocktoday)

weeklychange = round(stockweek) - round(closestock1)
print(weeklychange)

dailychange = round(stockday) - round(closestock1)
print(dailychange)

firebase.put("/Apple/", "1daychange", weeklychange)
firebase.put("/Apple/", "3daychange", dailychange)
firebase.put("/Apple/", "estimated1day", stockday)
firebase.put("/Apple/", "estimated3day", stockweek)
firebase.put("/Apple/", "stockprice", closestock1)


plt.scatter(a, b)
plt.plot(myline, highmodel(myline), color="blue", label="Daily high")
plt.plot(myline, lowmodel(myline), color="red", label="Daily low")
plt.plot(myline, openmodel(myline),color="green", label="Daily open")
plt.plot(myline, closemodel(myline), color="purple", label="Daily close")
plt.legend(fontsize=9)
plt.show()