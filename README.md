# Typeform SMS

This application integrates [Typeform webhooks](https://developer.typeform.com/webhooks/) + [AWS Lambda](https://aws.amazon.com/lambda/) + [Amazon API Gateway](https://aws.amazon.com/api-gateway/) + [Twilio](https://www.twilio.com/docs/sms/api) to receive automatic SMS notifications when a response is submitted to Typeform. 


<img src="https://i.imgur.com/yXrnhHY.png" alt="drawing" style="width:40px;"/>


In the example above, a local business owner receives automatic notifications when a response is submitted to [this Typeform survey](https://shubhaswamy1.typeform.com/to/ECQYOG). In order to receive custom text messages with your custom form, edit the contents in `lambda_function.py` accordingly and follow the [tutorial](https://www.google.com/) here.


### Requirements 

To test and deploy this you will need: 

- A Typeform account: your own custom Typeform with webhooks enabled

- An AWS account 

- A Twilio account:  `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TO_NUMBER`, `TWILIO_NUMBER` 

- Python 3.6.5 

  ```python
  pip install -r requirements.txt
  ```


### Setup and Usage

- Create a custom form to collect data on [Typeform](https://www.typeform.com).  
- Configure Twilio account and setup `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TO_NUMBER`, `TWILIO_NUMBER` in environment variables in AWS Lambda.
- Setup the Lambda function on AWS by copying the contents of `lambda_function.py`  and modifying it accordingly as stated above. 
- Link the code to the lambda function by adding the necessary triggers using Amazon API Gateway. 
- Set API variables under "Environment variables" in AWS. 
- Create a test in AWS with an empty JSON input to manually test the lambda function. 
- **Debugging**: Once the execution successfully completes, you should see a log message as seen below. If it fails to execute, fix the errors accordingly. Increase the "Timeout" threshold under "Basic settings" if a timeout occurs. 


<img src="https://i.imgur.com/FRDQTrS.png" alt="drawing" style="width:500px;"/>



License: [MIT](/LICENSE)
