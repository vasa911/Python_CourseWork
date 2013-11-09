# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def Primitive_Classifier(List_Rez,PathOfFile):
    print u"\n-----------------------ПРИМИТИВНЫЙ КЛАССИФИКАТОР-----------------------"
    number_patients = len(List_Rez)
    print u"Общее количество пациентов =",number_patients

    # Подсчитаем  Количество здоровых и больных пациентов
    number_sick = 0
    number_healthy = 0
    for i in range(len(List_Rez)):
        if List_Rez[i]== 1:
            number_healthy = number_healthy + 1
        if List_Rez[i]== 2:
            number_sick = number_sick + 1
    print "Количество больных пациентов =",number_sick
    print "Количество здоровых пациентов =",number_healthy


    # Определим вероятности, что пациент болен или здоров
    Probability_sick = number_sick/float(number_patients)
    Probability_healthy = number_healthy/float(number_patients)


    print "Вероятность больных пациентов =",Probability_sick
    print "Вероятность здоровых пациентов =",Probability_healthy



    #Объявим списки, в которых будут храниться выданный диагноз примититвного классификатора
    List_primitive_diagnosis = []
    List_primitive_healthy = []
    List_primitive_sick = []


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
    f=open(PathOfFile,"rb")
    li = f.readlines()
    f.close()

    for stroka in li:
        Person_Age,Person_Pol,Person_Har,Person_VG,Person_YH,Person_YS,Person_Card,Person_MaxP,Person_Sten,Person_StepTest,Person_Sklon,Person_Sosyd,Person_Sps,Person_Rez = stroka.split()

         #Определим болен или здоров пациент
        if Probability_sick>Probability_healthy:
            diagnosis = 2
        if Probability_healthy>Probability_sick:
            diagnosis = 1
        if Probability_healthy==Probability_sick:
            diagnosis =0
        List_primitive_diagnosis.append(diagnosis)
        List_primitive_healthy.append(Probability_healthy)
        List_primitive_sick.append(Probability_sick)


        print "Результат работы:"
        if diagnosis==1 :
            print " Диагноз = ЗДОРОВ"
        if diagnosis==2 :
            print " Диагноз= БОЛЕН"
        print " Вероятность, что пациент здоров = ",Probability_healthy
        print " Вероятность, что пациент болен = ",Probability_sick

        if diagnosis==int(Person_Rez):
            print"Диагнозы совпали!"
        if diagnosis<>int(Person_Rez):
            print "Диагнозы не совпали"
    return (number_sick, number_healthy, Probability_sick, Probability_healthy,List_primitive_diagnosis)