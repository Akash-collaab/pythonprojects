from email.message import EmailMessage
from python_app2 import password
import ssl
import smtplib


email_sender = 'akashgupta84957@gmail.com'
email_password = password

email_reciever = 'lesoy67468@edinel.com'

subject = "D on't forget to thanks me"
body = """ Don't forget to practice by yourself"""

# Creating Instance 

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

   
  

