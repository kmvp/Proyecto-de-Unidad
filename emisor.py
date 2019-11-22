from tkinter import *
from tkinter import scrolledtext
import serial, time
import threading
import socket
import struct
import subprocess

canal = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
arduino = serial.Serial('COM4', 9600)
despertador = ' * * Hola! Ya amanecio,\nes hora de despertar :D * *\n'
direccion_ip = '224.0.0.1'
puerto = 6000

pantalla = Tk() 
pantalla.title("Alerta Emisor") 
pantalla.geometry('350x490')  
chat = scrolledtext.ScrolledText(pantalla,width=40,height=30, bg='mint cream')
chat.tag_config("yo",foreground='midnight blue', font='Fixedsys 14')
chat.grid(column=1, row=0)

def con_serial():
    while(True):
        msjarduino = arduino.readline()
        texto = msjarduino.decode("utf-8")        
        print(texto)
        if (float(texto) >= 700 and float(texto)<= 999):
            chat.insert(INSERT,texto,"yo")
            canal.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
            canal.sendto((str.encode(despertador)), (direccion_ip, puerto))
            #os.system('msj.py')
            result=subprocess.getoutput('correo.py')

hilo = threading.Thread(target = con_serial)
hilo.start()

pantalla.mainloop()