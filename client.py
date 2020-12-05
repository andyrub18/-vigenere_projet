import socket
from datetime import datetime
from Vigenere import encrypt_text,decrypt_text,crack_key,crack
#fin des importations

IP = input("Enter the IP address: ")
t1 = datetime.now()
ttl = 1
PORT = 6332
with open('vigenere.txt', 'r') as file:
    data = file.read()
def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(ttl)
   result = s.connect_ex((addr,PORT))
   
   if result == 0:
      s.send(encrypt_text(data,"salut").encode())
      return 1
   else :
      return 0

def ping(addr):
      if (scan(addr)):
         t2 = datetime.now()
         total = t2 - t1
         print('Succes !!')
         print ("from {}: ttl={} time={} ".format(addr,ttl,total))
      else:
          print('Port unreachable')

      
ping(IP)