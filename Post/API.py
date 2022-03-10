import pochta
from pochta import SingleTracker, BatchTracker, tracking
from zeep import CachingClient, Settings

# Трекинг через API почты России

tracking = SingleTracker('YhdmWXIsTUCtVT', '19IvLEmsRkN5')  # Треккинг Володя
# tracking = SingleTracker('HRixxqSeEHLqWu', 'nH5sLTOCmpnn')  # Треккинг Олег

track=str(80102367216110)

# history = tracking.get_history(track)

viplata = tracking.get_order_events_for_mail(track)


# Печать результата из почты России


print(viplata)

if str(viplata)!='None':
    print((viplata[-1]['EventName'])+' '+str(viplata[-1]['EventDateTime'])+' '+str(viplata[-1]['IndexTo']))
else:
    print('Нет данный на сервере')




# class Tracking:
#     """
#     API клиент сервиса отслеживания посылок.
#
#     https://tracking.pochta.ru/specification
#     """
#
#     def __init__(self, login: 'HRixxqSeEHLqWu', password: 'nH5sLTOCmpnn'):
#         """
#         Инициализация API клиента сервиса отслеживания посылок.
#
#         :param login: Логин от системы трекинга
#         :param password: Пароль от системы трекинга
#         """
#         self._login = login
#         self._password = password
#
#         self._client = CachingClient(
#             'https://tracking.russianpost.ru/rtm34?wsdl',
#             settings=Settings(strict=False),
#         )
#
#     def get_history(self, barcode: '14102059104821') -> dict:
#         """
#         История операций над отправлением.
#
#         Метод getOperationHistory используется для получения информации о
#         конкретном отправлении. Метод возвращает подробную информацию
#         по всем операциям, совершенным над отправлением.
#
#         https://tracking.pochta.ru/specification#getOperationHistory
#
#         :param barcode: Идентификатор регистрируемого почтового отправления
#             в одном из форматов:
#             - внутрироссийский, состоящий из 14 символов (цифровой)
#             - международный, состоящий из 13 символов (буквенно-цифровой) в формате S10.
#
#         :return: Ответ метода getOperationHistory содержит список элементов
#             historyRecord. Каждый из них содержит информацию об одной операции над
#             отправлением. Если над отправлением еще не зарегистрировано ни одной
#             операции, то возвращается пустой список элементов historyRecord.
#         """
#         return self._client.service.getOperationHistory(
#             OperationHistoryRequest={
#                 'Barcode': barcode,
#                 'MessageType': '0'
#             },
#             AuthorizationHeader={
#                 'login': self._login,
#                 'password': self._password,
#             },
#         )
#
#
#     def get_order_events_for_mail(self, barcode: '14102059104821') -> dict:
#         """
#         История операций с наложенным платежом.
#
#         Метод PostalOrderEventsForMail позволяет получить информацию об операциях с
#         наложенным платежом, который связан с конкретным почтовым отправлением.
#
#         https://tracking.pochta.ru/specification#PostalOrderEventsForMail
#
#         :param barcode: Идентификатор регистрируемого почтового отправления
#             в одном из форматов:
#             - внутрироссийский, состоящий из 14 символов (цифровой);
#             - международный, состоящий из 13 символов (буквенно-цифровой) в формате S10.
#         :return: Список событий
#         """
#         return self._client.service.PostalOrderEventsForMail(
#             PostalOrderEventsForMailInput={
#                 'Barcode': barcode,
#             },
#             AuthorizationHeader={
#                 'login': self._login,
#                 'password': self._password,
#             },
#         )
#
#
#     # TODO: Пакетный доступ
#
#
#     def get_ticket(self, bar_codes: ['14102059171960', '14391358833161']) -> dict:
#         return self._client.service.ti(
#             PostalOrderEventsForMailInput={
#                 'bar_codes': bar_codes,
#             },
#             AuthorizationHeader={
#                 'login': self._login,
#                 'password': self._password,
#             },
#         )
#
#     def get_history_for_ticket(self, ticket: str) -> dict:
#         pass
#
#
# if __name__=="__main__":
#     pass
