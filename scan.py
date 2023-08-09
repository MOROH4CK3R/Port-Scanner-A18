import socket
from time import sleep 


import colorama
from colorama import Fore, Style

colorama.init(Style.BRIGHT)


logo = """\
    _    _  ___    ____                                  
   / \  / |( _ )  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
  / _ \ | |/ _ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 / ___ \| | (_) |  ___) | (_| (_| | | | | | | |  __/ |   
/_/   \_\_|\___/  |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                         

    v1.0.1                      by @A18

"""


#print(logo)
print(Fore.RED + Style.BRIGHT + logo + Fore.RESET)



print("""
[1] scan host
[2] scan name_port
[3] scan number_port
""")
while True:
  x = int(input( "[?]: "))
  if x == 1:
      hostname = input("Enter the hostname : ")
      ip = socket.gethostbyname(hostname)
      print("---------------------")
      print(f' {hostname} ip =  {ip}')
  elif  x == 2:
      try:
          port_name = input("Enter the port name : ")
          port = socket.getservbyname(port_name)
          print("-"*40)
          print(f' {port_name}   port number : {port}')
      except:
          print('port not found!! ') 
  elif  x == 3:
      port_number = int(input("Enter the port number : "))
      service = socket.getservbyport(port_number)
      print("-"*40)
      print(f'{port_number}  port name :  {service}')
  else:
      print("Error !")
