# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def Bayes_classifier_risks(Probability_sick,Probability_healthy,Result_Dictionary,PathOfFile):
    List_Baes_diagnosis=[]
    List_Baes_risks_diagnosis=[]
    List_Correct_diagnosis=[]
    f=open(PathOfFile,"rb")
    li = f.readlines()
    f.close()

    count=1
    for stroka in li:
        Person_Age,Person_Pol,Person_Har,Person_VG,Person_YH,Person_YS,Person_Card,Person_MaxP,Person_Sten,Person_StepTest,Person_Sklon,Person_Sosyd,Person_SPS,Person_Rez = stroka.split()

        print "\nПациент №"+str(count) +" имеет такие атрибуты:"
        print " возраст =",Person_Age
        print " пол =",Person_Pol
        print " характер боли в сердце (один из четырех)=",Person_Har
        print " верхняя граница давления в состоянии покоя	=",Person_VG
        print " уровень холестерина в крови mg/dl =",Person_YH
        print " уровень сахара в крови больший 20 mg/dl=",Person_YS
        print " результаты кардиограммы в состоянии покоя (values 0,1,2)=",Person_Card
        print " максимальная величина пульса=",Person_MaxP
        print " данные степ-теста=",Person_StepTest
        print " склонение данных по степ-тесту=",Person_Sklon
        print " количество основных сосудов (0-3) выявленных рентгеноскопие =",Person_Sosyd
        print " степень повреждения сосудов =",Person_SPS
        print "--------------------------------------------------------"

        #номер пациента
        count+=1
        #Список, в котором хранятся все параметры пациента
        List_Person_Paramets=[Person_Age, Person_Har,Person_VG,Person_YH,Person_YS,Person_Card,Person_MaxP, Person_StepTest,Person_Sklon,Person_Sosyd,Person_SPS,Person_Pol]
        #Список названий параметров
        Keys_param=('List_Age','List_Har','List_VG','List_YH','List_YS','List_Card','List_MaxP','List_StepTest','List_Sklon','List_Sosyd','List_Sps','List_Pol')

        #Определим болен или здоров пациент
        print " Определим диагноз больного по построенному классфикатору:"
        Patient_Healthy = 1
        Patient_Sick = 1

        j=0
        for i in  Keys_param:
            if i=='List_Pol' or i=='List_Sten':
                if float(List_Person_Paramets[j])==0.0:
                    Patient_Healthy =float(Patient_Healthy) * float(Result_Dictionary[i][8])
                    Patient_Sick =float(Patient_Sick) * float(Result_Dictionary[i][9])
                if float(List_Person_Paramets[j])==1.0:
                    Patient_Healthy = float(Patient_Healthy) * float(Result_Dictionary[i][10])
                    Patient_Sick = float(Patient_Sick) * float(Result_Dictionary[i][11])
            else:
                if float(List_Person_Paramets[j])<Result_Dictionary[i][12]:
                    Patient_Healthy =float(Patient_Healthy) * float(Result_Dictionary[i][8])
                    Patient_Sick =float(Patient_Sick) * float(Result_Dictionary[i][9])
                if float(List_Person_Paramets[j])>=Result_Dictionary[i][12]:
                    Patient_Healthy = float(Patient_Healthy) * float(Result_Dictionary[i][10])
                    Patient_Sick = float(Patient_Sick) * float(Result_Dictionary[i][11])
            j+=1


        #Определим болен или здоров пациент
        print "вероятность, что пациент здоров = ",Patient_Healthy
        print "вероятность, что пациент болен = ",Patient_Sick

        BayesClassifier_Diagnosis=0
        if Patient_Sick>Patient_Healthy:
            print "Диагноз, поставленный программой = БОЛЕН"
            BayesClassifier_Diagnosis = 2
        if Patient_Healthy>Patient_Sick:
            print "Диагноз, поставленный программой = ЗДОРОВ"
            BayesClassifier_Diagnosis = 1
        if Patient_Healthy==Patient_Sick:
            print "Диагноз, поставленный программой = НЕ ОПРЕДЕЛЁН(Вероятности равны)"

         #Сравниваем диагноз, полученный классификатором с заданным
        if BayesClassifier_Diagnosis==int(Person_Rez):
            print"Диагнозы совпали!"
        elif BayesClassifier_Diagnosis<>int(Person_Rez):
            print "Диагнозы не совпали"


        #Определим болен или здоров пациент с учётом рисков
        print "--------Определим болен или здоров пациент с учётом рисков--------"

        Say_sick_is_healthy = 1
        Say_healthy_is_sick = 5
        print "Данные исходные "
        print "Сказать больному, что он здоров =",Say_sick_is_healthy
        print "Сказать здоровому, что он болен =",Say_healthy_is_sick

        #нормируем
        amount_risks = Say_sick_is_healthy+Say_healthy_is_sick
        Patient_Healthy_with_risk = Patient_Healthy*Say_healthy_is_sick/float(amount_risks)*Probability_sick
        Patient_Sick_with_risk = Patient_Sick*Say_sick_is_healthy/float(amount_risks)*Probability_healthy
        print "вероятность, что пациент здоров с учётом рисков= ",Patient_Healthy_with_risk
        print "вероятность, что пациент болен с учётом рисков= ",Patient_Sick_with_risk

        BayesClassifier_Risks_Diagnosis=0
        if Patient_Healthy_with_risk<Patient_Sick_with_risk:
            print "Диагноз, поставленный программой с учетом рисков = БОЛЕН"
            BayesClassifier_Risks_Diagnosis = 2
        if Patient_Healthy_with_risk>Patient_Sick_with_risk:
            print "Диагноз, поставленный программой с учетом рисков = ЗДОРОВ"
            BayesClassifier_Risks_Diagnosis = 1
        if Patient_Healthy_with_risk==Patient_Sick_with_risk:
            print "Диагноз, поставленный программой с учетом рисков = НЕ ОПРЕДЕЛЁН(Вероятности равны)"

        if BayesClassifier_Risks_Diagnosis==int(Person_Rez):
            print"Диагнозы совпали!"
        elif BayesClassifier_Risks_Diagnosis<>int(Person_Rez):
            print "Диагнозы не совпали"

        List_Baes_diagnosis.append(BayesClassifier_Diagnosis)
        List_Baes_risks_diagnosis.append(BayesClassifier_Risks_Diagnosis)
        List_Correct_diagnosis.append(int(Person_Rez))
    return (List_Baes_diagnosis,List_Baes_risks_diagnosis,List_Correct_diagnosis)