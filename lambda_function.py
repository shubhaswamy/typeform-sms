from __future__ import print_function
import json
import boto3
import base64
import os
import urllib
from urllib import request, parse

print('Loading function')

# Twilio stuff; insert these keys below under environment variables 

#get environment variables into lambda function 
TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.environ.get("TO_NUMBER")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

def lambda_handler(event, context):
    d1 = json.dumps(event, indent=2)
    print("Received event: " + d1)
    
    l1 = json.loads(event['body']) #load responses 
    
    #declare variables we want to display in our Twilio SMS 
    name = ""
    foodRating = 0
    CSRating = 0
    satisfactionRating = 0


    #parse through Typeform data 
    for x in l1['form_response']['answers']: 
        answersID = x['field']['id']

        #get field ID's from your custom Typeform's API
        nameID = 'cqGsQnbWUFrO' #replace this 
        foodRatingID = 'AUg19Oo8DAR6' #replace this 
        CSRatingID = 'N5WIKDH55nC6' #replace this 
        satisfactionRatingID = 'enkMJA3vylY0' #replace this 
        

        #field types need to correspond to field types with ID's
        if (answersID == nameID):
            name = x['text'] #name
        if (answersID == foodRatingID):
            foodRating = x['number'] #food rating 
        if (answersID == CSRatingID):
            CSRating = x['number'] #customer service rating
        if (answersID == satisfactionRatingID):
            satisfactionRating = x['number'] #overall satisfaction rating 
            
    #call Twlio function to send message 
    sendmessage(name, foodRating, CSRating, satisfactionRating)    

    #return statement to test Lambda function    
    return {
    'statusCode': 200,
    'body': json.dumps({'message': 'hello world'})
    }
    

def sendmessage(name, foodRating, CSRating, satisfactionRating):

    #get twilio variables from environment variables 
    to_number = TO_NUMBER
    from_number = TWILIO_NUMBER

    #Custom body message; edit this to your own custom message 
    food = "Food quality:  "+str(foodRating) + " stars" + '\n'
    cs = "Customer service:  "+str(CSRating) + " stars" + '\n'
    satis = "Overall satisfaction:  "+str(satisfactionRating) + " stars" 
    body = name + " just submitted a satisfaction survey for your business."+ '\n' + food + cs +satis
    
    #error messages 
    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."
        
    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}
    
    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)
    
    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))
    
    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e
    
    #AWS lambda test
    return "SMS sent successfully!"
    

    
