import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from colorama import Fore                               
from colorama import Style
####### Colors   ###### 
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                           
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN                                          
sd  =   Style.DIM                                           
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
                                        
#######################
def banners():
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;    
             ;:::::'   :;     
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

        \n""".format(fg, fr, fg, sn)
        
    print(banner)

def getoption():
    print("Type Youtube url")
    print("End of url https://www.youtube.com/watch?v=GCc4hy8MEpI")
    print("Ex: GCc4hy8MEpI")
    url=input("Type Url Ex (GCc4hy8MEpI): ")
    youtubeviewer(url)


def youtubeviewer(url):
    try:
        howmanyview=input("How many View You want (Ex: 100): ")
        howmanyview = int(howmanyview)
        howmanytime=input("How many Watch Time in Second (Ex: 60): ")
        howmanytime = int(howmanytime)
        for i in range(howmanyview):
            geckodriver_autoinstaller.install()
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.socks", '127.0.0.1')
            profile.set_preference("network.proxy.socks_port", 9050)
            profile.set_preference("network.proxy.socks_remote_dns", False)
            profile.update_preferences()
            browser = webdriver.Firefox(firefox_profile=profile)
            browser.get('http://www.watchframebyframe.com/watch/yt/'+url)
            element = browser.find_element(By.XPATH,'//iframe[@id="player-iframe"]')
            element.click()
            time.sleep(howmanytime)
            browser.quit()
        
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass
        
banners()
getoption()
