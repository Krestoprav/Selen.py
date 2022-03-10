import win32com
from win32com import client
import openpyxl
from openpyxl import Workbook, load_workbook
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os
import win32api
import win32print
import pdfplumber


def zamena():
    path=str(rf'C:\Users\User\Desktop\Python\Zamena')
    n=0
    # Отрываем исходный файл для определения текста
    pdf = pdfplumber.open(rf'{path}\1.pdf')

    # Создаем экземпляр класса входного (чтение) и выходного файла (запись)
    input2 = PdfFileReader(open(rf"{path}\1.pdf", "rb"))
    output = PdfFileWriter()

    # Определяем и выводим количество страниц входного файла из почты России
    numPages = input2.getNumPages()
    print(rf"В документе {numPages} страниц")

    # Запускаем цикл обхода всех страниц и создания файлов
    for n in range(numPages):
        print(f'Обработка {n+1}-ой страницы')

        # Блок работы с текстом из первичного файла
        page = pdf.pages[n]  # читаем текущую страницу
        text = page.extract_text()  # Читаем текст со страницы
        sum_cif=text.split("руб.) ")[1].split(",00")[0]+' '  # Получаем сумму цифрами
        sum_slov=text.split("руб.) ")[1].split(' (')[1].replace(')', '')+' '  # Получаем сумму прописью

        # Список некорректных фраз
        bad=['рублей  ', 'рублей 0 ', 'рублей 00  ', 'рублей 00 к ', 'рублей 00 копе ', 'рублей 00 коп ',
             'рубле ', 'рублей 00 ко ']

        # Цикл замены некорректных фраз
        for word in bad:
            if sum_slov.find(word) != -1:
                sum_slov = sum_slov.replace(word, 'рублей 00 копеек ')
                break

        # Замена некорректных фраз. Выше цикл. удалить, если цикл сработает нормально
        # if sum_slov.find('рублей  ')!=-1:
        #     sum_slov= sum_slov.replace('рублей  ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 0 ')!=-1:
        #     sum_slov=sum_slov.replace('рублей 0 ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 00  ') != -1:
        #     sum_slov = sum_slov.replace('рублей 00  ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 00 к ') != -1:
        #     sum_slov = sum_slov.replace('рублей 00 к ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 00 копе ') != -1:
        #     sum_slov = sum_slov.replace('рублей 00 копе ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 00 коп ') != -1:
        #     sum_slov = sum_slov.replace('рублей 00 коп ', 'рублей 00 копеек ')
        # elif sum_slov.find('рубле ') != -1:
        #     sum_slov = sum_slov.replace('рубле ', 'рублей 00 копеек ')
        # elif sum_slov.find('рублей 00 ко ') != -1:
        #     sum_slov = sum_slov.replace('рублей 00 ко ', 'рублей 00 копеек ')

        # FIO=text.split('Отправитель От кого  ООО "БП" (')[1].split(', ЕСПП')[0]+' '
        FIO='Бочкарева Жанна Равилевна'  # ФИО отправителя
        t=str(f"{n + 1}) {sum_cif}{sum_slov}{FIO}")
        print(t)

        # Блок работы с шаблоном Ф112
        #  Открываем шаблон Ф112
        f112 = load_workbook(rf'{path}\Ф112ЭП-бланк.xlsx')
        print('Бланк открыт')
        sheet_f112 = f112.active

        # Вписываем ФИО
        sheet_f112['K20']= FIO

        # Вписываем цену
        sheet_f112['E5']= sum_cif

        # Вписываем цену прописью
        sheet_f112['AJ4']= sum_slov

        #  Сохраняем заполоненный бланк
        f112.save(rf'{path}\Ф112ЭП.xlsx')

        f112.close()
        print('Бланк закрыт')


        # Блок работы с конвертированием Ф112 в PDF
        # Open Microsoft Excel
        excel = client.Dispatch("Excel.Application")
        print("Win32 открыл эксель")
        # excel.Visible = False

        # Read Excel File
        sheets = excel.Workbooks.Open(rf'{path}\Ф112ЭП.xlsx')
        work_sheets = sheets.Worksheets[0]
        print("Win32 прочитал файл с бланком")

        # Convert into PDF File
        work_sheets.ExportAsFixedFormat(0, rf'{path}\Ф112ЭП{n}.pdf')
        print("Win32 сохранил бланк в PDF")

        # Закрыть эксель
        sheets.Close(True)

        # Блок работы по обрезанию файла и формированию выходного файла
        # Создаем экземпляр класса входного (чтение) и выходного файла (запись)
        input1 = PdfFileReader(open(rf"{path}\Ф112ЭП{n}.pdf", "rb"))

        page1=input1.getPage(0)  # Получаем страницу из Ф112

        # обрезаем n-ую страницу входного файла
        page2 = input2.getPage(n)
        # print(page2.cropBox.getLowerLeft())
        # print(page2.cropBox.getLowerRight())
        # print(page2.cropBox.getUpperLeft())
        # print(page2.cropBox.getUpperRight())

        # print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page2.trimBox.lowerLeft = (422, 0)
        page2.trimBox.upperRight = (841.889, 595.275)
        page2.cropBox.lowerLeft = (422, 0)
        page2.cropBox.upperRight = (841.889, 595.275)
        # page.rotateClockwise(90)

        output.addPage(page2)  # Добавляем в выходной файл адресный ярлык

        output.addPage(page1)  # Добавляем в выходной файл наложку



    with open(rf"{path}\out.pdf", "wb") as out_f:  # Сохраняем выходной файл
        output.write(out_f)

    # Закрываем исходный файл ранее открытый для чтения
    pdf.close()

    # Блок печати двух страниц на одном листе

    name = win32print.GetDefaultPrinter()

    #printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}
    printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}
    handle = win32print.OpenPrinter(name, printdefaults)

    level = 2
    attributes = win32print.GetPrinter(handle, level)

    print("Old Duplex = %d" % attributes['pDevMode'].Duplex)

    #attributes['pDevMode'].Duplex = 1    # no flip
    #attributes['pDevMode'].Duplex = 2    # flip up
    attributes['pDevMode'].Duplex = 3    # flip over

    ## 'SetPrinter' fails because of 'Access is denied.'
    ## But the attribute 'Duplex' is set correctly
    try:
        win32print.SetPrinter(handle, level, attributes, 0)
    except:
        print("win32print.SetPrinter: set 'Duplex'")

    res = win32api.ShellExecute(0, 'print', rf'C:\Users\User\Desktop\Python\Zamena\out.pdf', None, '.', 0)

    win32print.ClosePrinter(handle)

zamena()

