import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
	# print(f.read())
	reader = csv.reader(f)
	print(str(reader))
	header_row = next(reader)
	# print(header_row)
	# for index, column_header in enumerate(header_row):
	# 	print("位置"+ str(index)+",值:"+column_header)

	dates, highs, lows = [],[],[]
	for row in reader:
		high = int(row[1])
		highs.append(high)
		current_date = datetime.strptime(row[0], '%Y-%m-%d')
		dates.append(current_date)
		low = int(row[3])
		lows.append(low)

	print(highs)

	#根据数据绘制图形
	fig = plt.figure(dpi = 128, figsize = (10, 6))

	plt.plot(dates, highs, c = 'red', alpha=0.5)

	plt.plot(dates, lows, c='blue', alpha=0.5)

	plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

	#设置图形的格式
	plt.title("Daily high temperatures, July 2014", fontsize = 24)
	plt.xlabel("", fontsize = 16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize = 16)
	plt.tick_params(axis = "both", which="major", labelsize = 16)

	plt.show()