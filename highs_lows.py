import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
filename1 = 'sitka_weather_2014.csv'

with open(filename) as fp:
    reader = csv.reader(fp)
    header_row = next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            cur_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(cur_date,'missing data')
        else:
            dates.append(cur_date)
            highs.append(high)
            lows.append(low)

with open(filename1) as fp1:
    reader1 = csv.reader(fp1)
    header_row1 = next(reader1)
    dates1,highs1,lows1=[],[],[]
    for row1 in reader1:
        try:
            cur_date1 = datetime.strptime(row1[0],'%Y-%m-%d')
            high1 = int(row1[1])
            low1 = int(row1[3])
        except ValueError:
            print(cur_date,'missing data')
        else:
            dates1.append(cur_date1)
            highs1.append(high1)
            lows1.append(low1)


fig = plt.figure(dpi=128,figsize=(10,6))
#For Death Valley
plt.plot(dates,highs,c='orange',alpha=1)
plt.plot(dates,lows,c='green',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='white',alpha=0.5)

#For Sitka
plt.plot(dates1,highs1,c='red',alpha=1)
plt.plot(dates1,lows1,c='blue',alpha=0.5)
plt.fill_between(dates1,highs1,lows1,facecolor='blue',alpha=0.1)

plt.title("Daily high and low temperatures,2014\nDeath Valley(OrangeGreen) and Sitka(RedBlue)",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

