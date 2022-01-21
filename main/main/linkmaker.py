import requests
from requests import Response
# from project.app.views import main
data = {
  'client_id': "client_id",
  'client_secret': "client_secret",
  'grant_type': "authorization_code",
  'code': "code",
  'redirect_uri': "http://*******.ngrok.io"
}
# менять ссылки в linkmaker, settings и в самой интеграции
session = requests.Session()
authorization_url = 'https://www.amocrm.ru/oauth?'
link = authorization_url + 'client_id=' + data['client_id'] + '&state=' + 'response.status_code'
response: Response = session.post(link, data=data)
print(link)
headers = {
  "token_type": "Bearer",
  "expires_in": 86400,
  "access_token": "",
  "refresh_token": ""
}

# create link get response for search a contact with using phone
# get_link = "https://login.amocrm.ru/api/v4/contacts?query=" + main.contact['phone']
# get_response = session.get(get_link)
