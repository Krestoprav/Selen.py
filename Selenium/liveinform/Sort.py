import os
import re
import shutil
import sys
import time
from time import sleep

folder=r'C:\Users\User\Downloads'
folder_excel=r'C:\Users\User\Downloads\EXCEL'
folder1=r'C:\Users\User\Downloads\1'
folder2=r'C:\Users\User\Downloads\2'
folder3=r'C:\Users\User\Downloads\3'

try:
    os.makedirs(folder_excel)
except OSError:
    print("Создать директорию %s не удалось" % folder_excel)
else:
    print("Успешно создана директория %s " % folder_excel)
finally:


    #Получаем списки файлов в папках

    a=os.listdir(path=folder)
    b=os.listdir(path=folder_excel)
    c1=os.listdir(path=folder1)
    c2=os.listdir(path=folder2)
    c3=os.listdir(path=folder3)

    w = [c1, c2, c3, b]
    total_size = [0, 0, 0]
    papki = [folder1, folder2, folder3, folder_excel]

    # очищаем папки 1,2,3

    for n in range(len(w)):
        try:
            for i in range(len(w[n])):
                os.remove(papki[n] + "/" + w[n][i])
        except Exception:
            continue
    print("Папки зачищены")


    # Вырезаем все нужные файлы в соответствующую папку

    for i in range(len(a)):
        x=a[i].split(".")
        if x[-1]=='xls':
            file=folder+"/"+a[i]
            new_path = folder_excel + "/" + a[i]
            os.rename(file, new_path)


    b = os.listdir(path=folder_excel)

    while True and len(b)>0:

        for n in range(1, 4):

            razmeri_v_excel = []

        #  Получаем список с размерами файлов:

            for i in range(len(b)):
                file_size = os.path.getsize(folder_excel + "/" + b[i])
                razmeri_v_excel+=[file_size/1024**2]
                # print(b[i] + ' - ' + str(razmeri_v_excel[i]))  # выводит название файла и его размер
            # print(razmeri_v_excel)  # выводит список к размерами
            print(str(len(razmeri_v_excel)) + " - " + str(len(b)))  # выводит длину списка с размерам и списка с файлами
            try:
                index=razmeri_v_excel.index(max(razmeri_v_excel))  # определяем индекс файла с макс размером
            except ValueError:
                break
            else:

                # Отправляем файл с макс размером в папки 1,2,3 попеременно попеременно

                b = os.listdir(path=folder_excel)
                file = folder_excel + "/" + b[index]
                new_path = folder + "/" +str(n) + "/" + b[index]
                os.rename(file, new_path)
                b = os.listdir(path=folder_excel)
                print((len(b)))

















    # for i in range(1, 4):
    #     b = os.listdir(path=folder_excel)
    #     file = folder_excel + "/" + b[1]
    #     new_path = folder + "/" +str(i) + "/" + b[1]
    #     os.rename(file, new_path)
    #     b = os.listdir(path=folder_excel)

    #
    # for n in range(len(w)):
    #
    #     print(len(w[n]))
    #     for i in range(len(w[n])):
    #         file_size = os.path.getsize(papki[n] + "/" + w[n][i])
    #         print(w[n][i]+' - '+str(file_size/1024**2))
    #         total_size[n]+=file_size
    #     print(total_size[n]/1024**2)
















