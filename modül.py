import subprocess
import platform
from os import system

# colorama'yı yükleme kontrolü
try:
    import colorama
    from colorama import Fore, init, Style
except ModuleNotFoundError:
    print("colorama modülü bulunamadı, yükleniyor...")
    subprocess.run(["pip", "install", "colorama"])
    import colorama
    from colorama import Fore, init, Style

# İşletim sistemine göre ekranı temizle
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

# Başlık yazısı
from colorama import Fore, Style, init
import time
init(autoreset=True)
ascii_art = '''


$$\   $$\ $$\   $$\ $$$$$$$\  $$\   $$\ $$\      $$\   $$\ $$\      $$\       $$$$$$$\   $$$$$$\   $$$$$$\  $$\        $$$$$$\  $$$$$$$\  $$$$$$\ 
$$ | $$  |$$ |  $$ |$$  __$$\ $$ |  $$ |$$ |     $$ |  $$ |$$$\    $$$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$\ \_$$  _|
$$ |$$  / $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |     $$ |  $$ |$$$$\  $$$$ |      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |      $$ /  $$ |$$ |  $$ |  $$ |  
$$$$$  /  $$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |     $$ |  $$ |$$\$$\$$ $$ |      $$$$$$$\ |$$$$$$$$ |\$$$$$$\  $$ |      $$$$$$$$ |$$ |  $$ |  $$ |  
$$  $$<   $$ |  $$ |$$  __$$< $$ |  $$ |$$ |     $$ |  $$ |$$ \$$$  $$ |      $$  __$$\ $$  __$$ | \____$$\ $$ |      $$  __$$ |$$ |  $$ |  $$ |  
$$ |\$$\  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |     $$ |  $$ |$$ |\$  /$$ |      $$ |  $$ |$$ |  $$ |$$\   $$ |$$ |      $$ |  $$ |$$ |  $$ |  $$ |  
$$ | \$$\ \$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$$$\\$$$$$$  |$$ | \_/ $$ |      $$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |  $$ |$$$$$$$  |$$$$$$\ 
\__|  \__| \______/ \__|  \__| \______/ \________|\______/ \__|     \__|      \_______/ \__|  \__| \______/ \________|\__|  \__|\_______/ \______|
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  

'''
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
for i, line in enumerate(ascii_art.split('\n')):
    print(colors[i % len(colors)] + line)
    time.sleep(0.1)
# request.txt dosyasından modülleri yükleme fonksiyonu
def install_from_file(file_name):
    with open(file_name, 'r') as file:
        modules = file.readlines()
        modules = [module.strip() for module in modules]

    for module in modules:
        print(f"Modül kuruluyor:{Fore.RED} {module}")
        result = subprocess.run(["pip3", "install", "--user", module], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{module} başarıyla kuruldu.{Fore.GREEN}")
        else:
            print(f"{module} kurulumu sırasında bir hata oluştu:{Fore.RED} {result.stderr}")

# request.txt dosyasından modülleri yükle
install_from_file('request.txt')

# Diğer belirtilen modülleri yükle
modules = [
    "psutil",
    "pypresence",
    "discord==1.7.3",
    "discord.py==1.7.3",
    "asyncio",
    "colorama",
]

for module in modules:
    print(f"Modül kuruluyor: {module}")
    result = subprocess.run(["pip3", "install", "--user", module], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{module} başarıyla kuruldu.")
    else:
        print(f"{module} kurulumu sırasında bir hata oluştu: {result.stderr}")
