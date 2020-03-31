#! python3
import webbrowser, time, shelve, os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# ------------INIT-----------------
data = shelve.open('.\\name')
data.setdefault('name', 'name')
if data['name'] == 'name':
    print('Type your name here: ', end='')
    data['name'] = input()
yourname = data['name']
data.close()
timeout = 30
additionalwaittime = 0
# ------------1st page-------------
browser = webdriver.Chrome()
browser.get('https://forms.gle/uVLrPGJM3HPnzZYbA')
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div/div/div[2]/div/div/div[2]/div/span/div/div[3]/label'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
Class = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div/div/div[2]/div/span/div/div[3]/label')
Class.click()
Next = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div[1]/div/span')
Next.click()
# ------------2nd page-------------
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div/div/div[3]/div[1]/div[1]/div[2]/span'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
Name = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
Name.send_keys(yourname)
time.sleep(additionalwaittime)
Next = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div[1]/div[2]/span')
Next.click()
# ------------3rd page-------------
time.sleep(additionalwaittime)
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div/div/div[2]/div[17]/div/div[2]/div/span/div/div[1]/label'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("1Timed out waiting for page to load")
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div[1]/div/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div[2]/div/label/div/div[2]/div/span')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div[3]/div/label/div/div[2]/div/span')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[11]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[12]/div/div[2]/div[4]/div/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[13]/div/div[2]/div[4]/div/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[14]/div/div[2]/div/span/div/div[2]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[15]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[16]/div/div[2]/div/span/div/div[1]/label')
a.click()
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[17]/div/div[2]/div/span/div/div[1]/label')
a.click()
Next = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div[1]/div[2]/span')
Next.click()
# ------------4th page-------------
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/div/label'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
a = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/div/label')
a.click()
Next = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div[1]/div[2]/span')
Next.click()
#browser.quit()
