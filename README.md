# Typeform SMS

This application integrates [Typeform](https://developer.typeform.com/responses/) + [AWS Lambda](https://aws.amazon.com/lambda/) + [Twilio](https://www.twilio.com/docs/sms/api) to receive automatic SMS notifications when a response is submitted to Typeform. 



<img src="https://i.imgur.com/8cYQaVa.jpg" alt="drawing" style="width:200px;"/>



In the example above, the recipient received a text based on a custom response to [this Typeform survey](https://shubhaswamy.typeform.com/to/ht2toX). In order to receive custom text messages with your custom form, edit the `form_id` and `your_access_token` and other contents in `getmessage.py` accordingly .

### Requirements 

To test and deploy this you will need: 

- A Typeform account: a `FORM_ID` for your custom form and `YOUR_ACCESS_TOKEN`

- An AWS account 

- A Twilio account:  `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` and source phone number 

- Python 3.6.5, 

  ```python
  pip install -r requirements.txt
  ```

### Setup and Usage

- Create a custom form to collect data on [Typeform](https://www.typeform.com) and update  `getmessage.py`  accordingly. 
- Configure Twilio account and setup `FROM_NUMBER` in `lambda_function.py`.
- Setup the Lambda function on AWS by copying the contents of `getmessage.py`  and `lambda_function.py`  and modifying it accordingly as stated above. 
- Link the code to the lambda function by adding the necessary triggers. Set API variables under "Environment variables" in AWS. 
- Create a test in AWS with an empty JSON input to manually test the lambda function. 
- **Debugging**: Once the execution successfully completes, you should see a log message as seen below. If it fails to execute, fix the errors accordingly. Increase the "Timeout" threshold under "Basic settings" if a timeout occurs. 

<img src="https://i.imgur.com/FRDQTrS.png" alt="drawing" style="width:500px;"/>





License: [MIT](/LICENSE)