import yaml
import time
import urllib3
from selenium import webdriver

# establish chromium options for driver module
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('headless')
driver = webdriver.Chrome(options=chromeOptions)


# main function which logs into bamboo hr and clicks clock in/out
def main():
    #grab companydomain, user, pass from config.yml. This file is added to gitignore to avoid sharing unique creds
    with open("config.yml",'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)

    #sets bamboo_ vars to specific config.yml values
    bamboo_url = 'https://' + cfg['companydomain'] + '.bamboohr.com/login.php?r=%2Fhome%2F'
    bamboo_user = cfg['user']
    bamboo_pass = cfg['pass']


    urllib3.disable_warnings()

    driver.get(bamboo_url)

    login_process = driver.find_element_by_id('lemail')
    login_process.send_keys(bamboo_user)
    login_process = driver.find_element_by_name('password')
    login_process.send_keys(bamboo_pass)
    time.sleep(1)
    login_process.submit()

    clock_in_out = driver.find_element_by_xpath('//button[@class="fab-Button fab-Button--biggie fab-Button--width100"]')
    clock_in_out.click()


main()
