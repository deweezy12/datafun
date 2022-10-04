import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	#get high and low temepratures from this file and dates
	dates, highs, lows, rains = [], [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			rain = float(row[3])
			high = int(row[4])
			low = int(row[5])			
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			rains.append(rain)
			highs.append(high)
			lows.append(low)
			
#plot the high and lowtemperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates,rains, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot
title = "Daily high and low temperatures - 2018\n Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
