# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def define_quality(List_primitive_diagnosis,List_Baes_diagnosis,List_Baes_risks_diagnosis,List_Correct_diagnosis):
    #Пусть TP-Правильно определённые больные; TN-Правильно определённые здоровые; FP-Человек здоров, а его причислили к больным; FN-Человек болен, а его причислили к здоровым
    TP=[0,0,0]   #В списках такой порядок: Байесовский,Байесовский с учетом рисков, Примитивный
    TN=[0,0,0]
    FP=[0,0,0]
    FN=[0,0,0]
    #Пусть Np - кол-во "положительных" объектов, а  Nn - кол-во "отрицательных"
    Np=[0,0,0]
    Nn=[0,0,0]
    #нормированные уровни ошибок первого и второго рода
    nFN=[0,0]
    nFP=[0,0]
    nTN=[0,0]
    nTP=[0,0]
    #Меры точности (precision) и отзыва (recall)
    Precision=[0,0]
    Recall=[0,0]
    #Посчитаем количество объектов для каждого классификатора
    def count_objects(List_classificator,index):
        for i in range(len(List_Correct_diagnosis)):
            if (List_Correct_diagnosis[i]==2) and (List_classificator[i]==2):
                TP[index]+=1
            if (List_Correct_diagnosis[i]==1) and (List_classificator[i]==2):
                FP[index]+=1
            if (List_Correct_diagnosis[i]==2) and (List_classificator[i]==1):
                FN[index]+=1
            if (List_Correct_diagnosis[i]==1) and (List_classificator[i]==1):
                TN[index]+=1

    #Посчитаем количество кол-во "положительных" и "отрицательных" объектов для каждого классификатора
    def count_positive_negative():
        for i in range(len(TP)):
            Np[i]=TP[i]-FN[i]
            Nn[i]=TN[i]-FP[i]

    #Посчитаем нормированные уровни ошибок первого и второго рода
    def count_errors():
        for i in range(len(nFN)):
            nFN[i]=FN[i]/float(Np[i])
            nFP[i]=FP[i]/float(Nn[i])
            nTN[i]=TN[i]/float(Nn[i])
            nTP[i]=TP[i]/float(Np[i])

    def precision_recall():
        for i in range(len(Precision)):
            Precision[i]=TP[i]/float(TP[i]+FP[i])*100
            Recall[i]=TP[i]/float(TP[i]+FN[i])*100

    count_objects(List_Baes_diagnosis,0)
    count_objects(List_Baes_risks_diagnosis,1)
    count_objects(List_primitive_diagnosis,2)
    count_positive_negative()
    count_errors()
    precision_recall()

    #Вывод результатов
    print
    print "-----------------------Расчет уровней ошибок первого и второго рода-----------------------"
    print "Результат работы примитивного классификатора "+str(List_primitive_diagnosis)
    print "Результат работы Байесовского классификатора "+str(List_Baes_diagnosis)
    print "Результат работы Байесовского классификатора с учетом рисков"+str(List_Baes_risks_diagnosis)
    for i in range(len(TP)):
        if i==2:
            print"          ПРИМИТИВНЫЙ КЛАССИФИКАТОР"
            print "Количество обнаружений: TP="+str(TP[i])+" TN="+str(TN[i])+" FP="+str(FP[i])+" FN="+str(FN[i])
        else:
            if i==0:
                print "          БАЙЕСОВСКИЙ КЛАССИФИКАТОР"
            else:
                print "          БАЙЕСОВСКИЙ КЛАССИФИКАТОР С УЧЕТОМ РИСКОВ"
            print "Количество обнаружений: TP="+str(TP[i])+" TN="+str(TN[i])+" FP="+str(FP[i])+" FN="+str(FN[i])+"\nНормированные уровни ошибок первого и второго рода: nFN="+str(nFN[i])+" nFP="+str(nFP[i])+" nTN="+str(nTN[i])+" nTP="+str(nTP[i])+"\nМера точности="+str(Precision[i])+"% Мера отзыва="+str(Recall[i])+"%"