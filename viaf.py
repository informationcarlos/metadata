import csv
import requests
import json


####THIS WILL FIND ULAN URI#####

#make viaf URI variable
viafURI = "http://viaf.org/viaf/59096037/"

viafURIJSON = "http://viaf.org/viaf/59096037/" + "justlinks-json"

#requests JSON data from API
r=requests.get(viafURIJSON)

#takes the API response and turn it into JSON
response = json.loads(r.text)

#Loop through JSON to find ULAN which is abbreviated "JPG" for some reason
for entry in response['JPG']:

	#this is the ulan id
	ulanID = entry

	#add URI info to beginning of ID to get final URI
	ulanURI = "http://vocab.getty.edu/ulan/"+ulanID 
	
	print (ulanURI)

