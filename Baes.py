# -*- coding: cp1251 -*-
#«Байесовский классификатор»
def Baes_classifier(number_sick,number_healthy,Probability_sick,Probability_healthy,List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_SPS,List_Rez):
    #List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,
    number_patients = len(List_Rez)
    print "-----------------------«Байесовский классификатор»-----------------------"

    List_amount_patient={'Age':{'Less_Healthy':0,'Less_Sick':0,'More_Healthy':0,'More_Sick':0}}
    List_probability_patient={'Age':{'Less_Healthy':0,'Less_Sick':0,'More_Healthy':0,'More_Sick':0}}
    #ПАРАМЕТР №1 - ВОЗРАСТ
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №1 Возраст-------"
    Summa_Age = 0 #сумма возрастов
    for i in range(len(List_Age)):
        Summa_Age = Summa_Age + List_Age[i]
    Middle_Age = Summa_Age/float(len(List_Age)) #средний возраст
    print "-------Средний возраст =",Middle_Age," лет"

    # Подсчитаем  Количество пациентов, которые старше или младше среднего возраста
    amount_Age_Bigger = 0
    amount_Age_Smaller = 0
    for i in range(len(List_Age)):
        if float(List_Age[i])>=Middle_Age:
            amount_Age_Bigger =amount_Age_Bigger +1
        if float(List_Age[i])<Middle_Age:
            amount_Age_Smaller =amount_Age_Smaller +1
    print "Количество пациентов, которые старше среднего возраста =",amount_Age_Bigger
    print "Количество пациентов, которые младше среднего возраста =",amount_Age_Smaller

    # Определим вероятности, что пациент младше или старше
    Probability_Age_Bigger = amount_Age_Bigger/float(number_patients)
    Probability_Age_Smaller = amount_Age_Smaller/float(number_patients)

    print "Вероятность того, что пациент старше среднего возраста =",Probability_Age_Bigger
    print "Вероятность того, что пациент младше среднего возраста=",Probability_Age_Smaller

   '''
    amount_Age_Smaller_Z = 0
    amount_Age_Smaller_B = 0
    amount_Age_Bigger_Z = 0
    amount_Age_Bigger_B = 0

    Probability_Age_Smaller_Z = 0
    Probability_Age_Smaller_B = 0
    Probability_Age_Bigger_Z = 0
    Probability_Age_Bigger_B = 0'''

    #Подсчитываем количество
    for i in range(len(List_Age)):
        #   младше среднего возраста
        if (float(List_Age[i])<Middle_Age)and (int(List_Rez[i])== 1):
            List_amount_patient['Age']['Less_Healthy'] +=1
        if (float(List_Age[i])<Middle_Age)and (int(List_Rez[i])== 2):
            List_amount_patient['Age']['Less_Sick'] +=1
        #  старше среднего возраста
        if (float(List_Age[i])>=Middle_Age)and (int(List_Rez[i])== 1):
            List_amount_patient['Age']['More_Healthy'] +=1
        if (float(List_Age[i])>=Middle_Age)and (int(List_Rez[i])== 2):
            List_amount_patient['Age']['More_Sick'] +=1

    #Подсчитываем вероятность
    List_probability_patient['Age']['Less_Healthy'] = List_amount_patient['Age']['Less_Healthy']/float(number_healthy)
    List_probability_patient['Age']['Less_Sick'] = List_amount_patient['Age']['Less_Sick']/float(number_sick)

    List_probability_patient['Age']['More_Healthy']= List_amount_patient['Age']['More_Healthy']/float(number_healthy)
    List_probability_patient['Age']['More_Sick'] = List_amount_patient['Age']['More_Sick']/float(number_sick)


    print "Вероятность того, что пацент младше среднего возраста и"
    print "здоров = ",List_probability_patient['Age']['Less_Healthy']
    print " и болен = ",List_probability_patient['Age']['Less_Sick']
    print "Вероятность того, что пацент старше среднего возраста и"
    print "здоров = ",List_probability_patient['Age']['More_Healthy']
    print " и болен = ",List_probability_patient['Age']['More_Sick']

    #Подсчет вероятностей с учетом примитивного классификатора
    #Таблица Баесовских вероятностей
    V_Age_1 = 0
    V_Age_2 = 0
    V_Age_3 = 0
    V_Age_4 = 0

    #Вероятность, что здоров ,если возраст младше
    V_Age_1 = float(Probability_healthy)*Probability_Age_Smaller_Z/float(Probability_Age_Smaller)

    #Вероятность, что болен,если возраст младше
    V_Age_2 = float(Probability_sick)*Probability_Age_Smaller_B/float(Probability_Age_Smaller)
    #Вероятность, что здоров ,если возраст старше
    V_Age_3 = float(Probability_healthy)*Probability_Age_Bigger_Z/float(Probability_Age_Bigger)

    #Вероятность, что болен,если возраст старше
    V_Age_4 = float(Probability_sick)*Probability_Age_Bigger_B/float(Probability_Age_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что здоров ,если возраст младше =",V_Age_1
    print "Вероятность, что болен,если возраст младше =",V_Age_2
    print "Вероятность, что здоров ,если возраст старше =",V_Age_3
    print "Вероятность, что болен,если возраст старше =",V_Age_4
    print "----------------------------------------------"

    #Параметр №2 Пол
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №2 Пол-------"
    # Подсчитаем  Количество пациентов-мужчин
    # Подсчитаем  Количество пациентов-женщин
    amount_Pol_Myj = 0
    amount_Pol_Jen = 0
    d=0
    for d in range(len(List_Pol)):
        if float(List_Pol[d])==0.0:
            amount_Pol_Myj =amount_Pol_Myj +1
        if float(List_Pol[d])==1.0:
            amount_Pol_Jen =amount_Pol_Jen +1
    print "Количество пациентов-мужчин =",amount_Pol_Myj
    print "Количество пациентов-женщин =",amount_Pol_Jen
    # Определим вероятности, что пациент-мужчина или пациент-женщина
    Probability_Pol_Myj = amount_Pol_Myj/float(number_patients)
    Probability_Pol_Jen = amount_Pol_Jen/float(number_patients)

    print "Вероятность, что пациент-мужчина =",Probability_Pol_Myj
    print "Вероятность, что пациент-женщина=",Probability_Pol_Jen

    amount_Pol_Myj_Z = 0
    amount_Pol_Myj_B = 0
    amount_Pol_Jen_Z = 0
    amount_Pol_Jen_B = 0

    Probability_Pol_Myj_Z = 0
    Probability_Pol_Myj_B = 0
    Probability_Pol_Jen_Z = 0
    Probability_Pol_Jen_B = 0

    for d in range(len(List_Pol)):
        # мужчины
        if (float(List_Pol[d])==0.0)and (int(List_Rez[d])== 1):
            amount_Pol_Myj_Z = amount_Pol_Myj_Z+1
        if (float(List_Pol[d])==0.0)and (int(List_Rez[d])== 2):
            amount_Pol_Myj_B = amount_Pol_Myj_B+1
        #  женщины
        if (float(List_Pol[d])==1.0)and (int(List_Rez[d])== 1):
            amount_Pol_Jen_Z = amount_Pol_Jen_Z + 1
        if (float(List_Pol[d])==1.0)and (int(List_Rez[d])== 2):
            amount_Pol_Jen_B = amount_Pol_Jen_B+1

    Probability_Pol_Myj_Z = amount_Pol_Myj_Z/float(number_healthy)
    Probability_Pol_Myj_B = amount_Pol_Myj_B/float(number_sick)
    Probability_Pol_Jen_Z = amount_Pol_Jen_Z/float(number_healthy)
    Probability_Pol_Jen_B = amount_Pol_Jen_B/float(number_sick)

    print "-----пациент-мужчина"
    print "Здоровые = ",Probability_Pol_Myj_Z
    print "Больные = ",Probability_Pol_Myj_B
    print "-----пациент-женщина"
    print "Здоровые = ",Probability_Pol_Jen_Z
    print "Больные = ",Probability_Pol_Jen_B

    #Таблица Байесовских вероятностей
    V_Pol_1 = 0
    V_Pol_2 = 0
    V_Pol_3 = 0
    V_Pol_4 = 0

    #Вероятность, что пациент-мужчина + здоров
    V_Pol_1 = float(Probability_healthy)*Probability_Pol_Myj_Z/float(Probability_Pol_Myj)
    #Вероятность, что пациент-мужчина + болен
    V_Pol_2 = float(Probability_sick)*Probability_Pol_Myj_B/float(Probability_Pol_Myj)

    #Вероятность, что пациент-женщина + здоров
    V_Pol_3 = float(Probability_healthy)*Probability_Pol_Jen_Z/float(Probability_Pol_Jen)
    #Вероятность, что пациент-женщина + болен
    V_Pol_4 = float(Probability_sick)*Probability_Pol_Jen_B/float(Probability_Pol_Jen)

    print "----------------------------------------------"
    print "Вероятность, что пациент-мужчина + здоров =",V_Pol_1
    print "Вероятность, что пациент-мужчина + болен =",V_Pol_2
    print "Вероятность, что пациент-женщина + здоров =",V_Pol_3
    print "Вероятность, что пациент-женщина + болен =",V_Pol_4
    print "----------------------------------------------"


    #Параметр №4 верхняя граница давления в состоянии покоя
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    print "-------Параметр №4 Верхняя граница давления в состоянии покоя-------"
    Summa_VG = 0
    for d in range(len(List_VG)):
        Summa_VG = Summa_VG + List_VG[d]
    Middle_VG = Summa_VG/float(len(List_VG))
    print "-------Среднее значение границы давления в состоянии покоя =",Middle_VG

    # Подсчитаем  Количество пациентов с большей границей давления
    # Подсчитаем  Количество пациентов, с меньшей границей давления
    amount_VG_Smaller = 0
    amount_VG_Bigger = 0

    for d in range(len(List_VG)):
        if float(List_VG[d])>=Middle_VG:
            amount_VG_Bigger =amount_VG_Bigger +1
        if float(List_VG[d])<Middle_VG:
            amount_VG_Smaller =amount_VG_Smaller +1
    print "Количество пациентов с меньшей границей давления=",amount_VG_Smaller
    print "Количество пациентов с большей границей давления=",amount_VG_Bigger

    # Определим вероятности, что пациент младше или старше
    Probability_VG_Smaller = amount_VG_Smaller/float(number_patients)
    Probability_VG_Bigger = amount_VG_Bigger/float(number_patients)

    print "Вероятность пациентов с большей границей давления=",Probability_VG_Bigger
    print "Вероятность пациентов с меньшей границей давления=",Probability_VG_Smaller

    amount_VG_Smaller_Z = 0
    amount_VG_Smaller_B = 0
    amount_VG_Bigger_Z = 0
    amount_VG_Bigger_B = 0

    Probability_VG_Smaller_Z = 0
    Probability_VG_Smaller_B = 0
    Probability_VG_Bigger_Z = 0
    Probability_VG_Bigger_B = 0
    for d in range(len(List_VG)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_VG[d])<Middle_VG)and (int(List_Rez[d])== 1):
            amount_VG_Smaller_Z = amount_VG_Smaller_Z+1
        if (float(List_VG[d])<Middle_VG)and (int(List_Rez[d])== 2):
            amount_VG_Smaller_B = amount_VG_Smaller_B+1
        #  старшие
        if (float(List_VG[d])>=Middle_VG)and (int(List_Rez[d])== 1):
            amount_VG_Bigger_Z = amount_VG_Bigger_Z+1
        if (float(List_VG[d])>=Middle_VG)and (int(List_Rez[d])== 2):
            amount_VG_Bigger_B = amount_VG_Bigger_B+1


    Probability_VG_Smaller_Z = amount_VG_Smaller_Z/float(number_healthy)
    Probability_VG_Smaller_B = amount_VG_Smaller_B/float(number_sick)

    Probability_VG_Bigger_Z = amount_VG_Bigger_Z/float(number_healthy)
    Probability_VG_Bigger_B = amount_VG_Bigger_B/float(number_sick)

    print "-----Граница давления меньше"
    print "Здоровые = ",Probability_VG_Smaller_Z
    print "Больные = ",Probability_VG_Smaller_B
    print "-----Граница давления больше"
    print "Здоровые = ",Probability_VG_Bigger_Z
    print "Больные = ",Probability_VG_Bigger_B

    #Таблица Баесовских вероятностей
    V_VG_1 = 0
    V_VG_2 = 0
    V_VG_3 = 0
    V_VG_4 = 0

    #Вероятность, что здоров ,если граница меньше
    V_VG_1 = float(Probability_healthy)*Probability_VG_Smaller_Z/float(Probability_VG_Smaller)

    #Вероятность, что болен,если граница меньше
    V_VG_2 = float(Probability_sick)*Probability_VG_Smaller_B/float(Probability_VG_Smaller)
    #Вероятность, что здоров ,если граница больше
    V_VG_3 = float(Probability_healthy)*Probability_VG_Bigger_Z/float(Probability_VG_Bigger)

    #Вероятность, что болен,если граница больше
    V_VG_4 = float(Probability_sick)*Probability_VG_Bigger_B/float(Probability_VG_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что Граница давления меньше + здоров =",V_VG_1
    print "Вероятность, что Граница давления меньше + болен=",V_VG_2
    print "Вероятность, что Граница давления больше + здоров =",V_VG_3
    print "Вероятность, что Граница давления больше + болен =",V_VG_4
    print "----------------------------------------------"

    #Параметр №5 уровень холестерина в крови mg/dl
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №5 уровень холестерина в крови mg/dl -------"

    Summa_YH = 0
    for d in range(len(List_YH)):
        Summa_YH = Summa_YH + List_YH[d]
    Middle_YH = Summa_YH/float(len(List_YH))
    print "-------Средний уровень холестерина в крови =",Middle_YH," mg/dl"

    # Подсчитаем  Количество пациентов, у которых уровень холестерина больше среднего
    # Подсчитаем  Количество пациентов, у которыхуровень холестерина меньше среднего
    amount_YH_Bigger = 0
    amount_YH_Smaller = 0
    for d in range(len(List_YH)):
        if float(List_YH[d])>=Middle_YH:
            amount_YH_Bigger =amount_YH_Bigger +1
        if float(List_YH[d])<Middle_YH:
            amount_YH_Smaller =amount_YH_Smaller +1
    print "Количество пациентов, у которых уровень холестерина больше среднего =",amount_YH_Bigger
    print "Количество пациентов, у которых уровень холестерина меньше среднего =",amount_YH_Smaller

    # Определим вероятности, что у пациента уровнеь больше или меньше
    Probability_YH_Bigger = amount_YH_Bigger/float(number_patients)
    Probability_YH_Smaller = amount_YH_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых уровень холестерина больше среднего=",Probability_YH_Bigger
    print "Вероятность пациентов, у которых уровень холестерина меньше среднего=",Probability_YH_Smaller

    amount_YH_Smaller_Z = 0
    amount_YH_Smaller_B = 0
    amount_YH_Bigger_Z = 0
    amount_YH_Bigger_B = 0

    Probability_YH_Smaller_Z = 0
    Probability_YH_Smaller_B = 0
    Probability_YH_Bigger_Z = 0
    Probability_YH_Bigger_B = 0
    for d in range(len(List_YH)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_YH[d])<Middle_YH)and (int(List_Rez[d])== 1):
            amount_YH_Smaller_Z = amount_YH_Smaller_Z+1
        if (float(List_YH[d])<Middle_YH)and (int(List_Rez[d])== 2):
            amount_YH_Smaller_B = amount_YH_Smaller_B+1
        #  старшие
        if (float(List_YH[d])>=Middle_YH)and (int(List_Rez[d])== 1):
            amount_YH_Bigger_Z = amount_YH_Bigger_Z+1
        if (float(List_YH[d])>=Middle_YH)and (int(List_Rez[d])== 2):
            amount_YH_Bigger_B = amount_YH_Bigger_B+1


    Probability_YH_Smaller_Z = amount_YH_Smaller_Z/float(number_healthy)
    Probability_YH_Smaller_B = amount_YH_Smaller_B/float(number_sick)

    Probability_YH_Bigger_Z = amount_YH_Bigger_Z/float(number_healthy)
    Probability_YH_Bigger_B = amount_YH_Bigger_B/float(number_sick)

    print "-----Уровень холестерина меньше среднего"
    print "Здоровые = ",Probability_YH_Smaller_Z
    print "Больные = ",Probability_YH_Smaller_B
    print "-----Уровень холестерина больше среднего"
    print "Здоровые = ",Probability_YH_Bigger_Z
    print "Больные = ",Probability_YH_Bigger_B

    #Таблица Байесовских вероятностей
    V_YH_1 = 0
    V_YH_2 = 0
    V_YH_3 = 0
    V_YH_4 = 0

    #Вероятность, что здоров ,если уровень холестерина меньше среднего
    V_YH_1 = float(Probability_healthy)*Probability_YH_Smaller_Z/float(Probability_YH_Smaller)
    #Вероятность, что болен,если уровень холестерина меньше среднего
    V_YH_2 = float(Probability_sick)*Probability_YH_Smaller_B/float(Probability_YH_Smaller)

    #Вероятность, что здоров ,если уровень холестерина больше среднего
    V_YH_3 = float(Probability_healthy)*Probability_YH_Bigger_Z/float(Probability_YH_Bigger)
    #Вероятность, что болен,если уровень холестерина больше среднего
    V_YH_4 = float(Probability_sick)*Probability_YH_Bigger_B/float(Probability_YH_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что уровень холестерина меньше среднего + здоров  =",V_YH_1
    print "Вероятность, что уровень холестерина меньше среднего + болен =",V_YH_2
    print "Вероятность, что уровень холестерина больше среднего + здоров  =",V_YH_3
    print "Вероятность, что уровень холестерина больше среднего + здоров =",V_YH_4
    print "----------------------------------------------"


    #Параметр №6 уровень сахара в крови больший 120 mg/dl
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №6 уровень сахара в крови больший 120 mg/dl   -------"

    Summa_YS = 0
    for d in range(len(List_YS)):
        Summa_YS = Summa_YS + List_YS[d]
    Middle_YS = Summa_YS/float(len(List_YS))
    print "-------Средний уровень сахара в крови =",Middle_YS," mg/dl"

    # Подсчитаем  Количество пациентов, у которых уровень сахара больше 120
    # Подсчитаем  Количество пациентов, у которых уровень сахара меньше 120
    amount_YS_Bigger = 0
    amount_YS_Smaller = 0
    for d in range(len(List_YS)):
        if float(List_YS[d])>=Middle_YS:
            amount_YS_Bigger =amount_YS_Bigger +1
        if float(List_YS[d])<Middle_YH:
            amount_YS_Smaller =amount_YS_Smaller +1
    print "Количество пациентов, у которых уровень сахара больше среднего =",amount_YS_Bigger
    print "Количество пациентов, у которых уровень сахара меньше среднего =",amount_YS_Smaller

    # Определим вероятности, что у пациента уровень больше или меньше
    Probability_YS_Bigger = amount_YS_Bigger/float(number_patients)
    Probability_YS_Smaller = amount_YS_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых уровень сахара больше 120=",Probability_YS_Bigger
    print "Вероятность пациентов, у которых уровень сахара меньше 120=",Probability_YS_Smaller

    amount_YS_Smaller_Z = 0
    amount_YS_Smaller_B = 0
    amount_YS_Bigger_Z = 0
    amount_YS_Bigger_B = 0

    Probability_YS_Smaller_Z = 0
    Probability_YS_Smaller_B = 0
    Probability_YS_Bigger_Z = 0
    Probability_YS_Bigger_B = 0
    for d in range(len(List_YS)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_YS[d])<Middle_YS)and (int(List_Rez[d])== 1):
            amount_YS_Smaller_Z = amount_YS_Smaller_Z+1
        if (float(List_YS[d])<Middle_YS)and (int(List_Rez[d])== 2):
            amount_YS_Smaller_B = amount_YS_Smaller_B+1
        #  старшие
        if (float(List_YS[d])>=Middle_YS)and (int(List_Rez[d])== 1):
            amount_YS_Bigger_Z = amount_YS_Bigger_Z+1
        if (float(List_YS[d])>=Middle_YS)and (int(List_Rez[d])== 2):
            amount_YS_Bigger_B = amount_YS_Bigger_B+1


    Probability_YS_Smaller_Z = amount_YS_Smaller_Z/float(number_healthy)
    Probability_YS_Smaller_B = amount_YS_Smaller_B/float(number_sick)

    Probability_YS_Bigger_Z = amount_YS_Bigger_Z/float(number_healthy)
    Probability_YS_Bigger_B = amount_YS_Bigger_B/float(number_sick)

    print "-----Уровень сахара меньше 120"
    print "Здоровые = ",Probability_YS_Smaller_Z
    print "Больные = ",Probability_YS_Smaller_B
    print "-----Уровень сахара больше 120"
    print "Здоровые = ",Probability_YS_Bigger_Z
    print "Больные = ",Probability_YS_Bigger_B

    #Таблица Байесовских вероятностей
    V_YS_1 = 0
    V_YS_2 = 0
    V_YS_3 = 0
    V_YS_4 = 0

    #Вероятность, что здоров ,если уровень сахара меньше 120
    V_YS_1 = float(Probability_healthy)*Probability_YS_Smaller_Z/float(Probability_YS_Smaller)
    #Вероятность, что болен,если уровень сахара меньше 120
    V_YS_2 = float(Probability_sick)*Probability_YS_Smaller_B/float(Probability_YS_Smaller)

    #Вероятность, что здоров ,если уровень сахара больше 120
    V_YS_3 = float(Probability_healthy)*Probability_YS_Bigger_Z/float(Probability_YS_Bigger)
    #Вероятность, что болен,если уровень сахара больше 120
    V_YS_4 = float(Probability_sick)*Probability_YS_Bigger_B/float(Probability_YS_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что уровень сахара меньше 120 + здоров  =",V_YS_1
    print "Вероятность, что уровень сахара меньше 120 + болен =",V_YS_2
    print "Вероятность, что уровень сахара больше 120 + здоров  =",V_YS_3
    print "Вероятность, что уровень сахара больше 120 + здоров =",V_YS_4
    print "----------------------------------------------"



    #Параметр №7 результаты кардиограммы в состоянии покоя (values 0,1,2)
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №7 результаты кардиограммы в состоянии покоя -------"
    Summa_Card = 0
    for d in range(len(List_Card)):
        Summa_Card = Summa_Card + List_Card[d]
    Middle_Card = Summa_Card/float(len(List_Card))
    print "-------Средние результаты кардиограммы=",Middle_Card

    # Подсчитаем  Количество пациентов, у которых результаты кардиограммы больше среднего
    # Подсчитаем  Количество пациентов, у которых результаты кардиограммы меньше среднего
    amount_Card_Bigger = 0
    amount_Card_Smaller = 0

    for d in range(len(List_Card)):
        if float(List_Card[d])>=Middle_Card:
            amount_Card_Bigger =amount_Card_Bigger +1
        if float(List_Card[d])<Middle_Card:
            amount_Card_Smaller =amount_Card_Smaller +1
    print "Количество пациентов, которые имеют результаты кардиограммы больше среднего =",amount_Card_Bigger
    print "Количество пациентов, которые имеют результаты кардиограммы меньше среднего =",amount_Card_Smaller

    # Определим вероятности, что у пациента результаты кардиограммы больше или меньше
    Probability_Card_Bigger = amount_Card_Bigger/float(number_patients)
    Probability_Card_Smaller = amount_Card_Smaller/float(number_patients)

    print "Вероятность, что у пациентов результаты кардиограммы больше среднего =",Probability_Card_Bigger
    print "Вероятность, что у пациентов результаты кардиограммы меньше среднего=",Probability_Card_Smaller

    amount_Card_Smaller_Z = 0
    amount_Card_Smaller_B = 0
    amount_Card_Bigger_Z = 0
    amount_Card_Bigger_B = 0

    Probability_Card_Smaller_Z = 0
    Probability_Card_Smaller_B = 0
    Probability_Card_Bigger_Z = 0
    Probability_Card_Bigger_B = 0

    for d in range(len(List_Card)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_Card[d])<Middle_Card)and (int(List_Rez[d])== 1):
            amount_Card_Smaller_Z = amount_Card_Smaller_Z+1
        if (float(List_Card[d])<Middle_Card)and (int(List_Rez[d])== 2):
            amount_Card_Smaller_B = amount_Card_Smaller_B+1
        #  старшие
        if (float(List_Card[d])>=Middle_Card)and (int(List_Rez[d])== 1):
            amount_Card_Bigger_Z = amount_Card_Bigger_Z+1
        if (float(List_Card[d])>=Middle_Card)and (int(List_Rez[d])== 2):
            amount_Card_Bigger_B = amount_Card_Bigger_B+1

    Probability_Card_Smaller_Z = amount_Card_Smaller_Z/float(number_healthy)
    Probability_Card_Smaller_B = amount_Card_Smaller_B/float(number_sick)

    Probability_Card_Bigger_Z = amount_Card_Bigger_Z/float(number_healthy)
    Probability_Card_Bigger_B = amount_Card_Bigger_B/float(number_sick)

    print "-----Результаты кардиограммы меньше среднего уровня"
    print "Здоровые = ",Probability_Card_Smaller_Z
    print "Больные = ",Probability_Card_Smaller_B
    print "-----Результаты кардиограммы больше среднего уровня"
    print "Здоровые = ",Probability_Card_Bigger_Z
    print "Больные = ",Probability_Card_Bigger_B

    #Таблица Байесовских вероятностей
    V_Card_1 = 0
    V_Card_2 = 0
    V_Card_3 = 0
    V_Card_4 = 0

    #Вероятность, что Результаты кардиограммы меньше среднего уровня + здоров
    V_Card_1 = float(Probability_healthy)*Probability_Card_Smaller_Z/float(Probability_Card_Smaller)
    #Вероятность, что Результаты кардиограммы меньше среднего уровня + болен
    V_Card_2 = float(Probability_sick)*Probability_Card_Smaller_B/float(Probability_Card_Smaller)

    #Вероятность, что Результаты кардиограммы больше среднего уровня + здоров
    V_Card_3 = float(Probability_healthy)*Probability_Card_Bigger_Z/float(Probability_Card_Bigger)
    #Вероятность, что Результаты кардиограммы больше среднего уровня + болен
    V_Card_4 = float(Probability_sick)*Probability_Card_Bigger_B/float(Probability_Card_Bigger)


    print "----------------------------------------------"
    print "Вероятность, что Результаты кардиограммы меньше среднего уровня + здоров =",V_Card_1
    print "Вероятность, что Результаты кардиограммы меньше среднего уровня + болен =",V_Card_2
    print "Вероятность, что Результаты кардиограммы больше среднего уровня + здоров =",V_Card_3
    print "Вероятность, что Результаты кардиограммы больше среднего уровня + болен =",V_Card_4
    print "----------------------------------------------"

    #Параметр №8 максимальная величина пульса

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №8 Максимальная величина пульса -------"
    Summa_MaxP = 0
    for d in range(len(List_MaxP)):
        Summa_MaxP = Summa_MaxP + List_MaxP[d]
    Middle_MaxP = Summa_MaxP/float(len(List_MaxP))
    print "-------Среднее значение максимальной величины пульса =",Middle_MaxP

    # Подсчитаем  Количество пациентов, у которых максимальная величина пульса меньше среднестатистической
    # Подсчитаем  Количество пациентов, у которых максимальная величина пульса больше среднестатистической
    amount_MaxP_Bigger = 0
    amount_MaxP_Smaller = 0

    for d in range(len(List_MaxP)):
        if float(List_MaxP[d])>=Middle_MaxP:
            amount_MaxP_Bigger =amount_MaxP_Bigger +1
        if float(List_MaxP[d])<Middle_MaxP:
            amount_MaxP_Smaller =amount_MaxP_Smaller +1
    print "Количество пациентов, у которых максимальная величина пульса меньше среднестатистической =",amount_MaxP_Bigger
    print "Количество пациентов, у которых максимальная величина пульса больше среднестатистической=",amount_MaxP_Smaller

    # Определим вероятности, что у пациента характер болей больше или меньше
    Probability_MaxP_Bigger = amount_MaxP_Bigger/float(number_patients)
    Probability_MaxP_Smaller = amount_MaxP_Smaller/float(number_patients)

    print "Вероятность, что у пациентов максимальная величина пульса больше среднестатистической =",Probability_MaxP_Bigger
    print "Вероятность, что у пациентов максимальная величина пульса меньше среднестатистической =",Probability_MaxP_Smaller

    amount_MaxP_Smaller_Z = 0
    amount_MaxP_Smaller_B = 0
    amount_MaxP_Bigger_Z = 0
    amount_MaxP_Bigger_B = 0

    Probability_MaxP_Smaller_Z = 0
    Probability_MaxP_Smaller_B = 0
    Probability_MaxP_Bigger_Z = 0
    Probability_MaxP_Bigger_B = 0

    for d in range(len(List_MaxP)):
        # младшие
        if (float(List_MaxP[d])<Middle_MaxP)and (int(List_Rez[d])== 1):
            amount_MaxP_Smaller_Z = amount_MaxP_Smaller_Z+1
        if (float(List_MaxP[d])<Middle_MaxP)and (int(List_Rez[d])== 2):
            amount_MaxP_Smaller_B = amount_MaxP_Smaller_B+1
        #  старшие
        if (float(List_MaxP[d])>=Middle_MaxP)and (int(List_Rez[d])== 1):
            amount_MaxP_Bigger_Z = amount_MaxP_Bigger_Z+1
        if (float(List_MaxP[d])>=Middle_MaxP)and (int(List_Rez[d])== 2):
            amount_MaxP_Bigger_B = amount_MaxP_Bigger_B+1

    Probability_MaxP_Smaller_Z = amount_MaxP_Smaller_Z/float(number_healthy)
    Probability_MaxP_Smaller_B = amount_MaxP_Smaller_B/float(number_sick)

    Probability_MaxP_Bigger_Z = amount_MaxP_Bigger_Z/float(number_healthy)
    Probability_MaxP_Bigger_B = amount_MaxP_Bigger_B/float(number_sick)

    print "-----Максимальная величина пульса меньше среднестатистической"
    print "Здоровые = ",Probability_MaxP_Smaller_Z
    print "Больные = ",Probability_MaxP_Smaller_B
    print "-----Максимальная величина пульса больше среднестатистической"
    print "Здоровые = ",Probability_MaxP_Bigger_Z
    print "Больные = ",Probability_MaxP_Bigger_B

    #Таблица Байесовских вероятностей
    V_MaxP_1 = 0
    V_MaxP_2 = 0
    V_MaxP_3 = 0
    V_MaxP_4 = 0

    #Вероятность, что Максимальная величина пульса меньше среднестатистической + здоров
    V_MaxP_1 = float(Probability_healthy)*Probability_MaxP_Smaller_Z/float(Probability_MaxP_Smaller)
    #Вероятность, что Максимальная величина пульса меньше среднестатистической + болен
    V_MaxP_2 = float(Probability_sick)*Probability_MaxP_Smaller_B/float(Probability_MaxP_Smaller)

    #Вероятность, что Максимальная величина пульса больше среднестатистической + здоров
    V_MaxP_3 = float(Probability_healthy)*Probability_MaxP_Bigger_Z/float(Probability_MaxP_Bigger)
    #Вероятность, что Максимальная величина пульса больше среднестатистической + болен
    V_MaxP_4 = float(Probability_sick)*Probability_MaxP_Bigger_B/float(Probability_MaxP_Bigger)


    print "----------------------------------------------"
    print "Вероятность, что Максимальная величина пульса меньше среднестатистической + здоров =",V_MaxP_1
    print "Вероятность, что Максимальная величина пульса меньше среднестатистической + болен =",V_MaxP_2
    print "Вероятность, что Максимальная величина пульса больше среднестатистической + здоров =",V_MaxP_3
    print "Вероятность, что Максимальная величина пульса больше среднестатистической + болен =",V_MaxP_4

    #Параметр №9 наличие стенокардии в анамнезе
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №9 наличие стенокардии в анамнезе -------"
    # Подсчитаем  Количество пациентов, у которых нет стенокардии в анамнезе
    # Подсчитаем  Количество пациентов, у которых есть стенокардия в анамнезе
    amount_Sten_Myj = 0
    amount_Sten_Jen = 0
    d=0
    for d in range(len(List_Sten)):
        if float(List_Sten[d])==0.0:
            amount_Sten_Myj =amount_Sten_Myj +1
        if float(List_Sten[d])==1.0:
            amount_Sten_Jen =amount_Sten_Jen +1
    print "Количество пациентов, у которых нет стенокардии в анамнезе =",amount_Sten_Myj
    print "Количество пациентов, у которых есть стенокардия в анамнезе =",amount_Sten_Jen
    # Определим вероятности, что есть ли стенокардия
    Probability_Sten_Myj = amount_Sten_Myj/float(number_patients)
    Probability_Sten_Jen = amount_Sten_Jen/float(number_patients)

    print "Вероятность пациентов, у которых есть стенокардия в анамнезе =",Probability_Sten_Myj
    print "Вероятность пациентов, у которых нет стенокардии в анамнезе =",Probability_Sten_Jen

    amount_Sten_Myj_Z = 0
    amount_Sten_Myj_B = 0
    amount_Sten_Jen_Z = 0
    amount_Sten_Jen_B = 0

    Probability_Sten_Myj_Z = 0
    Probability_Sten_Myj_B = 0
    Probability_Sten_Jen_Z = 0
    Probability_Sten_Jen_B = 0

    for d in range(len(List_Sten)):
        # есть
        if (float(List_Sten[d])==0.0)and (int(List_Rez[d])== 1):
            amount_Sten_Myj_Z = amount_Sten_Myj_Z+1
        if (float(List_Sten[d])==0.0)and (int(List_Rez[d])== 2):
            amount_Sten_Myj_B = amount_Sten_Myj_B+1
        #  нет
        if (float(List_Sten[d])==1.0)and (int(List_Rez[d])== 1):
            amount_Sten_Jen_Z = amount_Sten_Jen_Z + 1
        if (float(List_Sten[d])==1.0)and (int(List_Rez[d])== 2):
            amount_Sten_Jen_B = amount_Sten_Jen_B+1

    Probability_Sten_Myj_Z = amount_Sten_Myj_Z/float(number_healthy)
    Probability_Sten_Myj_B = amount_Sten_Myj_B/float(number_sick)
    Probability_Sten_Jen_Z = amount_Sten_Jen_Z/float(number_healthy)
    Probability_Sten_Jen_B = amount_Sten_Jen_B/float(number_sick)

    print "-----есть стенокардия в анамнезе"
    print "Здоровые = ",Probability_Sten_Myj_Z
    print "Больные = ",Probability_Sten_Myj_B
    print "-----нет стенокардии в анамнезе"
    print "Здоровые = ",Probability_Sten_Jen_Z
    print "Больные = ",Probability_Sten_Jen_B

    #Таблица Байесовских вероятностей
    V_Sten_1 = 0
    V_Sten_2 = 0
    V_Sten_3 = 0
    V_Sten_4 = 0

    #Вероятность, что есть стенокардия в анамнезе + здоров
    V_Sten_1 = float(Probability_healthy)*Probability_Sten_Myj_Z/float(Probability_Sten_Myj)
    #Вероятность, что есть стенокардия в анамнезе + болен
    V_Sten_2 = float(Probability_sick)*Probability_Sten_Myj_B/float(Probability_Sten_Myj)

    #Вероятность, что нет стенокардии в анамнезе + здоров
    V_Sten_3 = float(Probability_healthy)*Probability_Sten_Jen_Z/float(Probability_Sten_Jen)
    #Вероятность, что нет стенокардии в анамнезе + болен
    V_Sten_4 = float(Probability_sick)*Probability_Sten_Jen_B/float(Probability_Sten_Jen)

    print "----------------------------------------------"
    print "Вероятность, что есть стенокардия в анамнезе + здоров =",V_Sten_1
    print "Вероятность, что есть стенокардия в анамнезе + болен =",V_Sten_2
    print "Вероятность, что нет стенокардии в анамнезе + здоров =",V_Sten_3
    print "Вероятность, что нет стенокардии в анамнезе + болен =",V_Sten_4
    print "----------------------------------------------"

    #Параметр №10 данные степ-теста
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №10 данные степ-теста -------"
    Summa_StepTest = 0
    for d in range(len(List_StepTest)):
        Summa_StepTest = Summa_StepTest + List_StepTest[d]
    Middle_StepTest = Summa_StepTest/float(len(List_StepTest))
    print "-------Средние данные степ-теста =",Middle_StepTest

    # Подсчитаем  Количество пациентов, у которых данные степ-теста больше среднего
    # Подсчитаем  Количество пациентов, у которых данные степ-теста меньше среднего
    amount_StepTest_Bigger = 0
    amount_StepTest_Smaller = 0
    for d in range(len(List_StepTest)):
        if float(List_StepTest[d])>=Middle_StepTest:
            amount_StepTest_Bigger =amount_StepTest_Bigger +1
        if float(List_StepTest[d])<Middle_StepTest:
            amount_StepTest_Smaller =amount_StepTest_Smaller +1
    print "Количество пациентов, у которых данные степ-теста больше среднего =",amount_StepTest_Bigger
    print "Количество пациентов, у которых данные степ-теста меньше среднего =",amount_StepTest_Smaller

    # Определим вероятности, что данные больше или меньше
    Probability_StepTest_Bigger = amount_StepTest_Bigger/float(number_patients)
    Probability_StepTest_Smaller = amount_StepTest_Smaller/float(number_patients)

    print "Вероятность данные больше =",Probability_StepTest_Bigger
    print "Вероятность данные меньше=",Probability_StepTest_Smaller

    amount_StepTest_Smaller_Z = 0
    amount_StepTest_Smaller_B = 0
    amount_StepTest_Bigger_Z = 0
    amount_StepTest_Bigger_B = 0

    Probability_StepTest_Smaller_Z = 0
    Probability_StepTest_Smaller_B = 0
    Probability_StepTest_Bigger_Z = 0
    Probability_StepTest_Bigger_B = 0
    for d in range(len(List_StepTest)):
        #меньше
        if (float(List_StepTest[d])<Middle_StepTest)and (int(List_Rez[d])== 1):
            amount_StepTest_Smaller_Z = amount_StepTest_Smaller_Z+1
        if (float(List_StepTest[d])<Middle_StepTest)and (int(List_Rez[d])== 2):
            amount_StepTest_Smaller_B = amount_StepTest_Smaller_B+1
        #  больше
        if (float(List_StepTest[d])>=Middle_StepTest)and (int(List_Rez[d])== 1):
            amount_StepTest_Bigger_Z = amount_StepTest_Bigger_Z+1
        if (float(List_StepTest[d])>=Middle_StepTest)and (int(List_Rez[d])== 2):
            amount_StepTest_Bigger_B = amount_StepTest_Bigger_B+1


    Probability_StepTest_Smaller_Z = amount_StepTest_Smaller_Z/float(number_healthy)
    Probability_StepTest_Smaller_B = amount_StepTest_Smaller_B/float(number_sick)

    Probability_StepTest_Bigger_Z = amount_StepTest_Bigger_Z/float(number_healthy)
    Probability_StepTest_Bigger_B = amount_StepTest_Bigger_B/float(number_sick)

    print "-----меньше"
    print "Здоровые = ",Probability_StepTest_Smaller_Z
    print "Больные = ",Probability_StepTest_Smaller_B
    print "-----больше"
    print "Здоровые = ",Probability_StepTest_Bigger_Z
    print "Больные = ",Probability_StepTest_Bigger_B

    #Таблица Баесовских вероятностей
    V_StepTest_1 = 0
    V_StepTest_2 = 0
    V_StepTest_3 = 0
    V_StepTest_4 = 0

    #Вероятность, что здоров ,если данные меньше
    V_StepTest_1 = float(Probability_healthy)*Probability_StepTest_Smaller_Z/float(Probability_StepTest_Smaller)
    #Вероятность, что болен, если данные меньше
    V_StepTest_2 = float(Probability_sick)*Probability_StepTest_Smaller_B/float(Probability_StepTest_Smaller)

    #Вероятность, что здоров, если данные больше
    V_StepTest_3 = float(Probability_healthy)*Probability_StepTest_Bigger_Z/float(Probability_StepTest_Bigger)
    #Вероятность, что болен, если данные больше
    V_StepTest_4 = float(Probability_sick)*Probability_StepTest_Bigger_B/float(Probability_StepTest_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что данные меньше + здоров =",V_StepTest_1
    print "Вероятность, что данные меньше + болен =",V_StepTest_2
    print "Вероятность, что данные больше + здоров =",V_StepTest_3
    print "Вероятность, что данные больше + болен =",V_StepTest_4
    print "----------------------------------------------"

    #Параметр №11 склонение данных по степ-тесту
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №11 склонение данных по степ-тесту -------"

    Summa_Sklon = 0
    for d in range(len(List_Sklon)):
        Summa_Sklon = Summa_Sklon + List_Sklon[d]
    Middle_Sklon = Summa_Sklon/float(len(List_Sklon))
    print "-------Среднее склонение данных =",Middle_Sklon

    # Подсчитаем  Количество пациентов, у которых данные больше Среднего склонения
    # Подсчитаем  Количество пациентов, у которых данные меньше Среднего склонения
    amount_Sklon_Bigger = 0
    amount_Sklon_Smaller = 0
    for d in range(len(List_Sklon)):
        if float(List_Sklon[d])>=Middle_Sklon:
            amount_Sklon_Bigger =amount_Sklon_Bigger +1
        if float(List_Sklon[d])<Middle_Sklon:
            amount_Sklon_Smaller =amount_Sklon_Smaller +1
    print "Количество пациентов, у которых данные больше Среднего склонения =",amount_Sklon_Bigger
    print "Количество пациентов, у которых данные меньше Среднего склонения =",amount_Sklon_Smaller

    # Определим вероятности, что пациент младше или старше
    Probability_Sklon_Bigger = amount_Sklon_Bigger/float(number_patients)
    Probability_Sklon_Smaller = amount_Sklon_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых данные больше Среднего склонения  =",Probability_Sklon_Bigger
    print "Вероятность пациентов, у которых данные меньше Среднего склонения =",Probability_Sklon_Smaller

    amount_Sklon_Smaller_Z = 0
    amount_Sklon_Smaller_B = 0
    amount_Sklon_Bigger_Z = 0
    amount_Sklon_Bigger_B = 0

    Probability_Sklon_Smaller_Z = 0
    Probability_Sklon_Smaller_B = 0
    Probability_Sklon_Bigger_Z = 0
    Probability_Sklon_Bigger_B = 0
    for d in range(len(List_Sklon)):
        # меньше
        if (float(List_Sklon[d])<Middle_Sklon)and (int(List_Rez[d])== 1):
            amount_Sklon_Smaller_Z = amount_Sklon_Smaller_Z+1
        if (float(List_Sklon[d])<Middle_Sklon)and (int(List_Rez[d])== 2):
            amount_Sklon_Smaller_B = amount_Sklon_Smaller_B+1
        #  больше
        if (float(List_Sklon[d])>=Middle_Sklon)and (int(List_Rez[d])== 1):
            amount_Sklon_Bigger_Z = amount_Sklon_Bigger_Z+1
        if (float(List_Sklon[d])>=Middle_Sklon)and (int(List_Rez[d])== 2):
            amount_Sklon_Bigger_B = amount_Sklon_Bigger_B+1


    Probability_Sklon_Smaller_Z = amount_Sklon_Smaller_Z/float(number_healthy)
    Probability_Sklon_Smaller_B = amount_Sklon_Smaller_B/float(number_sick)

    Probability_Sklon_Bigger_Z = amount_Sklon_Bigger_Z/float(number_healthy)
    Probability_Sklon_Bigger_B = amount_Sklon_Bigger_B/float(number_sick)

    print "-----данные меньше"
    print "Здоровые = ",Probability_Sklon_Smaller_Z
    print "Больные = ",Probability_Sklon_Smaller_B
    print "-----данные больше"
    print "Здоровые = ",Probability_Sklon_Bigger_Z
    print "Больные = ",Probability_Sklon_Bigger_B

    #Таблица Баесовских вероятностей
    V_Sklon_1 = 0
    V_Sklon_2 = 0
    V_Sklon_3 = 0
    V_Sklon_4 = 0

    #Вероятность, что данные меньше + здоров
    V_Sklon_1 = float(Probability_healthy)*Probability_Sklon_Smaller_Z/float(Probability_Sklon_Smaller)

    #Вероятность, что данные меньше + болен
    V_Sklon_2 = float(Probability_sick)*Probability_Sklon_Smaller_B/float(Probability_Sklon_Smaller)

    #Вероятность, что данные больше + здоров
    V_Sklon_3 = float(Probability_healthy)*Probability_Sklon_Bigger_Z/float(Probability_Sklon_Bigger)
    #Вероятность, что данные больше + болен
    V_Sklon_4 = float(Probability_sick)*Probability_Sklon_Bigger_B/float(Probability_Sklon_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что данные меньше + здоров =",V_Sklon_1
    print "Вероятность, что данные меньше + болен =",V_Sklon_2
    print "Вероятность, что данные больше + здоров =",V_Sklon_3
    print "Вероятность, что данные больше + болен =",V_Sklon_4
    print "----------------------------------------------"


    #Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопией
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопие -------"

    Summa_Sosyd = 0
    for d in range(len(List_Sosyd)):
        Summa_Sosyd = Summa_Sosyd + List_Sosyd[d]
    Middle_Sosyd = Summa_Sosyd/float(len(List_Sosyd))
    print "-------Среднее количество основных сосудов =",Middle_Sosyd

    # Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего
    # Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего
    amount_Sosyd_Bigger = 0
    amount_Sosyd_Smaller = 0
    for d in range(len(List_Sosyd)):
        if float(List_Sosyd[d])>=Middle_Sosyd:
            amount_Sosyd_Bigger =amount_Sosyd_Bigger +1
        if float(List_Sosyd[d])<Middle_Sosyd:
            amount_Sosyd_Smaller =amount_Sosyd_Smaller +1
    print "Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего =",amount_Sosyd_Bigger
    print "Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего  =",amount_Sosyd_Smaller

    # Определим вероятности, что пациент младше или старше
    Probability_Sosyd_Bigger = amount_Sosyd_Bigger/float(number_patients)
    Probability_Sosyd_Smaller = amount_Sosyd_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых количество основных сосудов больше Среднего =",Probability_Sosyd_Bigger
    print "Вероятность пациентов, у которых количество основных сосудов меньше Среднего =",Probability_Sosyd_Smaller

    amount_Sosyd_Smaller_Z = 0
    amount_Sosyd_Smaller_B = 0
    amount_Sosyd_Bigger_Z = 0
    amount_Sosyd_Bigger_B = 0

    Probability_Sosyd_Smaller_Z = 0
    Probability_Sosyd_Smaller_B = 0
    Probability_Sosyd_Bigger_Z = 0
    Probability_Sosyd_Bigger_B = 0
    for d in range(len(List_Sosyd)):
        # меньше
        if (float(List_Sosyd[d])<Middle_Sosyd)and (int(List_Rez[d])== 1):
            amount_Sosyd_Smaller_Z = amount_Sosyd_Smaller_Z+1
        if (float(List_Sosyd[d])<Middle_Sosyd)and (int(List_Rez[d])== 2):
            amount_Sosyd_Smaller_B = amount_Sosyd_Smaller_B+1
        #  больше
        if (float(List_Sosyd[d])>=Middle_Sosyd)and (int(List_Rez[d])== 1):
            amount_Sosyd_Bigger_Z = amount_Sosyd_Bigger_Z+1
        if (float(List_Sosyd[d])>=Middle_Sosyd)and (int(List_Rez[d])== 2):
            amount_Sosyd_Bigger_B = amount_Sosyd_Bigger_B+1


    Probability_Sosyd_Smaller_Z = amount_Sosyd_Smaller_Z/float(number_healthy)
    Probability_Sosyd_Smaller_B = amount_Sosyd_Smaller_B/float(number_sick)

    Probability_Sosyd_Bigger_Z = amount_Sosyd_Bigger_Z/float(number_healthy)
    Probability_Sosyd_Bigger_B = amount_Sosyd_Bigger_B/float(number_sick)

    print "-----количество основных сосудов меньше Среднего"
    print "Здоровые = ",Probability_Sosyd_Smaller_Z
    print "Больные = ",Probability_Sosyd_Smaller_B
    print "-----количество основных сосудов больше Среднего"
    print "Здоровые = ",Probability_Sosyd_Bigger_Z
    print "Больные = ",Probability_Sosyd_Bigger_B

    #Таблица Баесовских вероятностей
    V_Sosyd_1 = 0
    V_Sosyd_2 = 0
    V_Sosyd_3 = 0
    V_Sosyd_4 = 0

    #Вероятность, что количество основных сосудов меньше Среднего + здоров
    V_Sosyd_1 = float(Probability_healthy)*Probability_Sosyd_Smaller_Z/float(Probability_Sosyd_Smaller)
    #Вероятность, что количество основных сосудов меньше Среднего + болен
    V_Sosyd_2 = float(Probability_sick)*Probability_Sosyd_Smaller_B/float(Probability_Sosyd_Smaller)

    #Вероятность, что количество основных сосудов больше Среднего + здоров
    V_Sosyd_3 = float(Probability_healthy)*Probability_Sosyd_Bigger_Z/float(Probability_Sosyd_Bigger)
    #Вероятность, что количество основных сосудов больше Среднего + болен
    V_Sosyd_4 = float(Probability_sick)*Probability_Sosyd_Bigger_B/float(Probability_Sosyd_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что количество основных сосудов меньше Среднего + здоров =",V_Sosyd_1
    print "Вероятность, что количество основных сосудов меньше Среднего + болен =",V_Sosyd_2
    print "Вероятность, что количество основных сосудов больше Среднего + здоров =",V_Sosyd_3
    print "Вероятность, что количество основных сосудов больше Среднего + болен =",V_Sosyd_4
    print "----------------------------------------------"

    #Параметр №13 степень повреждения сосудов
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №13 степень повреждения сосудов -------"

    Summa_SPS = 0
    for d in range(len(List_SPS)):
        Summa_SPS = Summa_SPS + List_SPS[d]
    Middle_SPS = Summa_SPS/float(len(List_SPS))
    print "-------Средняя степень повреждения сосудов =",Middle_SPS

    # Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  больше Среднего
    # Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  меньше Среднего
    amount_SPS_Bigger = 0
    amount_SPS_Smaller = 0
    for d in range(len(List_SPS)):
        if float(List_SPS[d])>=Middle_SPS:
            amount_SPS_Bigger =amount_SPS_Bigger +1
        if float(List_SPS[d])<Middle_SPS:
            amount_SPS_Smaller =amount_SPS_Smaller +1
    print "Количество пациентов, у которых степень повреждения сосудов  больше Среднего =",amount_SPS_Bigger
    print "Количество пациентов, у которых степень повреждения сосудов  меньше Среднего =",amount_SPS_Smaller

    # Определим вероятности, что степень повреждения сосудов меньше или больше
    Probability_SPS_Bigger = amount_SPS_Bigger/float(number_patients)
    Probability_SPS_Smaller = amount_SPS_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых степень повреждения сосудов  больше Среднего  =",Probability_SPS_Bigger
    print "Вероятность пациентов, у которых степень повреждения сосудов  меньше Среднего =",Probability_SPS_Smaller

    amount_SPS_Smaller_Z = 0
    amount_SPS_Smaller_B = 0
    amount_SPS_Bigger_Z = 0
    amount_SPS_Bigger_B = 0

    Probability_SPS_Smaller_Z = 0
    Probability_SPS_Smaller_B = 0
    Probability_SPS_Bigger_Z = 0
    Probability_SPS_Bigger_B = 0
    for d in range(len(List_SPS)):
        # меньше
        if (float(List_SPS[d])<Middle_SPS)and (int(List_Rez[d])== 1):
            amount_SPS_Smaller_Z = amount_SPS_Smaller_Z+1
        if (float(List_SPS[d])<Middle_SPS)and (int(List_Rez[d])== 2):
            amount_SPS_Smaller_B = amount_SPS_Smaller_B+1
        #  больше
        if (float(List_SPS[d])>=Middle_SPS)and (int(List_Rez[d])== 1):
            amount_SPS_Bigger_Z = amount_SPS_Bigger_Z+1
        if (float(List_SPS[d])>=Middle_SPS)and (int(List_Rez[d])== 2):
            amount_SPS_Bigger_B = amount_SPS_Bigger_B+1


    Probability_SPS_Smaller_Z = amount_SPS_Smaller_Z/float(number_healthy)
    Probability_SPS_Smaller_B = amount_SPS_Smaller_B/float(number_sick)

    Probability_SPS_Bigger_Z = amount_SPS_Bigger_Z/float(number_healthy)
    Probability_SPS_Bigger_B = amount_SPS_Bigger_B/float(number_sick)

    print "-----степень повреждения сосудов  меньше"
    print "Здоровые = ",Probability_SPS_Smaller_Z
    print "Больные = ",Probability_SPS_Smaller_B
    print "-----степень повреждения сосудов больше"
    print "Здоровые = ",Probability_SPS_Bigger_Z
    print "Больные = ",Probability_SPS_Bigger_B

    #Таблица Баесовских вероятностей
    V_SPS_1 = 0
    V_SPS_2 = 0
    V_SPS_3 = 0
    V_SPS_4 = 0

    #Вероятность, что степень повреждения сосудов  меньше + здоров
    V_SPS_1 = float(Probability_healthy)*Probability_SPS_Smaller_Z/float(Probability_SPS_Smaller)
    #Вероятность, что степень повреждения сосудов  меньше + болен
    V_SPS_2 = float(Probability_sick)*Probability_SPS_Smaller_B/float(Probability_SPS_Smaller)

    #Вероятность, что степень повреждения сосудов больше + здоров
    V_SPS_3 = float(Probability_healthy)*Probability_SPS_Bigger_Z/float(Probability_SPS_Bigger)
    #Вероятность, что степень повреждения сосудов больше + болен
    V_SPS_4 = float(Probability_sick)*Probability_SPS_Bigger_B/float(Probability_SPS_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что степень повреждения сосудов меньше + здоров =",V_SPS_1
    print "Вероятность, что степень повреждения сосудов меньше + болен=",V_SPS_2
    print "Вероятность, что степень повреждения сосудов больше + здоров =",V_SPS_3
    print "Вероятность, что степень повреждения сосудов больше + болен =",V_SPS_4
    print "----------------------------------------------"


