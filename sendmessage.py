from twilio.rest import Client
import getresults as tf 

account_sid = "AC11420ad1cc32bf375d45608bcb929338"
auth_token = "fbf462925f928f278315c00c229ef85e"
client = Client(account_sid, auth_token)

# FROM getresults file 
frm, phone, rcpt, msg = tf.runTypeform()

#print(getNum)

#end 


phoneNumber = phone
sendMessage = "Hi " + rcpt + "! " + msg

message = client.messages.create(
    to=phoneNumber, 
    from_="+19165426597",
    body=sendMessage)

print(message.sid)
