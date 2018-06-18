import base64
import json
import os
import urllib
import getresults as tf #.py file gets data from Typeform
from urllib import request, parse
 

#Twilio SMS URL
TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
 
 
def lambda_handler(event, context):

	#call main function to get Typeform data 
    frm, phone, rcpt, msg = tf.runTypeform()
    to_number = phone #gets phone number from details filled out in the Typeform 
    from_number = "+19165426597" #replace with your Twilio Phone Number 
    body = msg #custom message from Typeform
 

 	#error messages fro AWS 
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


 
 	#catch exception
    try:
        # perform HTTP POST request

        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))

    except Exception as e:
        # something went wrong!
        return e



 
    return "SMS sent successfully!" #yay! 
