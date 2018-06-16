import requests
import json
from collections import OrderedDict
import unicodedata
import ast

# api-endpoint

ACCESS_TOKEN = "HrHtpTSH1ZpVZgoK9gdVZy5m66FTgSME8yA5h25rSemq"

#URL2 = "https://api.typeform.com/v1/form/ht2toX?key=HrHtpTSH1ZpVZgoK9gdVZy5m66FTgSME8yA5h25rSemq"
URL = "https://api.typeform.com/forms/ht2toX/responses"
 
# location given here

response = requests.get(URL, headers={'authorization': 'bearer HrHtpTSH1ZpVZgoK9gdVZy5m66FTgSME8yA5h25rSemq'})
data = response.json()


#data2 = json.loads(data.decode('utf-8'), object_pairs_hook=OrderedDict)
#data2 =json.dumps(data)


#print(data2)
#response2 = requests.get(URL2)
#data2 = response2.json()

#print(data3)


#with open('data.txt', 'w') as outfile:  
	#json.dump(data, outfile)


def printJSON(d): 
	phoneNumber = ""
	
	for i in d['items']:
		for x in i['answers']:
			#print(" x: ", x)
			y = x['field']['id']
			idVal = 'JomoOraxCZNn'
			if (y == idVal):
				print(x['text'])
			#typeVal = x['type']
			#print(x)
			#print(x['field']['text'])
			#print(type(x[typeVal]), x[typeVal])

			#print(unicodedata.normalize('NFC', x[typeVal]))





	'''
	phoneNumber = ""
	for i in d['items']:
		for x in i['answers']:
			print(x['field'])

			
			typeVal = x['type']
			#print(x)
			#print(x['field']['text'])
			print(type(x[typeVal]), x[typeVal])

			#print(unicodedata.normalize('NFC', x[typeVal]))

	'''

printJSON(data)

print("done")


#print(response.status_code)
#print(data)


#print(data)