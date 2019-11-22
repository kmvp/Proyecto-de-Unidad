from tkinter import *
from tkinter import scrolledtext
import threading
import socket
import struct

ip_multicast = '224.0.0.1'
direccion = '0.0.0.0'
puerto = 6000

canal = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
chatmulticast = socket.inet_aton(ip_multicast) + socket.inet_aton(direccion)

canal.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, chatmulticast)
canal.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

canal.bind((direccion, puerto))

pantalla = Tk() 
pantalla.title("Despertador receptor") 
pantalla.geometry('350x490')
chat = scrolledtext.ScrolledText(pantalla,width=40,height=30, bg='mint cream')
chat.tag_config("yo",foreground='midnight blue', font='Fixedsys 14')
chat.grid(column=1, row=0)

def con_serial():
    while True:
        texto, dirr = canal.recvfrom(255)
        chat.insert(INSERT,texto,"yo")
        chat.insert(INSERT,'\n')
        print (texto)

hilo = threading.Thread(target = con_serial)
hilo.start()
pantalla.mainloop()