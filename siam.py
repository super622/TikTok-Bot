from tls_client     import Session
from re             import findall
from PIL            import Image
from io             import BytesIO
from requests       import get
from urllib.parse   import unquote
from base64         import b64decode
from time           import sleep, time
from colorama       import Fore, init; init()
from datetime       import datetime
from json           import load
#~~~~~~~~~~~~~~~LINK ZONE ~~~~~~~~~~~~~~~~~#
linksiam = str(input("ENTER LINK : "))
f = open("config.json", "w")
f.write(f'{linksiam}')
f.close()
f = open("config.json", "r")
time.sleep(2)
############ COLORZONE RANDOM ##########
import random
skillsiam = ["\033[0;32m", "\033[0;31m", "\033[1;31m", "\033[1;32m", "\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m"]
siamclr = random.choice(skillsiam)
# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
banner = f'''{siamclr}
  ██████    ██     █████      ███    ███
 ██         ██    ██   ██     ████  ████
  █████     ██    ███████     ██ ████ ██
      ██    ██    ██   ██     ██  ██  ██
 ██████     ██    ██   ██     ██      ██
{nc}
                        {siamclr}[TOOL : VIEW BOT]{nc}
'''
print(banner)

def fmt(string) -> str:
    return f"{Fore.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {Fore.BLUE}INFO {Fore.MAGENTA}__main__ -> {Fore.RESET}{string}"

class Client:
    def session() -> Session:
        return Session(client_identifier='chrome_108')
    
    def headers(extra: dict = {}) -> dict:
        return {
            **extra,
            "host"              : "zefoy.com",
            "connection"        : "keep-alive",
            "sec-ch-ua"         : "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
            "accept"            : "*/*",
            "x-requested-with"  : "XMLHttpRequest",
            "sec-ch-ua-mobile"  : "?0",
            "user-agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "origin"            : "https://zefoy.com",
            "sec-fetch-site"    : "same-origin",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-dest"    : "empty",
            "accept-encoding"   : "gzip, deflate, br",
            "accept-language"   : "en-US,en;q=0.9",
        }

class Captcha:
    def __init__(this, client: Session) -> None:
        this.client = client
    
    def solve(this) -> None:
        try:
            html           = str(this.client.get('https://zefoy.com', headers = Client.headers()).text).replace('&amp;', '&')
            captcha_token  = findall(r'<input type="hidden" name="(.*)">', html)[0]
            captcha_url    = findall(r'img src="([^"]*)"', html)[0]
            
            print(fmt(f'{green}captcha_token{nc}{yellow} :{nc} {red}{captcha_token}{nc}'))
            print(fmt(f'{green}captcha_url{nc}{yellow}:{nc} {red}{captcha_url}{nc}'))
            
            captcha_image  = get('https://zefoy.com' + captcha_url, headers = Client.headers(), cookies=this.client.cookies.get_dict()).content;
            image          = Image.open(BytesIO(captcha_image));image.show()
            
            captcha_answer = input(f'{cyan}solve captcha{green}: {nc}')
            
            response = this.client.post('https://zefoy.com', headers = Client.headers({"content-type": "application/x-www-form-urlencoded"}), data = {
                    "captcha_secure": captcha_answer,
                    captcha_token   : ""
            })
            
            key_1 = findall('(?<=")[a-z0-9]{16}', response.text)[0]
            
            print(fmt(f'{green}[{nc}{red}key_1{nc}{green}]{nc}{yellow} :{nc} {green}[{nc}{red}{key_1}{nc}{green}]{nc}'))
            
            return key_1
            
        except Exception as e:
            print(fmt(f'{red}FAILD TO SOLVE CAPTCHA (YOU HAVE BEEN BLOCKED) [{e}]{nc}'))
            return

class SIAM:
    def __init__(this, client: Session) -> None:
        this.client = client
        this.key = Captcha(client).solve()
        this.config = load(open('config.json', 'r'))

    def decode(this, text: str) -> str:
        return b64decode(unquote(text[::-1])).decode()
    
    def send(this, token: str, aweme_id: str) -> None:
        try:
            payload = f"--siam\r\nContent-Disposition: form-data; name=\"{token}\"\r\n\r\n{aweme_id}\r\n--siam--\r\n"
            response = this.decode(this.client.post("https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V", 
                data = payload, headers = Client.headers({"content-type": "multipart/form-data; boundary=siam",})).text.encode())
            
            if 'views sent' in response: 
                print(fmt(f'{red}[{nc}{bgreen} VIEWS SEND {nc}{red}]{nc} {bcyan}BY -{nc} {bpurple}(SIAM){nc} {bred}ID{nc} {yellow}:{nc} {red}[{nc}{green}{aweme_id}{nc}{red}]{nc}'))
                
            else:
                print(fmt(f'{red}[FAILD] TO SEND VIEWS{nc} {bred}ID{nc} {yellow}:{nc} {red}[{nc}{green}{aweme_id}{nc}{red}]'))

        except Exception as e:
            print(fmt(f'{red}[FAILD] TO SEND VIEWS{nc} {green}[{e}]{nc}'))
    
    def search(this, link: str) -> None:
        try:

            payload = f"--siam\r\nContent-Disposition: form-data; name=\"{this.key}\"\r\n\r\n{link}\r\n--siam--\r\n"
            response = this.decode(this.client.post("https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V", 
                data = payload, headers = Client.headers({"content-type": "multipart/form-data; boundary=siam",})).text.encode())
            
            if 'comviews' in response:
                token, aweme_id = findall(r'name="(.*)" value="(.*)" hidden', response)[0]
                print(fmt(f'{bcyan}SENDING TO{nc}{yellow}:{nc} {red}[{nc}{aweme_id}{red}]{nc} | {green}key_2{nc}{yellow}:{nc} {red}[{nc}{green}{token}{nc}{red}]{nc}'))
    
                sleep(3); this.send(token, aweme_id)
                
            else:

                timer = findall(r'ltm=(\d*);', response)[0]
                if int(timer) == 0:
                    return

                print(fmt(f'{red}TIME TO SLEEP{nc}{yellow}:{nc}{green} {timer}{nc}   '),  end="\r")

                start = time()
                while time() < start + int(timer):

                    print(fmt(f'{red}TIME TO SLEEP{nc}{yellow}:{nc} {green}{round((start + int(timer)) - time())}   {nc}'),  end="\r")
                    sleep(1)
                    
                print(fmt(f'{green}SENDING VIEWS...                {nc}'),  end="\r")

        except Exception as e:
            print(fmt(f'{red}Failed to search link {red}[{nc}{green}{e}{nc}{red}]{nc}'))
            print(fmt(response))
            return
    
    def mainloop(this) -> None:
        while True:
            this.search(this.config['link'])
            sleep(5)

if __name__ == '__main__':
    client = Client.session()
    SIAM  = SIAM(client).mainloop()
