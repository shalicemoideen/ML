from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	import ipdb;ipdb.set_trace()
	return HttpResponse("Hello, world. You're at the core index.")

def create_meetings(request):
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
  from selenium.webdriver.common.alert import Alert
  from selenium.webdriver.support.ui import WebDriverWait as wait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.firefox.options import Options
  from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
  

  # driver = webdriver.Remote(
  #           command_executor='http://192.168.65.50:4444/wd/hub',
  #           desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
  #           )
  driver = webdriver.Firefox()
  driver.implicitly_wait(20)
  driver.maximize_window()
  # driver.get('https://rapid360.marlabs.com/outlook/tutorial/')
  driver.get('http://localhost:8888/tutorial/')
  driver.find_element_by_xpath("//*[@id='connect-button']").click()
  driver.find_element_by_xpath("//*[@id='i0116']").send_keys("roshin.raj@marlabs.com")
  driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
  # import ipdb;ipdb.set_trace()

  ###### To run in local when alert is not present ######
  try:
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UsernameTextBox']").send_keys("roshin.raj@marlabs.com")
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_PasswordTextBox']").send_keys("Roshi@123")
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_SubmitButton']").click()
  except NoSuchElementException:
    print("No username and password field")
  # End here 


  ###### To run in server for alert popup  ######

  # wait(driver, 20).until(EC.alert_is_present())
  # alert = driver.switch_to_alert()
  # alert.send_keys('roshin.raj@marlabs.com' + Keys.TAB + 'Roshi@123')
  # alert.accept()

  # Alert end here

  
  time.sleep(1)
  try:
    driver.find_element_by_xpath("//*[@id='KmsiDescription']").click()
    driver.find_element_by_xpath("//*[@id='idBtn_Back']").click()
    print("Save button found")
  except NoSuchElementException:
    print("No save button  found")

  
  time.sleep(1)
  try:
    driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
    print("accept button found")
  except NoSuchElementException:
      print("No accept button")

  driver.quit()

def getrooms(request):
	import ipdb;ipdb.set_trace()
	return HttpResponse("Hello, world. You're at the core rooms.")


