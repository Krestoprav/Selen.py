#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
import urllib.parse
import urllib.request


data = {}
data['type_blank'] = 'F112'
data['from_name'] = 'Ивана Ивановича'
data['from_city'] = 'г. Москва'
data['from_street'] = 'ул. Стахановская'
data['from_build'] = '999'
data['from_appartment'] = '99'
data['from_zip'] = '109428'
data['whom_surname'] = 'Петрову'
data['whom_name'] = 'Петру Петровичу'
data['whom_city'] = 'г. Санкт-Петербург'
data['whom_street'] = 'ул. Гоголя'
data['whom_build'] = '888'
data['whom_appartment'] = '88'
data['whom_zip'] = '190000'
data['declared_value'] = '1000.00'
data['COD_amount'] = '1100.00'

params = {'access_token': 'ebe815eb3932dba8369c8ce32602516b',
          'data': json.dumps(data)}
#params['access_token'] = 'ebe815eb3932dba8369c8ce32602516b'
#params['data'] = json.dumps(data)

params = urllib.parse.urlencode(params)
f = urllib.request.urlopen("http://pbrf.ru/pdf.F7", {'access_token': 'ebe815eb3932dba8369c8ce32602516b', 'data': json.dumps(data)})
print(f.read())
