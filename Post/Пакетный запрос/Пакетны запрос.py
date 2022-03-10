from time import sleep
from suds.client import Client

url = 'https://tracking.russianpost.ru/fc?wsdl'
client = Client(url)

barcodesFile = open("barcodes.txt") #файл с баркодами
my_login = 'HRixxqSeEHLqWu'  # логин
my_password = 'nH5sLTOCmpnn'  # пароль
barcodes =[]
print('1')
for line in barcodesFile:
    item = client.factory.create('item')
    item._Barcode = line
    barcodes.append(item)
print('2')
file = client.factory.create('file')
file.Item = barcodes
print('3')

result = client.service.getTicket(file, my_login, my_password, 'RUS')
print(result)

sleep(900) #задержка 15 мин для создания ответа
print('5')
result2 = client.service.getResponseByTicket(result.value, my_login, my_password)
print(result2) # вывод всей информации
print('6')

for val in result2.value.Item:
    print(val._Barcode)
    for oper in val.Operation:
        print(oper._DateOper +', '+ oper._OperName)  #  вывод даты и описания операции

print('7')
