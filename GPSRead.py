import serial
import math
import datetime

port = raw_input("Enter the port (in /dev/): ")

ser = serial.Serial('/dev/{0}'.format(port), 9600)

# def nmeaParse(sentence):
# 	gpsarr = sentence.split(',')
# 	time = "{0}:{1}:{2}".format( gpsarr[1][0:2], gpsarr[2][2:4], gpsarr[1][4:6])
# 	date = "{0}-{1}-{2}".format(  )

class GPSdataObj:
	def __init__(self, sentence):
		gpsArray = sentence.split(',')
		century = str(datetime.datetime.now().year)[0:2]
		self.date = "{0}{1}-{2}-{3}".format( century, gpsArray[9][4:6],  gpsArray[9][2:4], gpsArray[9][0:2] )
		self.time = "{0}:{1}:{2}".format( gpsArray[1][0:2], gpsArray[1][2:4], gpsArray[1][4:6]  )
		self.speed = float(gpsArray[7]) / 0.539956803456
		latDeg = int(gpsArray[3][0:2])
		lonDeg = int(gpsArray[5][0:3])
		latMin = float(gpsArray[3][2:])
		lonMin = float(gpsArray[5][3:])
		self.latitude = latDeg + (latMin / 60)
		self.longitude = lonDeg + (lonMin / 60)
		if gpsArray[4] == "S":
			self.latitude = 0 - self.latitude
		if gpsArray[6] == "W":
			self.longitude = 0 - self.longitude

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
	try:
		vehSpeed = ( float(distance) / time ) * 60 * 60
	except ZeroDivisionError:
		vehSpeed = 0
	return vehSpeed

while True:
	t = ser.readline()
	currentPoint = t.split(',')
	if "RMC" in currentPoint[0] and (currentPoint[1] != '') and (currentPoint[3] != '') and (currentPoint[5] != '') and (currentPoint[9] != ''):
		currentData = GPSdataObj(t)
		print "date & time:", currentData.date, currentData.time
		print "speed:", currentData.speed, "km/h"
		print "lat:", currentData.latitude
		print "lon:", currentData.longitude
		if lastPoint:
			distanceTraveled = distance(lastData.latitude, lastData.longitude, currentData.latitude, currentData.longitude)
			timeDifference = timeDiff(lastData.time, currentData.time)
			currentSpeed = speed(distanceTraveled, timeDifference)
			print "speed:", currentSpeed
		lastData = currentData
