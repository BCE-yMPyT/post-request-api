import smtplib

email_user = 'interested.pink@gmail.com'
email_password = 'Tolik9379992'
email_send = 'interested.pink@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(email_user,email_password)

msg = 'Hi there, sending this email from Python!'

server.sendmail(email_user,email_send,msg)
server.quit()
