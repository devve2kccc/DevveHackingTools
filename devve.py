import os
import sys

logo = '''\033[0m 
 ____                                
|  _ \             __   __                  ___
| | | |            \ \ / /                 / _ \   
| | | |             \ V /                 |  __/
|____/               \_/                   \___| 
                                              
              
           ___               __   __ 
          / _ \              \ \ / /   
         |  __/               \ V / 
          \___|                \_/\033[0m  \033[91m    \033[1m 
       }--{+} Coded By Devve {+}--{                             
     '''

menu = '''\033[0m
    {1}--Whois 
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--NMAP Scan
    {99}-Exit                                                                                                                   
 '''

print(logo)
print(menu)


def quit():
			con = input("Continue (Y/n) --> ")
			if con[0].upper() == 'N':
				exit()
			else:
				os.system("clear")
				print(logo)
				print(menu)
				select()
			

def select():
	try:
		choice = int(input("Devve~# "))
		if choice == 1:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
			os.system("curl http://api.hackertarget.com/whois/?q=" + ip)
			quit()

		elif choice == 2:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
 ____ ____   __   ___ ____ ____ _____ __  __ ____ ____ 
(_  _(  _ \ /__\ / __( ___(  _ (  _  (  )(  (_  _( ___)
  )(  )   //(__)( (__ )__) )   /)(_)( )(__)(  )(  )__) 
 (__)(_)\_(__)(__\___(____(_)\_(_____(______)(__)(____)
""")
			os.system("curl https://api.hackertarget.com/mtr/?q=" + ip)	
			print("")
			quit()

		elif choice == 3:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")	
			os.system("curl http://api.hackertarget.com/dnslookup/?q=" + ip)
			print("")
			quit() 

		elif choice == 4:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
 _____                            ____  _____ _____ 
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|
                                                    
	  """)
			os.system("curl https://api.hackertarget.com/reversedns/?q=" + ip )
			print("")
			quit()

		elif choice == 5:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __| (_) _| |_| |     
  \_____|\___|\___|_____|_|     
                                	
	""")
			os.system("curl https://api.hackertarget.com/geoip/?q=" + ip )
			print("")
			quit()

		elif choice == 6:
			ip = input("Enter IP or Domain: ")
			os.system("clear")
			print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
			os.system("curl https://api.hackertarget.com/nmap/?q=" + ip )
			print("")
			quit()


	except (KeyboardInterrupt):
		print("")
select()