# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license. See LICENSE.txt in the project root for license information.
import requests
import uuid
import json

# graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'
graph_endpoint = 'https://graph.microsoft.com/beta{0}'
# graph_endpoint = 'https://outlook.office.com/api/v1.0{0}'
# graph_endpoint = 'https://outlook.office.com/api/beta{0}'

# Generic API Sending
def make_api_call(method, url, token, payload = None, parameters = None):
    # Send these headers with all API calls
    headers = { 'User-Agent' : 'python_tutorial/1.0',
                'Authorization' : 'Bearer {0}'.format(token),
                'Accept' : 'application/json' }
                
    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = { 'client-request-id' : request_id,
                        'return-client-request-id' : 'true' }
                        
    headers.update(instrumentation)
    
    response = None
    # import ipdb;ipdb.set_trace()
    if (method.upper() == 'GET'):
        response = requests.get(url, headers = headers, params = parameters)
    elif (method.upper() == 'DELETE'):
        response = requests.delete(url, headers = headers, params = parameters)
    elif (method.upper() == 'PATCH'):
        headers.update({ 'Content-Type' : 'application/json' })
        response = requests.patch(url, headers = headers, data = json.dumps(payload), params = parameters)
    elif (method.upper() == 'POST'):
        headers.update({ 'Content-Type' : 'application/json' })
        response = requests.post(url, headers = headers, data = json.dumps(payload), params = parameters)
        
    return response

def get_me(access_token):
  get_me_url = graph_endpoint.format('/me')

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields
  query_parameters = {'$select': 'displayName,mail'}

  r = make_api_call('GET', get_me_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def get_my_messages(access_token):
  get_messages_url = graph_endpoint.format('/me/mailfolders/inbox/messages')
  
  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the ReceivedDateTime, Subject, and From fields
  #  - Sort the results by the ReceivedDateTime field in descending order
  query_parameters = {'$top': '10',
                      '$select': 'receivedDateTime,subject,from',
                      '$orderby': 'receivedDateTime DESC'}
                      
  r = make_api_call('GET', get_messages_url, access_token, parameters = query_parameters)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)
    
def get_my_events(access_token):
  get_events_url = graph_endpoint.format('/me/events')
  
  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the Subject, Start, and End fields
  #  - Sort the results by the Start field in ascending order
  query_parameters = {'$top': '10',
                      '$select': 'subject,start,end',
                      # '$orderby': 'start/dateTime ASC'
                     }
                      
  r = make_api_call('GET', get_events_url, access_token, parameters = query_parameters)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)
    
def get_my_contacts(access_token):
  get_contacts_url = graph_endpoint.format('/me/contacts')
  
  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the GivenName, Surname, and EmailAddresses fields
  #  - Sort the results by the GivenName field in ascending order
  query_parameters = {'$top': '10',
                      '$select': 'givenName,surname,emailAddresses',
                      '$orderby': 'givenName ASC'}
                        
  r = make_api_call('GET', get_contacts_url, access_token, parameters = query_parameters)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def get_my_rooms(access_token):
  get_contacts_url = graph_endpoint.format('/me/findrooms')
  
  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the GivenName, Surname, and EmailAddresses fields
  #  - Sort the results by the GivenName field in ascending order
  query_parameters = {'$top': '10',
                      '$select': 'givenName,surname,emailAddresses',
                      '$orderby': 'givenName ASC'}
  r = make_api_call('GET', get_contacts_url, access_token)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def post_find_meetings(access_token):
  post_meetings_url = graph_endpoint.format('/me/findmeetingtimes')

def post_my_events(access_token):
  get_events_url = graph_endpoint.format('/me/events')

  query_parameters = {
                    "Subject": "Plan summer company picnic",
                    "Body": {
                      "ContentType": "HTML",
                      "Content": "Let's kick-start this event planning!"
                    },
                    "Start": {
                        "DateTime": "2018-10-22T11:00:00",
                        "TimeZone": "India Standard Time"
                    },
                    "End": {
                        "DateTime": "2018-10-22T12:00:00",
                        "TimeZone": "India Standard Time"
                    },
                    "Attendees": [
                      {
                        "EmailAddress": {
                          "Address": "sujith.suthan@marlabs.com",
                          "Name": "Shalice Moideen"
                        },
                        "Type": "Required"
                      }
                    ],
                    "Location": {
                      "DisplayName": "KochiConf1",
                      "LocationType": "Default"
                    },
                  }
  r = make_api_call('POST', get_events_url, access_token, payload =query_parameters)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def post_send_message(access_token):
  get_message_url = graph_endpoint.format('/me/sendmail')

  query_parameters = {
                      "Message": {
                        "Subject": "Meet for lunch?",
                        "Body": {
                          "ContentType": "Text",
                          "Content": "The new cafeteria is open."
                        },
                        "ToRecipients": [
                          {
                            "EmailAddress": {
                              "Address": "roshin.raj@marlabs.com"
                            }
                          }
                        ],
                      },
                      "SaveToSentItems": "false"
                    }
  r = make_api_call('POST', get_message_url, access_token, payload =query_parameters)
  
  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)
