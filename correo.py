# importacion de los paquetes necesarios
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# crear instancia de objeto de mensaje
msg = MIMEMultipart()
message = "Hola! Ya amanecio, es hora de despertar :D"

# configurar los parametros del mensaje
password = "contrasena"
msg['De'] = "kari.oc3@gmail.com"
msg['Para'] = "kari_oc3@hotmail.com"
msg['Tema'] = "Hora de despertar!"

# agregar en el cuerpo del mensaje
msg.attach(MIMEText(message, 'plain'))

# crear servidor 
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Credenciales de inicio de sesión para enviar el correo
server.login(msg['De'], password)

# Enviar el mensaje a través del servidor
server.sendmail(msg['De'], msg['Para'], msg.as_string())
server.quit()

print ("Correo enviado satisfactoriamente desde%s:" % (msg['Para']))