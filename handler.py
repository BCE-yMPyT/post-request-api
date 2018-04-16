import json
import logging
import time



# time_now = {'time_is': str(int(time.time()))

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

    return response

    import smtplib
    email_user = 'interested.pink@gmail.com'
    email_password = 'Tolik9379992'
    
    email_send = data['email']

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_user,email_password)

    msg = data['time_is']
    server.sendmail(email_user, email_send, msg.as_string())
    server.quit()
