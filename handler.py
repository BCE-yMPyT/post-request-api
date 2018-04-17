'''
This script used AWS Lambda for sending email. When you send
POST request in API Development Environment in JSON format like:
{"email": 'your@email.stuff'}, this script will send to your@email.stuff,
time in UNIX_TIMESTAMP.
'''
import json
import logging
import time

def hello(event, context):

    data = json.loads(event['body'])
    data1 = {}
    data1['time_is'] = str(int(time.time()))
    data.update(data1)

    if 'email' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422, 'body': json.dumps({'error_message': 'Empty field'})}

    response = {
        "statusCode": 200,
        "body": json.dumps(data),
    }

    import smtplib
    email_user = 'your@email.stuff'
    email_password = 'your_password'

    email_send = data['email']

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_user,email_password)

    msg = data['time_is']
    server.sendmail(email_user, email_send, msg)
    server.quit()

    return response
