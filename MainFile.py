# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Primitive import *
from Bayes import *
from Bayes_risks import *
from Quality_classification import *
from Kendall import *

#объявим переменные параметров
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
# List_Card - нету (Юлин вариант)
List_Age = [] #возраст
List_Har = []#характер боли в сердце
List_VG = [] #верх граница давл
List_YH = []#уровень холестерина
List_YS = []# уровень сахара
List_Card = [] #результаты кардиограммы с состоянии покоя
List_MaxP = [] #макс величина пульса
List_Sten = [] #наличие стенокардии
List_StepTest = [] #данные степ-теста
List_Sklon = [] #склонение данных по степ-тесту
List_Sosyd = [] #кол-во основных сосудов
List_Sps = [] #степень повреждения сосудов
#Выданный результат
List_Rez =[]

#PathOfFileTraining="heart4.csv"


def Readfile_and_FillLists(PathOfFile):
    f=open(PathOfFile,"rb")
    li = f.readlines()
    f.close()
    for stroka in li:
        Person_Age,Person_Pol,Person_Har,Person_VG,Person_YH,Person_YS,Person_Card,Person_MaxP,Person_Sten,Person_StepTest,Person_Sklon,Person_Sosyd,Person_Sps,Person_Rez = stroka.split()
        List_Age.append(float(Person_Age))
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

for i in range(5):
    #Тренировочный набор - набор, по которому обучается классификатор
    #Тестовый набор - набор, по которому проверяется классификатор
    if   i==0:
        print "---------------------------------НАЧАЛЬНЫЕ ЗНАЧЕНИЯ---------------------------------"
    elif i==1:
        print "\n\n\n\n---------------------------------МЕТОД Holdout--------------------------------------"
    elif i==2:
        print "\n\n\n\n---------------------------------МЕТОД Stratification-------------------------------"
    elif i==3:
        print "\n\n\n\n---------------------------------МЕТОД Cross-validation-----------------------------"
    elif i==4:
        print "\n\n\n\n---------------------------------МЕТОД Bootstrap------------------------------------"


    PathOfFileTraining="data\heart"+str(i)+".csv"   #Файл, в котором тренировочный набор, 1-Holdout, 2-Stratification, 3-Cross-validation (K=9), 4-Bootstrap
    PathOfFileTesting="data\pacient"+str(i)+".csv"  #Файл, в котором тестовый набор,      1-Holdout, 2-Stratification, 3-Cross-validation (K=9), 4-Bootstrap

    #ВЫЗОВ ОСНОВНЫХ ФУНКЦИЙ
    #Чтение исходых данных и занесения их в списки
    Readfile_and_FillLists(PathOfFileTraining)
    #Оценка коеффициента ранговой корреляциии(Спирмен/Кэндалл)
    Kendall(List_Age,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,List_Rez)
    #Результаты работы и оценка работы ПРИМИТИВНОГО КЛАССИФИКАТОРА
    Result_Primitive=Primitive_Classifier(List_Rez,PathOfFileTesting)
    #Списки с параметрами коеффициентов
    List_param=(List_Age,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_StepTest,List_Sklon,List_Sosyd,List_Sps)
    List_other_param=List_Sten
    #Результаты работы БАйЕСОВСКОГО КЛАССИФИКАТОРА
    Result_Vocabulary = Bayes_classifier(Result_Primitive[0],Result_Primitive[1],Result_Primitive[2],Result_Primitive[3],List_param, List_other_param, List_Rez)
    #Оценка работы БАйЕСОВСКОГО КЛАССИФИКАТОРА. Результаты работы и оценка работы БАйЕСОВСКОГО КЛАССИФИКАТОРА С УЧЁТОМ РИСКОВ
    Result_Bayes_risks=Bayes_classifier_risks(Result_Primitive[2],Result_Primitive[3],Result_Vocabulary,PathOfFileTesting)
    #Вычисление характеристик качества классификации (уровни ошибок первого и второго рода)
    define_quality(Result_Primitive[4],Result_Bayes_risks[0],Result_Bayes_risks[1],Result_Bayes_risks[2])