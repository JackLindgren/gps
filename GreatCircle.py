import math
from datetime import datetime

la1 = float(raw_input("Enter the starting latitude: "))
lo1 = float(raw_input("Enter the starting longitude: "))
la2 = float(raw_input("Enter the ending latitude: "))
lo2 = float(raw_input("Enter the ending longitude: "))

ts1 = "2016-01-15 10:00:00"
ts2 = "2016-01-15 10:30:00"

def distance(lat1, lon1, lat2, lon2):
	R = 6371000
	l1r = math.radians(lat1)
	l2r = math.radians(lat2)
	latDr = math.radians(lat2 - lat1)
	lonDr = math.radians(lon2 - lon1)
	a = math.sin(latDr / 2) * math.sin(latDr / 2) + math.cos(l1r) * math.cos(l2r) * math.sin(lonDr / 2) * math.sin(lonDr / 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = (R * c) / 1000
	return d 		# distance is in kilometers

def timeDiff(t1, t2):
	t1obj = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
	t2obj = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
	tDiff = t2obj - t1obj
	return tDiff.seconds		# time is in seconds

def speed(distance, time):
	# distance is in km
	# time is in seconds
	vehSpeed = ( float(distance) / time ) * 60 * 60
	return vehSpeed

distanceTraveled = distance(la1, lo1, la2, lo2)
timeTaken = timeDiff(ts1, ts2)
velocity = speed(distanceTraveled, timeTaken)
print "Speed is: {0} km/h".format(velocity)

