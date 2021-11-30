#!/usr/bin/python3
from datetime import datetime
from zone import Zone
from API import send_drive
from clen_data import Clean
import pytz

sent_flag=False
#Check if it is "Pico y placa" time
def charge_time():
	timezone = pytz.timezone('America/Bogota')
	now = datetime.now(timezone).time()
	#Pico y placa time
	#First period
	start1 = datetime.time(6, 0, 0)
	end1 = datetime.time(8, 30, 0)
	#Second period
	start2 = datetime.time(15, 0, 0)
	end2 = datetime.time(19, 30, 0)
	if (start1 <= now <= end1):
		return True
	elif (start2 <= now <= end2):
		return True
	else:
		return False
def main():
	global sent_flag
	if not charge_time():
		Clean()
		timezone = pytz.timezone('America/Bogota')
		today=datetime.datetime.now(timezone).strftime("%d%m%y")
		file_name=f'./data{today}.txt'
		try:
			with open(file_name,"r") as file:
				data = file.readlines()
		except FileNotFoundError:
			print('There is not a file with that name')
		else:
			for element in data[0:-1]:
				separate_comma = element.strip().split(',')
				lat = separate_comma[0]
				lon = separate_comma[1]
				position = lat + lon
				plate = separate_comma[2]
				time = separate_comma[3]
				send_drive(time,"Zona1",plate,position)	
			sent_flag = True
if __name__ == '__main__':
	while True:
		if charge_time():
			sent_flag = False
		if not sent_flag and not charge_time():
			main()