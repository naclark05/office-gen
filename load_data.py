# imports csv file officedb which contains all episodes

import configurations
configurations.setup()

# Full path and name to your csv file 
csv_path = "/Users/nikclarks/djproj/officesite/officedb.csv" 
# Full path to your django project directory 
officesite_path = "/Users/nikclarks/djproj/officesite/" 

import sys, os 
sys.path.append(officesite_path) 

from offgen.models import Episode 
import csv 
dataReader = csv.reader(open(csv_path), delimiter=',', quotechar='"') 
header = next(dataReader) # define header
if header != None: # skip header, import all other rows
	for row in dataReader: 
		episode = Episode()
		episode.epname = row[0] 
		episode.epdesc = row[1] 
		episode.season = row[2] 
		episode.epnum = row[3] 
		episode.save()