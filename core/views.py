from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from core.authhelper import get_signin_url, get_token_from_code, get_access_token
from core.outlookservice import get_me, get_my_messages, get_my_events, get_my_contacts, get_my_rooms, post_my_events, post_send_message
import time
import json

action = None

def index(request):
	import ipdb;ipdb.set_trace()
	return HttpResponse("Hello, world. You're at the core index.")

def login(request):
  # redirect_uri = request.build_absolute_uri(reverse('ML:gettoken'))
  redirect_uri = settings.BASE_URL
  sign_in_url = get_signin_url(redirect_uri)
  context = { 'signin_url': sign_in_url }
  return render(request, 'core/home.html', context)

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
  selenium_login()


def selenium_login():

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
  driver.get('http://localhost:8888/login/')
  driver.find_element_by_xpath("//*[@id='connect-button']").click()
  driver.find_element_by_xpath("//*[@id='i0116']").send_keys("roshin.raj@marlabs.com")
  driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
  # import ipdb;ipdb.set_trace()

  ###### To run in local when alert is not present ######
  # try:
  #   driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_UsernameTextBox']").send_keys("roshin.raj@marlabs.com")
  #   driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_PasswordTextBox']").send_keys("Roshi@123")
  #   driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_SubmitButton']").click()
  # except NoSuchElementException:
  #   print("No username and password field")
  # End here 


  ###### To run in server for alert popup  ######

  wait(driver, 20).until(EC.alert_is_present())
  alert = driver.switch_to_alert()
  alert.send_keys('roshin.raj@marlabs.com' + Keys.TAB + 'Roshi@123')
  alert.accept()

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
  pass


def gettoken(request):

  # auth_code = request.GET['code']
  # print(auth_code,"code")
  # redirect_uri = settings.BASE_URL
  # token = get_token_from_code(auth_code, redirect_uri)
  # access_token = token['access_token']
  # print(access_token,"access_token")

  # events = get_my_rooms(access_token)
  from django.http import JsonResponse
  # import ipdb;ipdb.set_trace()
  # resp = {}
  # resp['type'] = "message"
  # resp['attachmentLayout'] = "list"
  # resp['text'] = ""

  # content = list()
  # resp['attachments'] = [
  #               {
  #                 "contentType": "application/vnd.microsoft.card.hero",
  #                 "content": {
  #                   "text": "What kind of sandwich would you like on your sandwich? ",
  #                   "buttons": [
  #                     {
  #                       "type": "imBack",
  #                       "title": "BLT",
  #                       "value": "1"
  #                     },
  #                     {
  #                       "type": "imBack",
  #                       "title": "Black Forest Ham",
  #                       "value": "2"
  #                     },
  #                     {
  #                       "type": "imBack",
  #                       "title": "Buffalo Chicken",
  #                       "value": "3"
  #                     }
  #                   ]
  #                 }
  #               }
  #             ]

  resp = {
          "type": "message",
          "text": "Welcome to <b>Botland</b>. Please visit <a href=\"https://blogs.msdn.microsoft.com/tsmatsuz\">my blog</a>."
        }
  botresponse = "Welcome to <b>Botland</b>. Please visit <a href=\"https://blogs.msdn.microsoft.com/tsmatsuz\">my blog</a>."
  bot_response = {
              "type": "message",
              "attachmentLayout": "list",
              "text": "",
              "attachments": [
                {
                  "contentType": "application/vnd.microsoft.card.hero",
                  "content": {
                    "text": "What kind of sandwich would you like on your sandwich? ",
                    "buttons": [
                      {
                        "type": "imBack",
                        "title": "BLT",
                        "value": "1"
                      },
                      {
                        "type": "imBack",
                        "title": "Black Forest Ham",
                        "value": "2"
                      },
                      {
                        "type": "imBack",
                        "title": "Buffalo Chicken",
                        "value": "3"
                      }
                    ]
                  }
                }
              ]
            }





  message = {
              "items": [
                {
                  "description": "Item One Description",
                  "image": {
                    "url": "http://imageOneUrl.com",
                    "accessibilityText": "Image description for screen readers"
                  },
                  "optionInfo": {
                    "key": "itemOne",
                    "synonyms": [
                      "thing one",
                      "object one"
                    ]
                  },
                  "title": "Item One"
                },
                {
                  "description": "Item Two Description",
                  "image": {
                    "url": "http://imageTwoUrl.com",
                    "accessibilityText": "Image description for screen readers"
                  },
                  "optionInfo": {
                    "key": "itemTwo",
                    "synonyms": [
                      "thing two",
                      "object two"
                    ]
                  },
                  "title": "Item Two"
                }
              ],
              "platform": "google",
              "title": "Title",
              "type": "list_card"
            }
                  

  simple = {
    "speech": "Welcome to <b>Botland</b>. Please visit <a href=\"https://blogs.msdn.microsoft.com/tsmatsuz\">my blog</a>.Text response<input type='button' value='Yes'/>",
    "type": 0
  }

  lst = [{
        "messages": {
          "type": 1,
          "title": "card title",
          "subtitle": "card text",
          "imageUrl": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png"
        }}]


  bot_res = [{"type":2, 
              "platform":"skype","title":"","replies":["book a meeting","nothing","test"]},
              {"type":0,"speech":"Ok can you please tell me the location"}]


  data = {
            "data": {
              "google": {
                "expectUserResponse": "true",
                "richResponse": {
                  "items": [
                    {
                      "simpleResponse": {
                        "textToSpeech": "this is a simple response"
                      }
                    }
                  ]
                }
              }
            }
          }


#           {
#   "payload": {
#     "google": {
#       "expectUserResponse": true,
#       "richResponse": {
#         "items": [
#           {
#             "simpleResponse": {
#               "textToSpeech": "this is a simple response"
#             }
#           }
#         ]
#       }
#     }
#   }
# }






# "[{\"type\":2,\"platform\":\"skype\",\"title\":\"\",\"replies\":[\"book a meeting\",\"nothing\",\"test\"]},{\"type\":0,\"speech\":\"Ok can you please tell me the location\"}]"

  fullfillment = {"speech":bot_response,"displayText":bot_response}
  speech = {"speech":json.dumps(bot_response)}
  fullfillment = json.dumps(fullfillment)
  return HttpResponse(json.dumps(simple), content_type="application/json")
  
  # result = json.dumps(resp)
  # return JsonResponse(resp)


  # response = {
  #             "type": "message",
  #             "attachmentLayout": "list",
  #             "text": "",
  #             "attachments": [
  #               {
  #                 "contentType": "application/vnd.microsoft.card.hero",
  #                 "content": {
  #                   "text": "What kind of sandwich would you like on your sandwich? ",
  #                   "buttons": [
  #                     {
  #                       "type": "imBack",
  #                       "title": "BLT",
  #                       "value": "1"
  #                     },
  #                     {
  #                       "type": "imBack",
  #                       "title": "Black Forest Ham",
  #                       "value": "2"
  #                     },
  #                     {
  #                       "type": "imBack",
  #                       "title": "Buffalo Chicken",
  #                       "value": "3"
  #                     }
  #                   ]
  #                 }
  #               }
  #             ]
  #           }

  # events = post_my_events(access_token)
  # events = post_send_message(access_token)
  # return HttpResponse("Hello, world. You're at the token index.")
  # context = { 'contacts': events['value'] }
  # return render(request, 'tutorial/contacts.html', context)