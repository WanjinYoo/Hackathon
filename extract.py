

# install pip ; sudo apt-get install python-pip javac n3-pip

import os
import os.path
import json
import datetime
import csv

def ToCSV(dict):
	with open('mycsvfile.csv','wb') as f:
		w = csv.writer(f)
		w.writerow(dict())
 	



def AgeAtSeasonStart(season,dob):
	dd = int(dob[-2:])
	mm = int(dob[5:7])
	yy = int(dob[:4])
	bigdate = datetime.date(yy,mm,dd)
	smldate = datetime.date(int(season[:4]),11,1)
	return abs(bigdate - smldate).days/365.25

def SetTargetSeasons(date):
	dd = int(date[-2:])
	mm = int(date[5:7])
	yy = int(date[:4])
	start = 0
	if (mm >= 11):
		start = yy+17
		interval = []
	else:
		start = yy+16
		interval = []
	ar = [[start,(start+1)%100],[start+1,(start+2)%100],[start+2,(start+3)%100],[start+3,(start+4)%100],[start+4,(start+5)%100],[start+5,(start+6)%100]]
	
	for i in range(6):
		if(ar[i][0] > 2008):
			interval.append( str(ar[i][0])+"-"+str(ar[i][0]+1-2000))
		elif(ar[i][0] > 1998):
			interval.append( str(ar[i][0])+"-0"+str(ar[i][0]+1-2000))
		else:
			interval.append( str(ar[i][0])+"-"+str(ar[i][0]+1-1900))
	return interval

def main():
	if os.path.exists('quotes.json'):
		with open('quotes.json') as data_file:
			data = json.load(data_file)
	new={}
	for i in (range(len(data))):
		age = data[i]['author']
		height = data[i]['height']
		mg = SetTargetSeasons(age)
		new[data[i]['name']]={}
		new[data[i]['name']]['height'] = height
		#new[data[i]['name']]['nhl'] = [something]
		for j in range(len(data[i]['Leage'])):
			if("WHL" in data[i]['Leage'][j]):
				for p in range(6):
					if(mg[p] == data[i]['season'][j]):
						ageSeason = int(AgeAtSeasonStart(data[i]['season'][j],age))
						s = 'S'+str(ageSeason)
						new[data[i]['name']][s] = [data[i]['GP'][j],data[i]['TP'][j]]
		print (new[data[0]['name']])
		
	

	
main()
