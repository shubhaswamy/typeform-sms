

from botocore.vendored import requests
import json
from collections import OrderedDict
import unicodedata
import ast


'''
Function for parsing through the JSON data 
data from API 
'''
def printJSON(d): 
	fromVal = ""
	phoneNumber = ""
	recepient = ""
	message = ""
	
	for i in d['items']:
		for x in i['answers']:
			
			y = x['field']['id']
			
			#ID Values are unique to the every field of unique question asked in Typeform survey 
			#replace idVals with corresponding questions from your custom form
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
			


	return fromVal, phoneNumber, recepient, message


'''
Main method for requesting data from Typeform API 
Pass in this function into lambda_function() to get the Typeform data
'''

def runTypeform():

	#insert ACCESS_TOKEN value from Typeform account
	ACCESS_TOKEN = "YOUR_ACCESS_TOKEN" 


	#Insert {form_id} value from custom Typeform
	URL = "https://api.typeform.com/forms/{form_id}/responses"
	 
	

	#request data and return JSON
	#Insert ACCESS_TOKEN value 
	response = requests.get(URL, headers={'authorization': 'bearer YOUR_ACCESS_TOKEN'})
	data = response.json()



	#grab data values 
	fromVal, phoneNumber, recepient, message = printJSON(data)



	#normalize data field values to string 
	frm = unicodedata.normalize('NFKD', fromVal).encode('ascii','ignore')
	phone = unicodedata.normalize('NFKD', phoneNumber).encode('ascii','ignore')
	rcpt = unicodedata.normalize('NFKD', recepient).encode('ascii','ignore')
	msg = unicodedata.normalize('NFKD', message).encode('ascii','ignore')

	
	#return all the value fields to use in lambda function
	return frm, phone, rcpt, msg


