import socket, threading, concurrent.futures, colorama, os, sys, fade, time, pyfade
from colorama import Fore

colorama.init()

def purple(text):
    os.system(""); faded = ""; down = False
    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 30
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

os.system('cls')
title = "Simple-Ryanz"
os.system(f'title {title}')
print(Fore.RED + f"""
        
        ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗███████╗
        ██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║╚══███╔╝
        ██████╔╝ ╚████╔╝ ███████║██╔██╗ ██║  ███╔╝ 
        ██╔══██╗  ╚██╔╝  ██╔══██║██║╚██╗██║ ███╔╝  
        ██║  ██║   ██║   ██║  ██║██║ ╚████║███████╗
        ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
                                           
                                                                                                
                                                            
  
  {Fore.GREEN + ("          [>] Type: Port Scanner")}
  {Fore.GREEN + ("          [>] By Ryanz")}

""")

print_lock = threading.Lock()


siteip = input(Fore.RED +"            [!] Website URL: ")
print("\n")
os.system(f"title {siteip}")
ip = f"{socket.gethostbyname(siteip)}"

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            os.system(f"title {ip}:{port}")
            print(Fore.BLUE + f"            [+] " + Fore.WHITE + f"Port: [{port}]" + Fore.GREEN + " Port Open")
    except:
        pass
    
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(11111):
        executor.submit(scan, ip, port)

print("\n")
input(Fore.RED + f"            [!] All Port scanned for {siteip}, press enter to exit: ")
time.sleep(1)
sys.exit(1234)
