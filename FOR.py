import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


# Создаем экземпляр класса входного (чтение) и выходного файла (запись)
with open("Замена/1.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    # Определяем и выводим количество страниц входного фала из почты России
    numPages = input1.getNumPages()
    print(rf"В документе {numPages} страниц")

    # Запускаем цикл для обрезания страниц входного файла
    for i in range(numPages):
        print(i)
        page = input1.getPage(i)
        print(page.cropBox.getLowerLeft())
        print(page.cropBox.getLowerRight())
        print(page.cropBox.getUpperLeft())
        print(page.cropBox.getUpperRight())

        # print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft = (422, 0)
        page.trimBox.upperRight = (841.889, 595.275)
        page.cropBox.lowerLeft = (422, 0)
        page.cropBox.upperRight = (841.889, 595.275)
        # page.rotateClockwise(90)
        output.addPage(page)


    # Сохраняем выходной файл
    with open("out.pdf", "wb") as out_f:
        output.write(out_f)

# # Создаем экземпляр класса для объединения выходного файла и файла с наложками
# merger = PdfFileMerger()
#
# path = open('out.pdf', 'rb')  # Открываем выходной файл
# path2 = open('out — копия.pdf', 'rb')  # Открываем файла с наложками
#
# merger.merge(position=0, fileobj=path2)  # Вставляем страницу из файла
# merger.merge(position=1, fileobj=path)
# merger.write(open("test_out.pdf", 'wb'))










# page1=reader.getPage(0)
#
# text=page1.extractText()
#
# print(text.encode('utf-8').decode('utf-8'))

# with pdfplumber.PDF(file) as pdf:
#   pages = [page.extract_text() for page in pdf.pages]
# text = '\n'.join(pages)
#
# # print(text)
# print(text[20])

