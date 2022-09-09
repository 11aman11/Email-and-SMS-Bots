import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['From']="Aman Singh"
email['to']="amansingh.sonu28@gmail.com"
email['subject']="I hope this works!"
email.set_content("Let's check if this works or not")
with smtplib.SMTP(host="smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("amansingh.sonu28@gmail.com","elptpiflvizsuync")
    smtp.send_message(email)
    print("wish me luck")

