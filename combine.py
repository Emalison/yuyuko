from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os
from selenium import webdriver
import time
import random
import smtplib

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def load_driver():
    options = webdriver.FirefoxOptions()

    # enable trace level for debugging
    options.log.level = "trace"

    options.add_argument("-remote-debugging-port=9224")
    options.add_argument("-headless")
    options.add_argument("-disable-gpu")
    options.add_argument("-no-sandbox")

    binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

    firefox_driver = webdriver.Firefox(
        firefox_binary=binary,
        executable_path=os.environ.get('GECKODRIVER_PATH'),
        options=options)

    return firefox_driver


driver = load_driver()
driver.get("https://app.growviews.com/#/login")
time.sleep(10)
scratch = driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div/div[2]/form/div[1]/input")
scratch.send_keys("charlesnganda001@gmail.com")
print("jkikk")
scratch = driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div/div[2]/form/div[2]/input")
scratch.send_keys("emalison81!")
time.sleep(3)
print("hjjj")
driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div/div[2]/form/div[3]/div/button").click()
time.sleep(6)
driver.get("https://app.growviews.com/#/earn/auto")
time.sleep(8)
print("okokjjj")
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/button").click()
time.sleep(6000)
driver.get("https://app.growviews.com/#/videos/add-video")
time.sleep(10)
scratch77 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/form/div[2]/input")
scratch77.send_keys("https://www.youtube.com/watch?v=vugL3C6uO7w")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/form/button[2]").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div[2]/span[2]/button").click()
time.sleep(6)
driver.quit()

