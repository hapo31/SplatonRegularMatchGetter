# -*- coding: utf-8 -*--

import datetime

def time_priod(time=None):
	if time is None:
		time = datetime.datetime.today()
	datetmp = datetime.datetime(time.year, time.month, time.day, time.hour, 0, 0)
	#現在時刻から、そのピリオドの開始時刻を求める
	begintime = ((((datetmp.hour + 1) % 24) / 6)* 6 - 1) % 24
	#print begintime
	begin = datetime.datetime(time.year, time.month, time.day, begintime, 0, 0)
	end = datetime.datetime(time.year, time.month, time.day, (begintime + 4) % 24 , 0, 0)

	return [begin, end]

if __name__ == '__main__':
	for x in range(0, 6):
		day = datetime.datetime(2015, 4, 1, x * 4)
		d = time_priod(day)
		print "input :",day
		print "result:",d[0], "~", d[1]