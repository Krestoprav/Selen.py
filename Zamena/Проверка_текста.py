import pdfplumber


pdf = pdfplumber.open(rf'C:\Users\User\Desktop\Python\Замена\1.pdf')

for n in range(180, 183):
    page = pdf.pages[n]
    text = page.extract_text()
    sum_cif=text.split("руб.) ")[1].split(",00")[0]+' '
    sum_slov=text.split("руб.) ")[1].split(' (')[1].replace(')', '')+' '

    if sum_slov.find('рублей  ')!=-1:
        sum_slov= sum_slov.replace('рублей  ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 0 ')!=-1:
        sum_slov=sum_slov.replace('рублей 0 ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 00  ') != -1:
        sum_slov = sum_slov.replace('рублей 00  ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 00 к ') != -1:
        sum_slov = sum_slov.replace('рублей 00 к ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 00 копе ') != -1:
        sum_slov = sum_slov.replace('рублей 00 копе ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 00 коп ') != -1:
        sum_slov = sum_slov.replace('рублей 00 коп ', 'рублей 00 копеек ')
    elif sum_slov.find('рубле ') != -1:
        sum_slov = sum_slov.replace('рубле ', 'рублей 00 копеек ')
    elif sum_slov.find('рублей 00 ко ') != -1:
        sum_slov = sum_slov.replace('рублей 00 ко ', 'рублей 00 копеек ')

    # FIO=text.split('Отправитель От кого  ООО "БП" (')[1].split(', ЕСПП')[0]+' '
    FIO='Бочкарева Жанна Равилевна'

    t=str(f"{n + 1}) {sum_cif}{sum_slov}{FIO}")
    print(t)

pdf.close()









# from tika import parser
#
# rawText = parser.from_file(rf'C:\Users\User\Desktop\Python\Замена\Ф112ЭП0.pdf')
#
# rawList = rawText['content'].splitlines()

















# import sys
# import pdfminer.high_level
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# import os
#
#
#
# # with open(rf'C:\Users\User\Desktop\Python\Замена\out.pdf', 'rb') as file:
# #     text = str(pdfminer.high_level.extract_text_to_fp(file, outfp=sys.stdout, page_numbers=0))
# #
# #     print('\n')
# #     print(text[0])
#
# output = StringIO
# manager = PDFResourceManager()
# converter = TextConverter(manager, output, laparams=LAParams())
# interpreter = PDFPageInterpreter(manager, converter)
#
# filepath = open(fname, 'rb')
# for page in PDFPage.get_pages(rf'C:\Users\User\Desktop\Python\Замена\out.pdf', pagenums):
#     interpreter.process_page(page)
# filepath.close()
# converter.close()
# text = output.getvalue()
# output.close
# print(text)


