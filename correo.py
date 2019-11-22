# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# create message object instance
msg = MIMEMultipart()
message = "Hola! Ya amanecio, es hora de despertar :D"
# setup the parameters of the message
password = "Florecita29.."
msg['From'] = "kari.oc3@gmail.com"
msg['To'] = "kari_oc3@hotmail.com"
msg['Subject'] = "Hora de despertar!"
# add in the message body
msg.attach(MIMEText(message, 'plain'))
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail
server.login(msg['From'], password)
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("successfully sent email to %s:" % (msg['To']))