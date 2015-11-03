import csv
import requests
import json
import re
import xml.etree.ElementTree as etree

#open csv of all artist names
with open('allArtsyArtists.csv', 'r') as csvfile:
	
	lines = csv.reader(csvfile)

	for a_line in lines:
		
		#make name variable
		person_name = a_line[1]
		
		#this searches dbpedia API for artist name against names in database that are in the "Artist" class of the ontology
		r= requests.get('http://lookup.dbpedia.org/api/search.asmx/KeywordSearch?QueryClass=artist&MaxHits=3&QueryString=' + person_name)

		#API returns an XML which needs to be parsed
		root = etree.fromstring(r.text)

		#loop through XML to pull out the data we want
		for a_element in root:
			for b_element in a_element:	

				#searches for the dbpedia URI and assigns it as variable
				if b_element.tag == "{http://lookup.dbpedia.org/}URI":
					uri = b_element.text

			for c_element in a_element:

				#searches for name of dbpedia entry and assigns it as variable
				if c_element.tag =="{http://lookup.dbpedia.org/}Label":
					name = c_element.text

			#checks that the name from the artist database matches the name of the dbpedia entry
			if str(name) == str(person_name):

				#prints dbpedia URI
				print (uri)

		
			
