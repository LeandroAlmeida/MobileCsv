# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import xlsxwriter
#import pickle
#from github import Github
import csv
#import json 
#from unicodedata import normalize
#from operator import itemgetter
#import time
#import datetime
from os import system
dicUsersFirst={}
dicUsersSecond={}


def readCsvToDic(data, time):
    dicUsers={}
    Id=0
    global dicUsersFirst, dicUsersSecond
    for rows in data: 
        dicUsers[Id]={}
        if Id>0:
            cont=0
            for cell in rows:
                dicUsers[Id][dicUsers[0][cont]]=cell
                cont+=1
            Id+=1
        else:#primeira linha - num das questões - converte num em id da questão
            cont=0
            for cell in rows:
                dicUsers[Id][cont]=cell
                cont+=1
            Id+=1
    if time=="First":
        dicUsersFirst=dicUsers
    else:
        dicUsersSecond=dicUsers

        
def expUsersCsv(sample, listIds):
    if sample=="First":
        dicFinalUsers=dicUsersFirst
    else:
        dicFinalUsers=dicUsersSecond
    
#    Fieldnames=["Login","Email"]
#    firstLine={"Login":"Login(Caso tenha sido informado)", "Email":"Email"}
#    fileResul=open(sample+".csv","wb")
#    csvWriter=csv.DictWriter(fileResul,delimiter='|',fieldnames=Fieldnames)
#    #csvWriter.writerow({"Login":"Login(Caso tenha sido informado)", "Email":"Email"})
#  
#    for Id in listIds:
#        row={"Login":dicFinalUsers[Id]["1."], "Email":dicFinalUsers[Id]["17."]}
#        csvWriter.writerow(row)      
#            
#    fileResul.close()  

    workbook = xlsxwriter.Workbook(sample+"_Sample.xlsx")
    worksheet = workbook.add_worksheet()
    
    worksheet.write(0,0, "Login(Caso tenha sido informado no survey)")
    worksheet.write(0,1, "Email")
    row = 1
    col = 0
    for Id in listIds:
        worksheet.write(row, col, dicFinalUsers[Id]["1."])
        worksheet.write(row, col+1, dicFinalUsers[Id]["17."])
        row += 1
    
    workbook.close()
      
        
try:
    data = csv.reader(open('Fist_Mobile_Survey_GitHub.csv', 'r'),delimiter='|') 
    data2= csv.reader(open('Second_Mobile_Survey_GitHub.csv', 'r'),delimiter='|')
except IOError as e:
    print ("Erro ao ler os arquivos, corrija o erro e execute novamente. Erro: ", e)
    system.exit(0)
    
print ("Ok")
readCsvToDic(data, "First")
readCsvToDic(data2, "Second")
listUserWithEmailFirst=[]
for Id in dicUsersFirst.keys():
    if Id == 0:
        continue
    else:
        if (dicUsersFirst[Id]["8.Social_Aspects"]=="Very influential") or (dicUsersFirst[Id]["11.Social_Aspects"]=="Very influential"):
            if (dicUsersFirst[Id]["16."]=="Yes, please!") or (dicUsersFirst[Id]["15."]=="Yes, I'd be up for it!"):
                listUserWithEmailFirst.append(Id)
        
print (len(listUserWithEmailFirst))

listUserWithEmailSecond=[]
for Id in dicUsersSecond.keys():
    if Id == 0:
        continue
    else:
        if (dicUsersSecond[Id]["8.Social_Aspects"]=="Very influential") or (dicUsersSecond[Id]["8.Social_Aspects"]=="Influential") or (dicUsersSecond[Id]["11.Social_Aspects"]=="Very influential") or (dicUsersSecond[Id]["11.Social_Aspects"]=="Influential"):
            if (dicUsersSecond[Id]["16."]=="Yes, please!") or (dicUsersSecond[Id]["15."]=="Yes, I'd be up for it!"):
                listUserWithEmailSecond.append(Id)
        
print (len(listUserWithEmailSecond))

expUsersCsv("First", listUserWithEmailFirst)
expUsersCsv("Second", listUserWithEmailSecond)
