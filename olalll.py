import geocoder
import math
import requests,json
from math import sin, cos, sqrt, atan2, radians

def signup():
	f=open("confidential.txt","a")
	name = input("UserName:")
	f.write(name)
	mobileNo = (int)(input("MobileNo:"))
	f.write(str(mobileNo))
	Password = input("Password:")
	f.write(Password)
	f.close()

def login():
	f=open("confidential.txt","r")
	txt = f.read()
	name = input("UserName: ")
	pwd = input("Password: ")
	if name and pwd in txt:
		print("Login Successful!")
	else:
		print("Please signup first!")
		signup()
	f.close()

def distance(a,b):
	R = 6373.0
	x=[]
	y=[]
	for n in a:
		x.append(n)
	for m in b:
	   	y.append(m)

	lat1 = radians(float(x[0]))
	lon1 = radians(float(x[1]))
	lat2 = radians(float(y[0]))
	lon2 = radians(float(y[1]))

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance

drivers = {"driver1":[11.0426,79.1840],"driver2": [12.9801,80.2184],"driver3" : [13.0473,80.0945]}
driver_number = {"driver1":9876543210,"driver2":5687456789,"driver3":9864709324}
drivers_len = len(drivers)
#LOGIN DETAILS
ch = (int)(input("'1' for signup '2' for login\n"))
if ch==1:
	signup()
elif ch==2:
	login()
#CURRENT LOCATION
flag=0
while(flag==0):
	while(True):
		choice=(int)(input("Type '1' to Enter pickup location\nType '2' for Current Location:\n"))
		if choice==1:
			inp = input("Enter your pickup point:")
			response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+inp+"&key=AIzaSyCdHv0Vh90k9Dd8ooFDrFNyQLSMZCaJBH4")
			resp_json_payload=response.json()
			g=[]
			c = resp_json_payload['results'][0]['geometry']['location']['lat']
			g.append(c)
			d = resp_json_payload['results'][0]['geometry']['location']['lng']
			g.append(d)
			break
		elif choice==2:
			g = geocoder.ip('me')
			g=g.latlng
			break
		else:
			print("Select either 1 or 2!")

	#DESTINATION
	destination = input("Enter destination address: ")
	response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+destination+"&key=AIzaSyCdHv0Vh90k9Dd8ooFDrFNyQLSMZCaJBH4")
	resp_json_payload = response.json()
	dest_address=[]
	c=resp_json_payload['results'][0]['geometry']['location']['lat']
	dest_address.append(c)
	d=resp_json_payload['results'][0]['geometry']['location']['lng']
	dest_address.append(d)

	print("Your Drop is "+str(distance(g,dest_address))+" kms away from here!")

	#CLOSEST DISTANCE BETWEEN DRIVERS AND USER
	dis_bet=[]
	checkeq = []

	for i in range(1,drivers_len+1):
		dist = distance(g,drivers["driver"+str(i)])
		dis_bet.append(dist)
		checkeq.append(dist)
		if dist<=25:
			print("Driver "+str(i)+" is "+str(dist)+"kms away from you!")
	dis_bet.sort()

	for i in range(0,drivers_len):
		if dis_bet[0] == checkeq[i]:
			print("Driver "+str(i+1)+" is closer to you and he'll pick you up!")
			print("Your driver's number is "+str(driver_number["driver"+str(i+1)]))
			break
		else:
			continue

	final_dec = input("Do you want to cancel ride?????(y/n): \n")
	if final_dec == 'n':
		flag=1
		print("Your booking is conformed!")
		break
	else:
		continue

	#print("Distance from "+str(g)+" to "+destination+" is "+str(dis(g,destination)))
