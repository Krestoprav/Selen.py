import os
import pandas as pd
import glob
import shutil
import pyexcel as p
import openpyxl
import xlrd
import comtypes.client as cl
import xlsxwriter



def Obidinenie_excell():

    papki=[r'C:\Users\User\Downloads\1', r'C:\Users\User\Downloads\2', r'C:\Users\User\Downloads\3']

    for papka in papki:
        combined = pd.DataFrame()
        print(papka)
        files = [item for item in glob.glob(papka+str('\*{}').format('.xlsx'))]
        print(files)
        print(len(files))

        for file in files:

            file = pd.read_excel(file)
            combined = pd.concat([combined, file])

        combined.to_excel(papka+'\Сумм.xlsx')





Obidinenie_excell()