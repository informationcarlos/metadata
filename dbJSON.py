import csv
import requests
import json
import re 

#####THIS RETURNS VIAF URIS######

#here is a dbpedia URI
dbURI = "http://dbpedia.org/resource/Piet_Mondrian"

#make sure it is a sting for regex action
s= str(dbURI)

#use regex to change the URI to query the JSON data
dbJSON = re.sub('/resource/', '/data/', s)

#query the JSON data for the dbpedia URI
r=requests.get(dbJSON +".json")

#takes the API response and turn it into JSON
response = json.loads(r.text)

#loop through the JSON entry to find the "SAME AS" property of the dbpedia ontology
for entry in response[dbURI]['http://www.w3.org/2002/07/owl#sameAs']:
	#there are many "same as" URIs, so need to pick out viaf
	if "viaf.org" in entry['value']:
		#This prints out the viaf URI
		print (entry['value'])





