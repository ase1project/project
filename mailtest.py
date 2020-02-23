from email.message import EmailMessage
import smtplib

def snedmail(toaddress,msginput):

    EMAIL = "sharezoneiiits@gmail.com"
    PASSWORD = "iiits2020"

    msg = EmailMessage()
    msg['Subject'] = 'EMAIL using python'
    msg['From'] = EMAIL
    msg['To'] = toaddress

    message = msginput
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com' , 465 ) as smtp:
        smtp.login(EMAIL,PASSWORD)
        smtp.send_message(msg)
print("Enter an email address to send")
toemail = input()
print("Enter the message you want to send (please enter the message in single line) ")
messageinput = input()
snedmail(toemail,messageinput)