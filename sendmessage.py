from twilio.rest import Client

account_sid = "AC11420ad1cc32bf375d45608bcb929338"
auth_token = "fbf462925f928f278315c00c229ef85e"
client = Client(account_sid, auth_token)

phoneNumber = "+19167051881"
sendMessage = "Hello from Python test"

message = client.messages.create(
    to=phoneNumber, 
    from_="+19165426597",
    body=sendMessage)

print(message.sid)
