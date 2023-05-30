from email.message import EmailMessage
from app2 import password 
import ssl 
import smtplib
email_sender = "Rouhialmadani@gmail.com"
email_password = password

email_reciever = 'pabemef668@dogemn.com'

subject = "dont forget to subscribe"
body = """
whet you watch video please hit subscribe
 """

em = EmailMessage()
em["from"] = email_sender
em ['to'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
    