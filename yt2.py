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

driver.get("https://mobile.betlion.ke/Login/login")
time.sleep(5)

username2 = driver.find_element_by_id("userMobile")
password2 = driver.find_element_by_id("userPass")
sele = input("Enter a number: ")
pos = input("Enter a passcode: ")
# 0770244721
username2.send_keys(sele)
password2.send_keys(pos)
time.sleep(2)

driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/button/span").click()
time.sleep(10)

driver.get("https://pick6.betlion.ke/predictions")
time.sleep(10)

driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/button").click()
time.sleep(3)

bn1 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[4]/div[3]/button[1]')
bn2 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[4]/div[5]/button[1]')
bn3 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[5]/div[3]/button[1]')
bn4 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[5]/div[5]/button[1]')
bn5 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[6]/div[3]/button[1]')
bn6 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[6]/div[5]/button[1]')
bn7 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[7]/div[3]/button[1]')
bn8 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[7]/div[5]/button[1]')
bn9 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[8]/div[3]/button[1]')
bn10 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[8]/div[5]/button[1]')
bn11 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[9]/div[3]/button[1]')
bn12 = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[9]/div[5]/button[1]')

scores = ["10", "20", "21", "00", "11", "01", "02", "12"]

score1 = random.choice(scores)
time.sleep(6)

if score1 == "10":
    bn1.click()
    print(score1)

if score1 == "20":
    bn1.click()
    bn1.click()
    print(score1)

if score1 == "21":
    bn1.click()
    bn1.click()
    bn2.click()
    print(score1)

if score1 == "11":
    bn1.click()
    bn2.click()
    print(score1)

if score1 == "01":
    bn2.click()
    print(score1)

if score1 == "02":
    bn2.click()
    bn2.click()
    print(score1)

if score1 == "12":
    bn1.click()
    bn2.click()
    bn2.click()
    print(score1)

    # SCORES 2
time.sleep(5)
score2 = random.choice(scores)

if score2 == "10":
    bn3.click()
    print(score2)

if score2 == "20":
    bn3.click()
    bn3.click()
    print(score2)

if score2 == "21":
    bn3.click()
    bn3.click()
    bn4.click()
    print(score2)

if score2 == "11":
    bn3.click()
    bn4.click()
    print(score2)

if score2 == "01":
    bn4.click()
    print(score2)

if score2 == "02":
    bn4.click()
    bn4.click()
    print(score2)

if score2 == "12":
    bn3.click()
    bn4.click()
    bn4.click()
    print(score2)

    # SCORES 3
time.sleep(2)
score3 = random.choice(scores)

if score3 == "10":
    bn5.click()
    print(score3)

if score3 == "20":
    bn5.click()
    bn5.click()
    print(score3)

if score3 == "21":
    bn5.click()
    bn5.click()
    bn6.click()
    print(score3)

if score3 == "11":
    bn5.click()
    bn6.click()
    print(score3)

if score3 == "01":
    bn6.click()
    print(score3)

if score3 == "02":
    bn6.click()
    bn6.click()
    print(score3)

if score3 == "12":
    bn5.click()
    bn6.click()
    bn6.click()
    print(score3)

    # SCORES 4
time.sleep(2)
score4 = random.choice(scores)

if score4 == "10":
    bn7.click()
    print(score4)

if score4 == "20":
    bn7.click()
    bn7.click()
    print(score4)

if score4 == "21":
    bn7.click()
    bn7.click()
    bn8.click()
    print(score4)

if score4 == "11":
    bn7.click()
    bn8.click()
    print(score4)

if score4 == "01":
    bn8.click()
    print(score4)

if score4 == "02":
    bn8.click()
    bn8.click()
    print(score4)

if score4 == "12":
    bn7.click()
    bn8.click()
    bn8.click()
    print(score4)

    # SCORES 5
time.sleep(2)
score5 = random.choice(scores)

if score5 == "10":
    bn9.click()
    print(score5)

if score5 == "20":
    bn9.click()
    bn9.click()
    print(score5)

if score5 == "21":
    bn9.click()
    bn9.click()
    bn10.click()
    print(score5)

if score5 == "11":
    bn9.click()
    bn10.click()
    print(score5)

if score5 == "01":
    bn10.click()
    print(score5)

if score5 == "02":
    bn10.click()
    bn10.click()
    print(score5)

if score5 == "12":
    bn9.click()
    bn10.click()
    bn10.click()
    print(score5)

time.sleep(2)
score6 = random.choice(scores)
if score6 == "10":
    bn11.click()
    print(score5)
if score6 == "20":
    bn11.click()
    bn11.click()
    print(score5)
if score6 == "21":
    bn11.click()
    bn11.click()
    bn12.click()
    print(score5)
if score6 == "11":
    bn11.click()
    bn12.click()
    print(score5)
if score6 == "01":
    bn12.click()
    print(score5)
if score6 == "02":
    bn12.click()
    bn12.click()
    print(score5)
if score6 == "12":
    bn11.click()
    bn12.click()
    bn12.click()
    print(score5)

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[10]/button").click()
time.sleep(6)
# rem = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[1]')
# res = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/a/div[1]/span[2]')

print(sele, "-", score1, score2, score3, score4, score5, score6)

time.sleep(3)
driver.quit()

