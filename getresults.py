import requests
import json
from collections import OrderedDict
import unicodedata
import ast

# api-endpoint



def printJSON(d): 
	fromVal = ""
	phoneNumber = ""
	recepient = ""
	message = ""
	
	for i in d['items']:
		for x in i['answers']:
			#print(" x: ", x)
			y = x['field']['id']
			#print(y)
			idVal = 'JomoOraxCZNn'

			idVal2 = 'shoDLZaF2OXS'
			idVal3 = 'eK0p6DZrF9rZ'
			idVal4 = 'dZ0AWx0czOJa'

			if (y == idVal):
				phoneNumber = (x['text']) #phone Number 

			if (y == idVal2):
				fromVal = (x['text']) #from 

			if (y == idVal3):
				recepient = (x['text']) #recepient 

			if (y == idVal4):
				message = (x['choice']['label']) #from 
			#typeVal = x['type']
			#print(x)
			#print(x['field']['text'])
			#print(type(x[typeVal]), x[typeVal])

			#print(unicodedata.normalize('NFC', x[typeVal]))

	#print(fromVal, " ", phoneNumber, " ", recepient, " ", message)
	return fromVal, phoneNumber, recepient, message





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

def runTypeform():
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
	fromVal, phoneNumber, recepient, message = printJSON(data)


	frm = unicodedata.normalize('NFKD', fromVal).encode('ascii','ignore')
	phone = unicodedata.normalize('NFKD', phoneNumber).encode('ascii','ignore')
	rcpt = unicodedata.normalize('NFKD', recepient).encode('ascii','ignore')
	msg = unicodedata.normalize('NFKD', message).encode('ascii','ignore')

	#print(type(retPhoneNum))
	#print(type(ret2))
	#print(ret2)

	#print(frm, phone, rcpt, msg)
	return frm, phone, rcpt, msg



	#print("done")

runTypeform()

#print(response.status_code)
#print(data)


#print(data)