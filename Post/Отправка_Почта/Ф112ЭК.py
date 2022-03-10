# -*- coding: utf-8 -*-
# примеры работы с api v1.0 для pyton 3
# необходим установленный модуль "requests"
# документация модуля: https://requests.readthedocs.io
# инструкции по установке модуля: https://requests.readthedocs.io/en/master/user/install

import requests
import base64

def to_base64(str):
	return base64.b64encode(str.encode()).decode("utf-8")

#properties
protocol	= "https://"
access_token	= "zpRNYASJazFUNLCXD8gO1t5f4UM08OEn"
login_password	= to_base64("login:password")
protocol	= "https://"
host		= "otpravka-api.pochta.ru"
id		= "23437816"

#опционально
sending_date    = ""

request_headers = {
	"Content-Type": "application/json",
	"Accept": "application/json;charset=UTF-8",
	"Authorization": "AccessToken " + access_token,
	"X-User-Authorization": "Basic " + login_password
}

path = "/1.0/forms/" + id + "/f112pdf"
url_args = "?sending-date=" + sending_date
url = protocol + host + path + url_args

filename = 'f112_shipment_' + id + '.pdf'
response = requests.get(url, headers=request_headers, stream=True)

print("Status code: ", response.status_code)
if response.status_code == 200:
	with open(filename, 'wb') as handle:
		for block in response.iter_content(1024):
			handle.write(block)
		print("File: ", filename)


