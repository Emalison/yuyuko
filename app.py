import os
import socket
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def  load_driver():
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

def  start():
	driver = load_driver()
	driver.get("https://www.youtube.com/watch?v=sfhWNBCIcM0")
	time.sleep(100)
	print(driver.title)
	hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
	print(local_ip)
	driver.close()

if  __name__ == "__main__":
	start()
