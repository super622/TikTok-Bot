import requests, re, os, random
from bs4 import BeautifulSoup as bs
import urllib.parse
from urllib.parse import urlparse
import base64,datetime,time,inquirer,sys
from colorama import init, Fore
init(autoreset=True)


url = 'https://zefoy.com/'
api = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAUbA4T8UWO-pw750uQqz0X2deq9lHLuLk'
hed = {"origin": "https://zefoy.com","user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2180) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36","x-requested-with": "XMLHttpRequest",'Host': 'zefoy.com'}

image = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠉⢻⢦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠈⣷⣇	 ⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀Tools   : Tiktok 2023
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⡷⣽⡆
⠀⠀⠀⢀⣠⠴⠒⠚⠛⠛⣦⡀⢸⡇⠀⠀⠀⢸⡻⣶⣤⣄⣀⣀⣟⢾⡇
⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⡟⢿⢸⡇⠀⠀⠀⢸⣝⡏⠙⠳⠬⢷⣌⣿⠇
⢠⠏⠀⠀⠀⠀⢀⡤⢤⡴⣟⢾⢸⡇⠀⠀⠀⢸⣌⡇⠀⠀⠀⠀⠀⠀⠀
⡞⠀⠀⠀⠀⡴⢯⣙⣦⠽⠾⠿⢸⡇⠀⠀⠀⢸⣌⡇⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⢸⡓⢤⠟⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⣌⡇⠀⠀⠀⠀⠀⠀⠀
⣇⠀⠀⠀⠈⢿⣾⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⡾⢮⡇⠀⠀⠀⠀⠀⠀⠀
⠹⡄⠀⠀⠀⠀⠙⠳⠤⠤⠖⠋⠀⠀⠀⠀⣰⡛⢦⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⢧⣙⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⢶⣤⣄⣀⣀⣀⣀⣠⣤⠾⣏⠙⣦⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠳⠽⣮⣻⣌⣳⣬⠷⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def capcha():
	global phpsessid 
	ses = requests.Session()
	respon = ses.get(url,headers=hed).text
	resp   = bs(respon,'html.parser')
	parse  = resp.find('img')
	data   = url + parse['src']
	img    = ses.get(data,headers=hed)
	open('img.png','wb').write(img.content)
	phpsessid = ses.cookies.get_dict()['PHPSESSID']
	login(ses)

def captcha_solver():
	solve_captcha = requests.post(
	api,
	headers={'Content-Type': 'application/json','Host': 'vision.googleapis.com','x-android-package': 'image.to.text.ocr','x-android-cert': 'ad32d34755bb3b369a2ea8dfe9e0c385d73f80f0',},
	json={"requests": [{"image": {"content": base64.b64encode(open('img.png', 'rb').read()).decode('utf-8')},"features": [{"type": "TEXT_DETECTION","maxResults": 1}]}]})
	return solve_captcha.json()['responses'][0]['textAnnotations'][0]['description'].lower()

def login(ses):
	solver = captcha_solver()
	try:
		hed['cookie'] = "PHPSESSID=" + phpsessid
		hed['content-type'] = "application/x-www-form-urlencoded; charset=UTF-8"
		data = {
		'captcha_secure':solver,
		'r75619cf53f5a5d7aa6af82edfec3bf0':''}
		post_captcha = ses.post(
		url,
		headers = hed,
		data = data
		)
		soup = bs(post_captcha.text, 'html.parser')
		key = soup.find('input', {'placeholder': 'Enter Video URL'}).get('name')
		menu(key,ses)
	except Exception as e:capcha()


def menu(key,ses):
	global video
	os.system('clear')
	print(image)
	sys.path.append(os.path.realpath("."))
	questions = [
	inquirer.List(
        	"select",
        	message="Menu",
        	choices=["Auto Views","Auto Shares + Views", "Auto Favorites + Views","Exit"],
    		),
	]
	answers = inquirer.prompt(questions)
	zett = answers.get("select")
	if zett in 'Auto Views':
		video = input(f' - Ex : https://www.tiktok.com/@xxx/video/xxx\n - Video : ')
		uid = 'c2VuZC9mb2xsb3dlcnNfdGlrdG9V' 
		for i in range(9999999):sendview(key,ses,uid)
	elif zett in 'Auto Shares + Views':
		video = input(f' - Ex : https://www.tiktok.com/@xxx/video/xxx\n - Video : ')
		uid = 'c2VuZC9mb2xsb3dlcnNfdGlrdG9s' 
		for i in range(9999999):sendview(key,ses,uid)
	elif zett in 'Auto Favorites + Views':
		video = input(f' - Ex : https://www.tiktok.com/@xxx/video/xxx\n - Video : ')
		uid = 'c2VuZF9mb2xsb3dlcnNfdGlrdG9L'
		for i in range(9999999):sendview(key,ses,uid)

def sendview(key,ses,uid):
	print('')
	hed['cookie'] = "PHPSESSID=" + phpsessid
	request_send_views = ses.post(
	url + uid,
	headers = hed,
	data = {
	key : video,
	}
	)
	decode = base64.b64decode(urllib.parse.unquote(request_send_views.text[::-1])).decode()
	try:
		view = re.search('></i>(.*?)</button>',str(decode)).group(1)
		print(f"[ {str(datetime.datetime.now())} ]{Fore.LIGHTGREEN_EX} Successfully Sent {view}")
	except:pass

	if "An error occurred. Please try again." in decode: 
		decode = force_send_views(
		url_video=video,
		old_request=decode,
		uid = uid
		)

	try:wait = (re.search(r"ltm=[0-9]+", decode).group(0).replace("ltm=", ""))
	except:wait = (re.findall(r" = [0-9]+", decode))
	for i in range(int(wait), 0, -1):
		print(f"\r[ {str(datetime.datetime.now())} ]{Fore.LIGHTYELLOW_EX} Please wait {str(i)} seconds", end="\r")
		time.sleep(1)

def force_send_views(url_video, old_request,uid):
	if 'tiktok' in url_video:
		if len(urlparse(url_video).path.split('/')[-1]) == 19:
			valid_id = urlparse(url_video).path.split('/')[-1]
		else:False
	else:False

	parse = bs(old_request, 'html.parser')
	hed['cookie'] = "PHPSESSID=" + phpsessid
	request_send_views = requests.post(
	url=url + uid,
	headers=hed,
	data={
	parse.find('input', {'type': 'text'}).get('name'): valid_id,
	}
	)
	decode = base64.b64decode(urllib.parse.unquote(request_send_views.text[::-1])).decode()
	return decode

capcha()
