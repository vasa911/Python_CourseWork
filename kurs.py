# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import scipy
#import scipy.stats
#объявим переменные атрибутов
from Spearman import *
from Primitiv import *
#from Baes import *


Person_Age =''
Person_Pol =''
Person_Har =''
Person_VG =''
Person_YH =''
Person_YS =''
Person_Card =''
Person_MaxP =''
Person_Sten =''
Person_StepTest =''
Person_Sklon =''
Person_Sosyd =''
Person_Sps =''

#Выданный результат
Person_Rez =''

#объявим списки для хранения атрибутов
# мой вариант
#8 9 10 11 12 13 1 2 3 4 5 6
List_Age = [] #возраст
List_Pol = [] #пол
List_Har = []#характер боли в сердце
List_VG = [] #верх граница давл
List_YH = []#уровень холестерина
List_YS = []# уровень сахара
List_Card = [] #результаті кардиограммі с состоянии покоя
List_MaxP = [] #макс величина пульса
List_Sten = [] #наличие стенокардии
List_StepTest = [] #данные степ-теста
List_Sklon = [] #склонение данных по степ-тесту
List_Sosyd = [] #кол-во основных сосудов
List_Sps = [] #степень повреждения сосудов
#Выданный результат
List_Rez =[]

def readfile_and_filllists():
    PathOfFile = "heart.csv"
    f=open(PathOfFile,"rb")
    li = f.readlines()
    f.close()
    #for i in li:
       # print i
    for stroka in li:
        Person_Age,Person_Pol,Person_Har,Person_VG,Person_YH,Person_YS,Person_Card,Person_MaxP,Person_Sten,Person_StepTest,Person_Sklon,Person_Sosyd,Person_Sps,Person_Rez = stroka.split()
        List_Age.append(float(Person_Age))
        List_Pol.append(float(Person_Pol))
        List_Har.append(float(Person_Har))
        List_VG.append(float(Person_VG))
        List_YH.append(float(Person_YH))
        List_YS.append(float(Person_YS))
        List_Card.append(float(Person_Card))
        List_MaxP.append(float(Person_MaxP))
        List_Sten.append(float(Person_Sten))
        List_StepTest.append(float(Person_StepTest))
        List_Sklon.append(float(Person_Sklon))
        List_Sosyd.append(float(Person_Sosyd))
        List_Sps.append(float(Person_Sps))
        #Выданный результат список
        List_Rez.append(float(Person_Rez))

#вызов функций
readfile_and_filllists()
Spearmen(List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,List_Rez)
Result_Primitive=Primitive_Classifier(List_Rez)
#Baes_classifier(Result_Primitive[0],Result_Primitive[1],Result_Primitive[2],Result_Primitive[3],List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,List_Rez)
