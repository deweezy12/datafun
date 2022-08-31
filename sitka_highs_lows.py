import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#get high and low temepratures from this file and dates
	dates, highs, lows, rains = [], [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		rain = int(row[3])
		high = int(row[5])
		low = int(row[6])
		dates.append(current_date)
		rains.append(rain)
		highs.append(high)
		lows.append(low)

#plot the high and lowtemperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, rains, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#format plot
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
