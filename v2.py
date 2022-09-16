import os
from os import system, name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from PIL import Image
from alive_progress import alive_bar
import psutil



#Script
OPTIONS = 5
#User
Views = 0
Follows = 0
Likes = 0
Shares = 0

def clear():
    if name == 'nt':
        _ = system('cls')

def title():
    clear()
    print(r"""
     _________  ___  ___  __    __________  ________  ___  ___   ________     
    |\___   ___\\  \|\  \|\  \ |\___   ___\|\   __  \|\  \|\  \ |\   __  \    
    \|___ \  \_| \  \ \  \/  /_\|___ \  \_|\ \  \ \  \ \  \/  /_\ \  \_\  \   
         \ \  \ \ \  \ \   ___  \   \ \  \  \ \  \ \  \ \   ___  \ \   _  _\  
          \ \  \ \ \  \ \  \\ \  \   \ \  \  \ \  \_\  \ \  \\ \  \ \  \\  \  
           \ \__\ \ \__\ \__\\ \__\   \ \__\  \ \_______\ \__\\ \__\ \__\\ _\ 
            \|__|  \|__|\|__| \|__|    \|__|   \|_______|\|__| \|__|\|__|\|__|    by @ersignee""")
    print("\n")

def menu():
    print("[1] Views\n[2] Likes\n[3] Followers\n[4] Shares\n[5] Credits\n\n[0] Exit\n")
    s = int(input("Select: "))
    if s<0 or s>OPTIONS:
        print("Invalid selection.")
        exit()
    else:
        return s

def exitmenu():
    print("\n\n[0] Exit\n")
    s = int(input("Select: "))
    if s!=0:
        print("Invalid selection.")
        exitmenu()
    else:
        clear()
        exit()

def captcha():
    print("Waiting for captcha...")
    #OPEN PAGE#
    driver.get("https://zefoy.com/")
    time.sleep(random.randint(5,10))
    driver.get_screenshot_as_file("captcha.png")
    im = Image.open('captcha.png').convert('L')
    im = im.crop((255, 55, 543, 200))
    im.save('captcha.png')
    im.show()
    #ASK USER TO INPUT CAPTCHA FROM GIVEN IMAGE
    title()
    captchaa = str(input("Captcha(once submitted you can close the image): "))
    #Complete captcha
    inputElement = driver.find_element(by=By.XPATH,value='//input[@name="captcha_secure"]')
    inputElement.send_keys(captchaa)
    driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary btn-lg btn-block rounded-0 a218b4367b97e62d147"]').click()
    #Find Miscrfosoft.Photos image viewer and close it
    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()
    #delete captcha image file
    os.remove('captcha.png')


def opt1():
    enabled = driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu4"]').is_enabled()
    if enabled == True:
        #SELECT VIEWS TAB
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu4"]').click()
        time.sleep(1)
    else:
        print("Option temporarily unavailable. Try again later.")
        exit()

    #ask for video url
    videourl=str(input("Video URL: "))
    views = int(input("Views(Min. 1000 - 3min wait for every 1000): "))
    views = views // 1000
    mintocomplete = (views*3) - 3
    print("The process will take approximately",mintocomplete,"minutes.")
    #PASTE URL
    urlinput = driver.find_element(by=By.XPATH,value='//*[@id="sid4"]/div/form/div/input')
    urlinput.click()
    urlinput.send_keys(videourl)
    time.sleep(1)
    
    with alive_bar(views, enrich_print = False, force_tty=True, stats=False, elapsed=False) as bar:
        i = 0
        while i <= views:
            #CLICK SEARCH
            urlinput.submit()
            time.sleep(5)
            #CLICK ON CONFIRM BUTTON
            try:
                driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
            except:
                timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/h4').text.split(" ")
                print("Try again in", int(timeleft[2])+1," minutes.")
                exit()
            
            time.sleep(5)
            #get time left until next click
            timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/h4').text.split(" ")
            timeleft = int(timeleft[2])+1
            print("Time left to the next ~1000 views:", timeleft)

            i+=1
            if i<views:
                bar()
            elif i==views:
                bar()
                print("You successfully recived",views*1000,"views.")
                break
            time.sleep(timeleft*60)
            
    exitmenu()

def opt2():
    enabled = driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu2"]').is_enabled()
    if enabled == True:
        #SELECT SHARE TAB
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu2"]').click()
        time.sleep(1)
    else:
        print("Option temporarily unavailable. Try again later.")
        exit()

    #ask for video url
    videourl=str(input("Video URL: "))
    likes = int(input("Likes(Min. 25 - 16min wait for every 25): "))
    likes = likes // 25
    mintocomplete = (likes*16) - 16
    print("The process will take approximately",mintocomplete,"minutes.")
    #PASTE URL
    urlinput = driver.find_element(by=By.XPATH,value='//*[@id="sid2"]/div/form/div/input')
    urlinput.click()
    urlinput.send_keys(videourl)
    time.sleep(1)

    with alive_bar(likes, enrich_print = False, force_tty=True, stats=False, elapsed=False) as bar:
        i = 0
        while i <= likes:
            #CLICK SEARCH
            urlinput.submit()
            time.sleep(5)
            #CLICK ON CONFIRM BUTTON
            try:
                driver.find_element(by=By.XPATH,value='//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
            except:
                timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/h4').text.split(" ")
                print("Try again in", int(timeleft[2])+1," minutes.")
                exit()
            
            time.sleep(5)
            #get time left until next click
            timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/h4').text.split(" ")
            timeleft = int(timeleft[2])+1
            print("Time left to the next ~25 likes:", timeleft)
            
            i+=1
            if i<likes:
                bar()
            elif i==likes:
                bar()
                print("You successfully recived",likes*25,"likes.")
                break
            time.sleep(timeleft*60)
            
    exitmenu()

def opt3():
    enabled = driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu"]').is_enabled()
    if enabled == True:
        #SELECT SHARE TAB
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu"]').click()
        time.sleep(1)
    else:
        print("Option temporarily unavailable. Try again later.")
        exit()

def opt4():
    enabled = driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu7"]').is_enabled()
    if enabled == True:
        #SELECT SHARE TAB
        driver.find_element(by=By.XPATH,value='//button[@class="btn btn-primary rounded-0 menu7"]').click()
        time.sleep(1)
    else:
        print("Option temporarily unavailable. Try again later.")
        exit()

    #ask for video url
    videourl=str(input("Video URL: "))
    shares = int(input("Shares(Min. 300 - 3min wait for every 300): "))
    shares = shares // 300
    mintocomplete = (shares*3) - 3
    print("The process will take",mintocomplete,"minutes.")
    #PASTE URL
    urlinput = driver.find_element(by=By.XPATH,value='//*[@id="sid7"]/div/form/div/input')
    urlinput.click()
    urlinput.send_keys(videourl)
    time.sleep(1)

    with alive_bar(shares, enrich_print = False, force_tty=True, stats=False, elapsed=False) as bar:
        i = 0
        while i <= shares:
            #CLICK SEARCH
            urlinput.submit()
            time.sleep(5)
            #CLICK ON CONFIRM BUTTON
            try:
                driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click()
            except:
                timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/h4').text.split(" ")
                print("Try again in", int(timeleft[2])+1," minutes.")
                exit()
            
            time.sleep(5)
            #get time left until next click
            timeleft = driver.find_element(by=By.XPATH,value='//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/h4').text.split(" ")
            timeleft = int(timeleft[2])+1
            print("Time left to the next ~300 shares:", timeleft)
            
            i+=1
            if i<shares:
                bar()
            elif i==shares:
                bar()
                print("You successfully recived",shares*300,"shares.")
                break
            time.sleep(timeleft*60)
    exitmenu()

def opt5():
    print("[+]This script was originally created by @ersignee. [https://github.com/ersignee]")
    exitmenu()



######################################################################################################################################################################################
######################################################################################################################################################################################

clear()
system('title TikTokr')

print(r"""
 _________  ___  ___  __    __________  ________  ___  ___   ________     
|\___   ___\\  \|\  \|\  \ |\___   ___\|\   __  \|\  \|\  \ |\   __  \    
\|___ \  \_| \  \ \  \/  /_\|___ \  \_|\ \  \ \  \ \  \/  /_\ \  \_\  \   
     \ \  \ \ \  \ \   ___  \   \ \  \  \ \  \ \  \ \   ___  \ \   _  _\  
      \ \  \ \ \  \ \  \\ \  \   \ \  \  \ \  \_\  \ \  \\ \  \ \  \\  \ 
       \ \__\ \ \__\ \__\\ \__\   \ \__\  \ \_______\ \__\\ \__\ \__\\ _\ 
        \|__|  \|__|\|__| \|__|    \|__|   \|_______|\|__| \|__|\|__|\|__|    v2""")
print("\n")
#Chrome driver arguments
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--incognito')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#Driver & Actions Init
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install())) #executable_path='chromedriver'
action = ActionChains(driver)

#Resolve Captcha (only first time you open the program)
captcha()

#Menu
title()
selection = menu()

#Selection
if selection == 1:
    title()
    opt1()
elif selection == 2:
    title()
    opt2()
elif selection == 3:
    title()
    opt3()
elif selection == 4:
    title()
    opt4()
elif selection == 5:
    title()
    opt5()
elif selection == 0:
    exit()
