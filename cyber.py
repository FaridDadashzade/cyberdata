import os

os.system("clear")

yaşıl = '\033[92m'
qırmızı = '\033[91m'
ağ = '\033[37m'
sarı = '\033[93m'
logo = """
░█████╗░██╗░░░██╗██████╗░███████╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝
"""

print(qırmızı + logo)

print(yaşıl + """C Y B Ξ R String Session Generator""")

print(ağ + "1. Telethon\n2. Pyrogram")

seçim = int(input(ağ + "\nBir seçim edin: "))

if ( seçim==1 ):
  os.system("git clone https://github.com/FaridDadashzade/cyberdata && cd cyberdata && pip install -r requirements.txt && python telethon.py")

if ( seçim==2 ):
  os.system("git clone https://github.com/FaridDadashzade/cyberdata && cd cyberdata && pip install -r requirements.txt && python pyrogram.py")
  
else:
	print("\nYanlış seçim...")
