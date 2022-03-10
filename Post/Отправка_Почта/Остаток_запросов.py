# -*- coding: utf-8 -*-
# примеры работы с api v1.0 для pyton 3
# необходим установленный модуль "requests"
# документация модуля: https://requests.readthedocs.io
# инструкции по установке модуля: https://requests.readthedocs.io/en/master/user/install

import requests
import json

#properties
protocol = "https://"
host = "otpravka-api.pochta.ru"
token = "zpRNYASJazFUNLCXD8gO1t5f4UM08OEn"
key = "b3MucHJldGVueml5QHlhbmRleC5ydTptb2lzZWV2YTIxMTE="

request_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json;charset=UTF-8",
    "Authorization": "AccessToken " + token,
    "X-User-Authorization": "Basic " + key
}

path = "/1.0/settings/limit"

url = protocol + host + path

response = requests.get(url, headers=request_headers)
print("Status code: ", response.status_code)
print("Response body: ", response.json())
a=response.json()['allowed-count']-response.json()['current-count']
print(rf'Остаток {a} запросов')



