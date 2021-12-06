# -*- coding: utf-8 -*-
import time,json,random,requests,re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException
from pyvirtualdisplay import Display
import platform
import os.path as osp


#from bs4 import BeautifulSoup
#from random import choice
#import socket,uuid

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Get list of user agents.
#user_agents = user_agent_rotator.get_user_agents()

# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()

# def proxy_generator():
#     response = requests.get("https://sslproxies.org/")
#     soup = BeautifulSoup(response.content, 'html5lib')
#     proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
#     return proxy







    
    #chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    #chrome_options.add_argument("--verbose")
    #chrome_options.add_argument("--incognito")
    #chrome_options.add_argument('--proxy-server='+ PROXY)
    #chrome_options.add_extension(proxies_extension)
    #chrome_options.add_extension('/Users/macbookpro/Documents/GitHub/LATEST-UFAINFO/PY-TOP1/2.3.1_0.crx')
    
    


def search(KEYWWW,no_gui=True):
    
    options = Options()
    options.ensure_clean_session = True
    options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument(f'user-agent='+ user_agent_rotator.get_random_user_agent())
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if no_gui:
         options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    searchName = KEYWWW
    randomText = 'https://th.wikipedia.org/wiki/%E0%B8%9E%E0%B8%B4%E0%B9%80%E0%B8%A8%E0%B8%A9:%E0%B8%AA%E0%B8%B8%E0%B9%88%E0%B8%A1'
    setURL = 'https://th.wikipedia.org/w/index.php?search='+searchName+'&title=Special%3ASearch&go=Go&ns0=1'
    driver.get(setURL)
    time.sleep(1)
    #elem = driver.find_element_by_tag_name("body")
    print('')
    print("[+] Find KEY: "+ searchName)
    print('_________________________________')
    contenttext = driver.find_element_by_id("content").text
    #print(contenttext)


    time.sleep(2)
    driver.delete_all_cookies()
    driver.execute_script('localStorage.clear();')
    print('[+] Deleting all cookies...')
    #driver.quit()
    return contenttext

