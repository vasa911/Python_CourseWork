# -*- coding: cp1251 -*-
#«Байесовский классификатор»
def Baes_classifier(number_sick,number_healthy,Probability_sick,Probability_healthy,List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_SPS,List_Rez):
    #List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,
    number_patients = len(List_Rez)
    print "-----------------------«Байесовский классификатор»-----------------------"
    
    #ПАРАМЕТР №1 - ВОЗРАСТ
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №1 Возраст-------"
    Symm_Age = 0
    for d in range(len(List_Age)):
        Symm_Age = Symm_Age + List_Age[d]
    Middle_Age = Symm_Age/float(len(List_Age))
    print "-------Средний возраст =",Middle_Age," лет"

    # Подсчитаем  Количество пациентов, которые старше среднего возраста 
    # Подсчитаем  Количество пациентов, которые младше среднего возраста
    kol_Age_Bigger = 0
    kol_Age_Smaller = 0
    for d in range(len(List_Age)):
        if float(List_Age[d])>=Middle_Age:
            kol_Age_Bigger =kol_Age_Bigger +1
        if float(List_Age[d])<Middle_Age:
            kol_Age_Smaller =kol_Age_Smaller +1
    print "Количество пациентов, которые старше среднего возраста =",kol_Age_Bigger
    print "Количество пациентов, которые младше среднего возраста =",kol_Age_Smaller

    # Определим вероятности, что пациент младше или старше
    Ver_Age_Bigger = kol_Age_Bigger/float(number_patients)
    Ver_Age_Smaller = kol_Age_Smaller/float(number_patients)

    print "Вероятность старших пациентов =",Ver_Age_Bigger    
    print "Вероятность младших пациентов=",Ver_Age_Smaller
    kol_Age_Smaller_Z = 0 
    kol_Age_Smaller_B = 0
    kol_Age_Bigger_Z = 0
    kol_Age_Bigger_B = 0

    Ver_Age_Smaller_Z = 0 
    Ver_Age_Smaller_B = 0
    Ver_Age_Bigger_Z = 0
    Ver_Age_Bigger_B = 0
    for d in range(len(List_Age)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_Age[d])<Middle_Age)and (int(List_Rez[d])== 1):
            
            kol_Age_Smaller_Z = kol_Age_Smaller_Z+1
        if (float(List_Age[d])<Middle_Age)and (int(List_Rez[d])== 2):
            kol_Age_Smaller_B = kol_Age_Smaller_B+1
        #  старшие  
        if (float(List_Age[d])>=Middle_Age)and (int(List_Rez[d])== 1):
            kol_Age_Bigger_Z = kol_Age_Bigger_Z+1
        if (float(List_Age[d])>=Middle_Age)and (int(List_Rez[d])== 2):
            kol_Age_Bigger_B = kol_Age_Bigger_B+1


    Ver_Age_Smaller_Z = kol_Age_Smaller_Z/float(number_healthy)
    Ver_Age_Smaller_B = kol_Age_Smaller_B/float(number_sick)

    Ver_Age_Bigger_Z = kol_Age_Bigger_Z/float(number_healthy)
    Ver_Age_Bigger_B = kol_Age_Bigger_B/float(number_sick)

    print "-----младшие"
    print "Здоровые = ",Ver_Age_Smaller_Z
    print "Больные = ",Ver_Age_Smaller_B
    print "-----Старшие"
    print "Здоровые = ",Ver_Age_Bigger_Z
    print "Больные = ",Ver_Age_Bigger_B

    #Таблица Баесовских вероятностей
    V_Age_1 = 0
    V_Age_2 = 0
    V_Age_3 = 0
    V_Age_4 = 0

    #Вероятность, что здоров ,если возраст младше
    V_Age_1 = float(Probability_healthy)*Ver_Age_Smaller_Z/float(Ver_Age_Smaller)

    #Вероятность, что болен,если возраст младше
    V_Age_2 = float(Probability_sick)*Ver_Age_Smaller_B/float(Ver_Age_Smaller)
    #Вероятность, что здоров ,если возраст старше
    V_Age_3 = float(Probability_healthy)*Ver_Age_Bigger_Z/float(Ver_Age_Bigger)

    #Вероятность, что болен,если возраст старше
    V_Age_4 = float(Probability_sick)*Ver_Age_Bigger_B/float(Ver_Age_Bigger)
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
    kol_Pol_Myj = 0
    kol_Pol_Jen = 0
    d=0
    for d in range(len(List_Pol)):
        if float(List_Pol[d])==0.0:
            kol_Pol_Myj =kol_Pol_Myj +1
        if float(List_Pol[d])==1.0:
            kol_Pol_Jen =kol_Pol_Jen +1
    print "Количество пациентов-мужчин =",kol_Pol_Myj
    print "Количество пациентов-женщин =",kol_Pol_Jen
    # Определим вероятности, что пациент-мужчина или пациент-женщина
    Ver_Pol_Myj = kol_Pol_Myj/float(number_patients)
    Ver_Pol_Jen = kol_Pol_Jen/float(number_patients)

    print "Вероятность, что пациент-мужчина =",Ver_Pol_Myj    
    print "Вероятность, что пациент-женщина=",Ver_Pol_Jen

    kol_Pol_Myj_Z = 0 
    kol_Pol_Myj_B = 0
    kol_Pol_Jen_Z = 0
    kol_Pol_Jen_B = 0

    Ver_Pol_Myj_Z = 0 
    Ver_Pol_Myj_B = 0
    Ver_Pol_Jen_Z = 0
    Ver_Pol_Jen_B = 0

    for d in range(len(List_Pol)):
        # мужчины
        if (float(List_Pol[d])==0.0)and (int(List_Rez[d])== 1):       
            kol_Pol_Myj_Z = kol_Pol_Myj_Z+1
        if (float(List_Pol[d])==0.0)and (int(List_Rez[d])== 2):
            kol_Pol_Myj_B = kol_Pol_Myj_B+1
        #  женщины  
        if (float(List_Pol[d])==1.0)and (int(List_Rez[d])== 1):
            kol_Pol_Jen_Z = kol_Pol_Jen_Z + 1
        if (float(List_Pol[d])==1.0)and (int(List_Rez[d])== 2):
            kol_Pol_Jen_B = kol_Pol_Jen_B+1

    Ver_Pol_Myj_Z = kol_Pol_Myj_Z/float(number_healthy) 
    Ver_Pol_Myj_B = kol_Pol_Myj_B/float(number_sick)
    Ver_Pol_Jen_Z = kol_Pol_Jen_Z/float(number_healthy)
    Ver_Pol_Jen_B = kol_Pol_Jen_B/float(number_sick)

    print "-----пациент-мужчина"
    print "Здоровые = ",Ver_Pol_Myj_Z
    print "Больные = ",Ver_Pol_Myj_B
    print "-----пациент-женщина"
    print "Здоровые = ",Ver_Pol_Jen_Z
    print "Больные = ",Ver_Pol_Jen_B

    #Таблица Байесовских вероятностей
    V_Pol_1 = 0
    V_Pol_2 = 0
    V_Pol_3 = 0
    V_Pol_4 = 0

    #Вероятность, что пациент-мужчина + здоров
    V_Pol_1 = float(Probability_healthy)*Ver_Pol_Myj_Z/float(Ver_Pol_Myj)
    #Вероятность, что пациент-мужчина + болен
    V_Pol_2 = float(Probability_sick)*Ver_Pol_Myj_B/float(Ver_Pol_Myj)

    #Вероятность, что пациент-женщина + здоров
    V_Pol_3 = float(Probability_healthy)*Ver_Pol_Jen_Z/float(Ver_Pol_Jen)
    #Вероятность, что пациент-женщина + болен
    V_Pol_4 = float(Probability_sick)*Ver_Pol_Jen_B/float(Ver_Pol_Jen)

    print "----------------------------------------------"
    print "Вероятность, что пациент-мужчина + здоров =",V_Pol_1
    print "Вероятность, что пациент-мужчина + болен =",V_Pol_2
    print "Вероятность, что пациент-женщина + здоров =",V_Pol_3
    print "Вероятность, что пациент-женщина + болен =",V_Pol_4
    print "----------------------------------------------"


    #Параметр №4 верхняя граница давления в состоянии покоя
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    print "-------Параметр №4 Верхняя граница давления в состоянии покоя-------"
    Symm_VG = 0
    for d in range(len(List_VG)):
        Symm_VG = Symm_VG + List_VG[d]
    Middle_VG = Symm_VG/float(len(List_VG))
    print "-------Среднее значение границы давления в состоянии покоя =",Middle_VG

    # Подсчитаем  Количество пациентов с большей границей давления
    # Подсчитаем  Количество пациентов, с меньшей границей давления
    kol_VG_Smaller = 0
    kol_VG_Bigger = 0

    for d in range(len(List_VG)):
        if float(List_VG[d])>=Middle_VG:
            kol_VG_Bigger =kol_VG_Bigger +1
        if float(List_VG[d])<Middle_VG:
            kol_VG_Smaller =kol_VG_Smaller +1
    print "Количество пациентов с меньшей границей давления=",kol_VG_Smaller
    print "Количество пациентов с большей границей давления=",kol_VG_Bigger

    # Определим вероятности, что пациент младше или старше
    Ver_VG_Smaller = kol_VG_Smaller/float(number_patients)
    Ver_VG_Bigger = kol_VG_Bigger/float(number_patients)

    print "Вероятность пациентов с большей границей давления=",Ver_VG_Bigger    
    print "Вероятность пациентов с меньшей границей давления=",Ver_VG_Smaller

    kol_VG_Smaller_Z = 0 
    kol_VG_Smaller_B = 0
    kol_VG_Bigger_Z = 0
    kol_VG_Bigger_B = 0

    Ver_VG_Smaller_Z = 0 
    Ver_VG_Smaller_B = 0
    Ver_VG_Bigger_Z = 0
    Ver_VG_Bigger_B = 0
    for d in range(len(List_VG)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_VG[d])<Middle_VG)and (int(List_Rez[d])== 1):       
            kol_VG_Smaller_Z = kol_VG_Smaller_Z+1
        if (float(List_VG[d])<Middle_VG)and (int(List_Rez[d])== 2):
            kol_VG_Smaller_B = kol_VG_Smaller_B+1
        #  старшие  
        if (float(List_VG[d])>=Middle_VG)and (int(List_Rez[d])== 1):
            kol_VG_Bigger_Z = kol_VG_Bigger_Z+1
        if (float(List_VG[d])>=Middle_VG)and (int(List_Rez[d])== 2):
            kol_VG_Bigger_B = kol_VG_Bigger_B+1


    Ver_VG_Smaller_Z = kol_VG_Smaller_Z/float(number_healthy)
    Ver_VG_Smaller_B = kol_VG_Smaller_B/float(number_sick)

    Ver_VG_Bigger_Z = kol_VG_Bigger_Z/float(number_healthy)
    Ver_VG_Bigger_B = kol_VG_Bigger_B/float(number_sick)

    print "-----Граница давления меньше"
    print "Здоровые = ",Ver_VG_Smaller_Z
    print "Больные = ",Ver_VG_Smaller_B
    print "-----Граница давления больше"
    print "Здоровые = ",Ver_VG_Bigger_Z
    print "Больные = ",Ver_VG_Bigger_B

    #Таблица Баесовских вероятностей
    V_VG_1 = 0
    V_VG_2 = 0
    V_VG_3 = 0
    V_VG_4 = 0

    #Вероятность, что здоров ,если граница меньше
    V_VG_1 = float(Probability_healthy)*Ver_VG_Smaller_Z/float(Ver_VG_Smaller)

    #Вероятность, что болен,если граница меньше
    V_VG_2 = float(Probability_sick)*Ver_VG_Smaller_B/float(Ver_VG_Smaller)
    #Вероятность, что здоров ,если граница больше
    V_VG_3 = float(Probability_healthy)*Ver_VG_Bigger_Z/float(Ver_VG_Bigger)

    #Вероятность, что болен,если граница больше
    V_VG_4 = float(Probability_sick)*Ver_VG_Bigger_B/float(Ver_VG_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что Граница давления меньше + здоров =",V_VG_1
    print "Вероятность, что Граница давления меньше + болен=",V_VG_2
    print "Вероятность, что Граница давления больше + здоров =",V_VG_3
    print "Вероятность, что Граница давления больше + болен =",V_VG_4
    print "----------------------------------------------"

    #Параметр №5 уровень холестерина в крови mg/dl
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №5 уровень холестерина в крови mg/dl -------"

    Symm_YH = 0
    for d in range(len(List_YH)):
        Symm_YH = Symm_YH + List_YH[d]
    Middle_YH = Symm_YH/float(len(List_YH))
    print "-------Средний уровень холестерина в крови =",Middle_YH," mg/dl"

    # Подсчитаем  Количество пациентов, у которых уровень холестерина больше среднего
    # Подсчитаем  Количество пациентов, у которыхуровень холестерина меньше среднего
    kol_YH_Bigger = 0
    kol_YH_Smaller = 0
    for d in range(len(List_YH)):
        if float(List_YH[d])>=Middle_YH:
            kol_YH_Bigger =kol_YH_Bigger +1
        if float(List_YH[d])<Middle_YH:
            kol_YH_Smaller =kol_YH_Smaller +1
    print "Количество пациентов, у которых уровень холестерина больше среднего =",kol_YH_Bigger
    print "Количество пациентов, у которых уровень холестерина меньше среднего =",kol_YH_Smaller

    # Определим вероятности, что у пациента уровнеь больше или меньше
    Ver_YH_Bigger = kol_YH_Bigger/float(number_patients)
    Ver_YH_Smaller = kol_YH_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых уровень холестерина больше среднего=",Ver_YH_Bigger    
    print "Вероятность пациентов, у которых уровень холестерина меньше среднего=",Ver_YH_Smaller

    kol_YH_Smaller_Z = 0 
    kol_YH_Smaller_B = 0
    kol_YH_Bigger_Z = 0
    kol_YH_Bigger_B = 0

    Ver_YH_Smaller_Z = 0 
    Ver_YH_Smaller_B = 0
    Ver_YH_Bigger_Z = 0
    Ver_YH_Bigger_B = 0
    for d in range(len(List_YH)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_YH[d])<Middle_YH)and (int(List_Rez[d])== 1):       
            kol_YH_Smaller_Z = kol_YH_Smaller_Z+1
        if (float(List_YH[d])<Middle_YH)and (int(List_Rez[d])== 2):
            kol_YH_Smaller_B = kol_YH_Smaller_B+1
        #  старшие  
        if (float(List_YH[d])>=Middle_YH)and (int(List_Rez[d])== 1):
            kol_YH_Bigger_Z = kol_YH_Bigger_Z+1
        if (float(List_YH[d])>=Middle_YH)and (int(List_Rez[d])== 2):
            kol_YH_Bigger_B = kol_YH_Bigger_B+1


    Ver_YH_Smaller_Z = kol_YH_Smaller_Z/float(number_healthy)
    Ver_YH_Smaller_B = kol_YH_Smaller_B/float(number_sick)

    Ver_YH_Bigger_Z = kol_YH_Bigger_Z/float(number_healthy)
    Ver_YH_Bigger_B = kol_YH_Bigger_B/float(number_sick)

    print "-----Уровень холестерина меньше среднего"
    print "Здоровые = ",Ver_YH_Smaller_Z
    print "Больные = ",Ver_YH_Smaller_B
    print "-----Уровень холестерина больше среднего"
    print "Здоровые = ",Ver_YH_Bigger_Z
    print "Больные = ",Ver_YH_Bigger_B

    #Таблица Байесовских вероятностей
    V_YH_1 = 0
    V_YH_2 = 0
    V_YH_3 = 0
    V_YH_4 = 0

    #Вероятность, что здоров ,если уровень холестерина меньше среднего
    V_YH_1 = float(Probability_healthy)*Ver_YH_Smaller_Z/float(Ver_YH_Smaller)
    #Вероятность, что болен,если уровень холестерина меньше среднего
    V_YH_2 = float(Probability_sick)*Ver_YH_Smaller_B/float(Ver_YH_Smaller)

    #Вероятность, что здоров ,если уровень холестерина больше среднего
    V_YH_3 = float(Probability_healthy)*Ver_YH_Bigger_Z/float(Ver_YH_Bigger)
    #Вероятность, что болен,если уровень холестерина больше среднего
    V_YH_4 = float(Probability_sick)*Ver_YH_Bigger_B/float(Ver_YH_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что уровень холестерина меньше среднего + здоров  =",V_YH_1
    print "Вероятность, что уровень холестерина меньше среднего + болен =",V_YH_2
    print "Вероятность, что уровень холестерина больше среднего + здоров  =",V_YH_3
    print "Вероятность, что уровень холестерина больше среднего + здоров =",V_YH_4
    print "----------------------------------------------"


    #Параметр №6 уровень сахара в крови больший 120 mg/dl  
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №6 уровень сахара в крови больший 120 mg/dl   -------"

    Symm_YS = 0
    for d in range(len(List_YS)):
        Symm_YS = Symm_YS + List_YS[d]
    Middle_YS = Symm_YS/float(len(List_YS))
    print "-------Средний уровень сахара в крови =",Middle_YS," mg/dl"

    # Подсчитаем  Количество пациентов, у которых уровень сахара больше 120
    # Подсчитаем  Количество пациентов, у которых уровень сахара меньше 120
    kol_YS_Bigger = 0
    kol_YS_Smaller = 0
    for d in range(len(List_YS)):
        if float(List_YS[d])>=Middle_YS:
            kol_YS_Bigger =kol_YS_Bigger +1
        if float(List_YS[d])<Middle_YH:
            kol_YS_Smaller =kol_YS_Smaller +1
    print "Количество пациентов, у которых уровень сахара больше среднего =",kol_YS_Bigger
    print "Количество пациентов, у которых уровень сахара меньше среднего =",kol_YS_Smaller

    # Определим вероятности, что у пациента уровень больше или меньше
    Ver_YS_Bigger = kol_YS_Bigger/float(number_patients)
    Ver_YS_Smaller = kol_YS_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых уровень сахара больше 120=",Ver_YS_Bigger    
    print "Вероятность пациентов, у которых уровень сахара меньше 120=",Ver_YS_Smaller

    kol_YS_Smaller_Z = 0 
    kol_YS_Smaller_B = 0
    kol_YS_Bigger_Z = 0
    kol_YS_Bigger_B = 0

    Ver_YS_Smaller_Z = 0 
    Ver_YS_Smaller_B = 0
    Ver_YS_Bigger_Z = 0
    Ver_YS_Bigger_B = 0
    for d in range(len(List_YS)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_YS[d])<Middle_YS)and (int(List_Rez[d])== 1):       
            kol_YS_Smaller_Z = kol_YS_Smaller_Z+1
        if (float(List_YS[d])<Middle_YS)and (int(List_Rez[d])== 2):
            kol_YS_Smaller_B = kol_YS_Smaller_B+1
        #  старшие  
        if (float(List_YS[d])>=Middle_YS)and (int(List_Rez[d])== 1):
            kol_YS_Bigger_Z = kol_YS_Bigger_Z+1
        if (float(List_YS[d])>=Middle_YS)and (int(List_Rez[d])== 2):
            kol_YS_Bigger_B = kol_YS_Bigger_B+1


    Ver_YS_Smaller_Z = kol_YS_Smaller_Z/float(number_healthy)
    Ver_YS_Smaller_B = kol_YS_Smaller_B/float(number_sick)

    Ver_YS_Bigger_Z = kol_YS_Bigger_Z/float(number_healthy)
    Ver_YS_Bigger_B = kol_YS_Bigger_B/float(number_sick)

    print "-----Уровень сахара меньше 120"
    print "Здоровые = ",Ver_YS_Smaller_Z
    print "Больные = ",Ver_YS_Smaller_B
    print "-----Уровень сахара больше 120"
    print "Здоровые = ",Ver_YS_Bigger_Z
    print "Больные = ",Ver_YS_Bigger_B

    #Таблица Байесовских вероятностей
    V_YS_1 = 0
    V_YS_2 = 0
    V_YS_3 = 0
    V_YS_4 = 0

    #Вероятность, что здоров ,если уровень сахара меньше 120
    V_YS_1 = float(Probability_healthy)*Ver_YS_Smaller_Z/float(Ver_YS_Smaller)
    #Вероятность, что болен,если уровень сахара меньше 120
    V_YS_2 = float(Probability_sick)*Ver_YS_Smaller_B/float(Ver_YS_Smaller)

    #Вероятность, что здоров ,если уровень сахара больше 120
    V_YS_3 = float(Probability_healthy)*Ver_YS_Bigger_Z/float(Ver_YS_Bigger)
    #Вероятность, что болен,если уровень сахара больше 120
    V_YS_4 = float(Probability_sick)*Ver_YS_Bigger_B/float(Ver_YS_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что уровень сахара меньше 120 + здоров  =",V_YS_1
    print "Вероятность, что уровень сахара меньше 120 + болен =",V_YS_2
    print "Вероятность, что уровень сахара больше 120 + здоров  =",V_YS_3
    print "Вероятность, что уровень сахара больше 120 + здоров =",V_YS_4
    print "----------------------------------------------"
         


    #Параметр №7 результаты кардиограммы в состоянии покоя (values 0,1,2)
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №7 результаты кардиограммы в состоянии покоя -------"
    Symm_Card = 0
    for d in range(len(List_Card)):
        Symm_Card = Symm_Card + List_Card[d]
    Middle_Card = Symm_Card/float(len(List_Card))
    print "-------Средние результаты кардиограммы=",Middle_Card

    # Подсчитаем  Количество пациентов, у которых результаты кардиограммы больше среднего
    # Подсчитаем  Количество пациентов, у которых результаты кардиограммы меньше среднего
    kol_Card_Bigger = 0
    kol_Card_Smaller = 0

    for d in range(len(List_Card)):
        if float(List_Card[d])>=Middle_Card:
            kol_Card_Bigger =kol_Card_Bigger +1
        if float(List_Card[d])<Middle_Card:
            kol_Card_Smaller =kol_Card_Smaller +1
    print "Количество пациентов, которые имеют результаты кардиограммы больше среднего =",kol_Card_Bigger
    print "Количество пациентов, которые имеют результаты кардиограммы меньше среднего =",kol_Card_Smaller

    # Определим вероятности, что у пациента результаты кардиограммы больше или меньше
    Ver_Card_Bigger = kol_Card_Bigger/float(number_patients)
    Ver_Card_Smaller = kol_Card_Smaller/float(number_patients)

    print "Вероятность, что у пациентов результаты кардиограммы больше среднего =",Ver_Card_Bigger    
    print "Вероятность, что у пациентов результаты кардиограммы меньше среднего=",Ver_Card_Smaller

    kol_Card_Smaller_Z = 0 
    kol_Card_Smaller_B = 0
    kol_Card_Bigger_Z = 0
    kol_Card_Bigger_B = 0

    Ver_Card_Smaller_Z = 0 
    Ver_Card_Smaller_B = 0
    Ver_Card_Bigger_Z = 0
    Ver_Card_Bigger_B = 0

    for d in range(len(List_Card)):
        # младшие
        #print "Diagnoz =",List_Rez[d]
        if (float(List_Card[d])<Middle_Card)and (int(List_Rez[d])== 1):       
            kol_Card_Smaller_Z = kol_Card_Smaller_Z+1
        if (float(List_Card[d])<Middle_Card)and (int(List_Rez[d])== 2):
            kol_Card_Smaller_B = kol_Card_Smaller_B+1
        #  старшие  
        if (float(List_Card[d])>=Middle_Card)and (int(List_Rez[d])== 1):
            kol_Card_Bigger_Z = kol_Card_Bigger_Z+1
        if (float(List_Card[d])>=Middle_Card)and (int(List_Rez[d])== 2):
            kol_Card_Bigger_B = kol_Card_Bigger_B+1

    Ver_Card_Smaller_Z = kol_Card_Smaller_Z/float(number_healthy)
    Ver_Card_Smaller_B = kol_Card_Smaller_B/float(number_sick)

    Ver_Card_Bigger_Z = kol_Card_Bigger_Z/float(number_healthy)
    Ver_Card_Bigger_B = kol_Card_Bigger_B/float(number_sick)

    print "-----Результаты кардиограммы меньше среднего уровня"
    print "Здоровые = ",Ver_Card_Smaller_Z
    print "Больные = ",Ver_Card_Smaller_B
    print "-----Результаты кардиограммы больше среднего уровня"
    print "Здоровые = ",Ver_Card_Bigger_Z
    print "Больные = ",Ver_Card_Bigger_B

    #Таблица Байесовских вероятностей
    V_Card_1 = 0
    V_Card_2 = 0
    V_Card_3 = 0
    V_Card_4 = 0

    #Вероятность, что Результаты кардиограммы меньше среднего уровня + здоров 
    V_Card_1 = float(Probability_healthy)*Ver_Card_Smaller_Z/float(Ver_Card_Smaller)
    #Вероятность, что Результаты кардиограммы меньше среднего уровня + болен
    V_Card_2 = float(Probability_sick)*Ver_Card_Smaller_B/float(Ver_Card_Smaller)

    #Вероятность, что Результаты кардиограммы больше среднего уровня + здоров 
    V_Card_3 = float(Probability_healthy)*Ver_Card_Bigger_Z/float(Ver_Card_Bigger)
    #Вероятность, что Результаты кардиограммы больше среднего уровня + болен 
    V_Card_4 = float(Probability_sick)*Ver_Card_Bigger_B/float(Ver_Card_Bigger)


    print "----------------------------------------------"
    print "Вероятность, что Результаты кардиограммы меньше среднего уровня + здоров =",V_Card_1
    print "Вероятность, что Результаты кардиограммы меньше среднего уровня + болен =",V_Card_2
    print "Вероятность, что Результаты кардиограммы больше среднего уровня + здоров =",V_Card_3
    print "Вероятность, что Результаты кардиограммы больше среднего уровня + болен =",V_Card_4
    print "----------------------------------------------"

    #Параметр №8 максимальная величина пульса

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №8 Максимальная величина пульса -------"
    Symm_MaxP = 0
    for d in range(len(List_MaxP)):
        Symm_MaxP = Symm_MaxP + List_MaxP[d]
    Middle_MaxP = Symm_MaxP/float(len(List_MaxP))
    print "-------Среднее значение максимальной величины пульса =",Middle_MaxP

    # Подсчитаем  Количество пациентов, у которых максимальная величина пульса меньше среднестатистической
    # Подсчитаем  Количество пациентов, у которых максимальная величина пульса больше среднестатистической
    kol_MaxP_Bigger = 0
    kol_MaxP_Smaller = 0

    for d in range(len(List_MaxP)):
        if float(List_MaxP[d])>=Middle_MaxP:
            kol_MaxP_Bigger =kol_MaxP_Bigger +1
        if float(List_MaxP[d])<Middle_MaxP:
            kol_MaxP_Smaller =kol_MaxP_Smaller +1
    print "Количество пациентов, у которых максимальная величина пульса меньше среднестатистической =",kol_MaxP_Bigger
    print "Количество пациентов, у которых максимальная величина пульса больше среднестатистической=",kol_MaxP_Smaller

    # Определим вероятности, что у пациента характер болей больше или меньше
    Ver_MaxP_Bigger = kol_MaxP_Bigger/float(number_patients)
    Ver_MaxP_Smaller = kol_MaxP_Smaller/float(number_patients)

    print "Вероятность, что у пациентов максимальная величина пульса больше среднестатистической =",Ver_MaxP_Bigger    
    print "Вероятность, что у пациентов максимальная величина пульса меньше среднестатистической =",Ver_MaxP_Smaller

    kol_MaxP_Smaller_Z = 0 
    kol_MaxP_Smaller_B = 0
    kol_MaxP_Bigger_Z = 0
    kol_MaxP_Bigger_B = 0

    Ver_MaxP_Smaller_Z = 0 
    Ver_MaxP_Smaller_B = 0
    Ver_MaxP_Bigger_Z = 0
    Ver_MaxP_Bigger_B = 0

    for d in range(len(List_MaxP)):
        # младшие
        if (float(List_MaxP[d])<Middle_MaxP)and (int(List_Rez[d])== 1):       
            kol_MaxP_Smaller_Z = kol_MaxP_Smaller_Z+1
        if (float(List_MaxP[d])<Middle_MaxP)and (int(List_Rez[d])== 2):
            kol_MaxP_Smaller_B = kol_MaxP_Smaller_B+1
        #  старшие  
        if (float(List_MaxP[d])>=Middle_MaxP)and (int(List_Rez[d])== 1):
            kol_MaxP_Bigger_Z = kol_MaxP_Bigger_Z+1
        if (float(List_MaxP[d])>=Middle_MaxP)and (int(List_Rez[d])== 2):
            kol_MaxP_Bigger_B = kol_MaxP_Bigger_B+1

    Ver_MaxP_Smaller_Z = kol_MaxP_Smaller_Z/float(number_healthy)
    Ver_MaxP_Smaller_B = kol_MaxP_Smaller_B/float(number_sick)

    Ver_MaxP_Bigger_Z = kol_MaxP_Bigger_Z/float(number_healthy)
    Ver_MaxP_Bigger_B = kol_MaxP_Bigger_B/float(number_sick)

    print "-----Максимальная величина пульса меньше среднестатистической"
    print "Здоровые = ",Ver_MaxP_Smaller_Z
    print "Больные = ",Ver_MaxP_Smaller_B
    print "-----Максимальная величина пульса больше среднестатистической"
    print "Здоровые = ",Ver_MaxP_Bigger_Z
    print "Больные = ",Ver_MaxP_Bigger_B

    #Таблица Байесовских вероятностей
    V_MaxP_1 = 0
    V_MaxP_2 = 0
    V_MaxP_3 = 0
    V_MaxP_4 = 0

    #Вероятность, что Максимальная величина пульса меньше среднестатистической + здоров 
    V_MaxP_1 = float(Probability_healthy)*Ver_MaxP_Smaller_Z/float(Ver_MaxP_Smaller)
    #Вероятность, что Максимальная величина пульса меньше среднестатистической + болен
    V_MaxP_2 = float(Probability_sick)*Ver_MaxP_Smaller_B/float(Ver_MaxP_Smaller)

    #Вероятность, что Максимальная величина пульса больше среднестатистической + здоров 
    V_MaxP_3 = float(Probability_healthy)*Ver_MaxP_Bigger_Z/float(Ver_MaxP_Bigger)
    #Вероятность, что Максимальная величина пульса больше среднестатистической + болен 
    V_MaxP_4 = float(Probability_sick)*Ver_MaxP_Bigger_B/float(Ver_MaxP_Bigger)


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
    kol_Sten_Myj = 0
    kol_Sten_Jen = 0
    d=0
    for d in range(len(List_Sten)):
        if float(List_Sten[d])==0.0:
            kol_Sten_Myj =kol_Sten_Myj +1
        if float(List_Sten[d])==1.0:
            kol_Sten_Jen =kol_Sten_Jen +1
    print "Количество пациентов, у которых нет стенокардии в анамнезе =",kol_Sten_Myj
    print "Количество пациентов, у которых есть стенокардия в анамнезе =",kol_Sten_Jen
    # Определим вероятности, что есть ли стенокардия
    Ver_Sten_Myj = kol_Sten_Myj/float(number_patients)
    Ver_Sten_Jen = kol_Sten_Jen/float(number_patients)

    print "Вероятность пациентов, у которых есть стенокардия в анамнезе =",Ver_Sten_Myj    
    print "Вероятность пациентов, у которых нет стенокардии в анамнезе =",Ver_Sten_Jen

    kol_Sten_Myj_Z = 0 
    kol_Sten_Myj_B = 0
    kol_Sten_Jen_Z = 0
    kol_Sten_Jen_B = 0

    Ver_Sten_Myj_Z = 0 
    Ver_Sten_Myj_B = 0
    Ver_Sten_Jen_Z = 0
    Ver_Sten_Jen_B = 0

    for d in range(len(List_Sten)):
        # есть
        if (float(List_Sten[d])==0.0)and (int(List_Rez[d])== 1):       
            kol_Sten_Myj_Z = kol_Sten_Myj_Z+1
        if (float(List_Sten[d])==0.0)and (int(List_Rez[d])== 2):
            kol_Sten_Myj_B = kol_Sten_Myj_B+1
        #  нет  
        if (float(List_Sten[d])==1.0)and (int(List_Rez[d])== 1):
            kol_Sten_Jen_Z = kol_Sten_Jen_Z + 1
        if (float(List_Sten[d])==1.0)and (int(List_Rez[d])== 2):
            kol_Sten_Jen_B = kol_Sten_Jen_B+1

    Ver_Sten_Myj_Z = kol_Sten_Myj_Z/float(number_healthy) 
    Ver_Sten_Myj_B = kol_Sten_Myj_B/float(number_sick)
    Ver_Sten_Jen_Z = kol_Sten_Jen_Z/float(number_healthy)
    Ver_Sten_Jen_B = kol_Sten_Jen_B/float(number_sick)

    print "-----есть стенокардия в анамнезе"
    print "Здоровые = ",Ver_Sten_Myj_Z
    print "Больные = ",Ver_Sten_Myj_B
    print "-----нет стенокардии в анамнезе"
    print "Здоровые = ",Ver_Sten_Jen_Z
    print "Больные = ",Ver_Sten_Jen_B

    #Таблица Байесовских вероятностей
    V_Sten_1 = 0
    V_Sten_2 = 0
    V_Sten_3 = 0
    V_Sten_4 = 0

    #Вероятность, что есть стенокардия в анамнезе + здоров
    V_Sten_1 = float(Probability_healthy)*Ver_Sten_Myj_Z/float(Ver_Sten_Myj)
    #Вероятность, что есть стенокардия в анамнезе + болен
    V_Sten_2 = float(Probability_sick)*Ver_Sten_Myj_B/float(Ver_Sten_Myj)

    #Вероятность, что нет стенокардии в анамнезе + здоров
    V_Sten_3 = float(Probability_healthy)*Ver_Sten_Jen_Z/float(Ver_Sten_Jen)
    #Вероятность, что нет стенокардии в анамнезе + болен
    V_Sten_4 = float(Probability_sick)*Ver_Sten_Jen_B/float(Ver_Sten_Jen)

    print "----------------------------------------------"
    print "Вероятность, что есть стенокардия в анамнезе + здоров =",V_Sten_1
    print "Вероятность, что есть стенокардия в анамнезе + болен =",V_Sten_2
    print "Вероятность, что нет стенокардии в анамнезе + здоров =",V_Sten_3
    print "Вероятность, что нет стенокардии в анамнезе + болен =",V_Sten_4
    print "----------------------------------------------"

    #Параметр №10 данные степ-теста
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №10 данные степ-теста -------"
    Symm_StepTest = 0
    for d in range(len(List_StepTest)):
        Symm_StepTest = Symm_StepTest + List_StepTest[d]
    Middle_StepTest = Symm_StepTest/float(len(List_StepTest))
    print "-------Средние данные степ-теста =",Middle_StepTest

    # Подсчитаем  Количество пациентов, у которых данные степ-теста больше среднего
    # Подсчитаем  Количество пациентов, у которых данные степ-теста меньше среднего
    kol_StepTest_Bigger = 0
    kol_StepTest_Smaller = 0
    for d in range(len(List_StepTest)):
        if float(List_StepTest[d])>=Middle_StepTest:
            kol_StepTest_Bigger =kol_StepTest_Bigger +1
        if float(List_StepTest[d])<Middle_StepTest:
            kol_StepTest_Smaller =kol_StepTest_Smaller +1
    print "Количество пациентов, у которых данные степ-теста больше среднего =",kol_StepTest_Bigger
    print "Количество пациентов, у которых данные степ-теста меньше среднего =",kol_StepTest_Smaller

    # Определим вероятности, что данные больше или меньше 
    Ver_StepTest_Bigger = kol_StepTest_Bigger/float(number_patients)
    Ver_StepTest_Smaller = kol_StepTest_Smaller/float(number_patients)

    print "Вероятность данные больше =",Ver_StepTest_Bigger    
    print "Вероятность данные меньше=",Ver_StepTest_Smaller

    kol_StepTest_Smaller_Z = 0 
    kol_StepTest_Smaller_B = 0
    kol_StepTest_Bigger_Z = 0
    kol_StepTest_Bigger_B = 0

    Ver_StepTest_Smaller_Z = 0 
    Ver_StepTest_Smaller_B = 0
    Ver_StepTest_Bigger_Z = 0
    Ver_StepTest_Bigger_B = 0
    for d in range(len(List_StepTest)):
        #меньше
        if (float(List_StepTest[d])<Middle_StepTest)and (int(List_Rez[d])== 1):       
            kol_StepTest_Smaller_Z = kol_StepTest_Smaller_Z+1
        if (float(List_StepTest[d])<Middle_StepTest)and (int(List_Rez[d])== 2):
            kol_StepTest_Smaller_B = kol_StepTest_Smaller_B+1
        #  больше  
        if (float(List_StepTest[d])>=Middle_StepTest)and (int(List_Rez[d])== 1):
            kol_StepTest_Bigger_Z = kol_StepTest_Bigger_Z+1
        if (float(List_StepTest[d])>=Middle_StepTest)and (int(List_Rez[d])== 2):
            kol_StepTest_Bigger_B = kol_StepTest_Bigger_B+1


    Ver_StepTest_Smaller_Z = kol_StepTest_Smaller_Z/float(number_healthy)
    Ver_StepTest_Smaller_B = kol_StepTest_Smaller_B/float(number_sick)

    Ver_StepTest_Bigger_Z = kol_StepTest_Bigger_Z/float(number_healthy)
    Ver_StepTest_Bigger_B = kol_StepTest_Bigger_B/float(number_sick)

    print "-----меньше"
    print "Здоровые = ",Ver_StepTest_Smaller_Z
    print "Больные = ",Ver_StepTest_Smaller_B
    print "-----больше"
    print "Здоровые = ",Ver_StepTest_Bigger_Z
    print "Больные = ",Ver_StepTest_Bigger_B

    #Таблица Баесовских вероятностей
    V_StepTest_1 = 0
    V_StepTest_2 = 0
    V_StepTest_3 = 0
    V_StepTest_4 = 0

    #Вероятность, что здоров ,если данные меньше
    V_StepTest_1 = float(Probability_healthy)*Ver_StepTest_Smaller_Z/float(Ver_StepTest_Smaller)
    #Вероятность, что болен, если данные меньше
    V_StepTest_2 = float(Probability_sick)*Ver_StepTest_Smaller_B/float(Ver_StepTest_Smaller)

    #Вероятность, что здоров, если данные больше
    V_StepTest_3 = float(Probability_healthy)*Ver_StepTest_Bigger_Z/float(Ver_StepTest_Bigger)
    #Вероятность, что болен, если данные больше
    V_StepTest_4 = float(Probability_sick)*Ver_StepTest_Bigger_B/float(Ver_StepTest_Bigger)
    print "----------------------------------------------"
    print "Вероятность, что данные меньше + здоров =",V_StepTest_1
    print "Вероятность, что данные меньше + болен =",V_StepTest_2
    print "Вероятность, что данные больше + здоров =",V_StepTest_3
    print "Вероятность, что данные больше + болен =",V_StepTest_4
    print "----------------------------------------------"

    #Параметр №11 склонение данных по степ-тесту
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №11 склонение данных по степ-тесту -------"

    Symm_Sklon = 0
    for d in range(len(List_Sklon)):
        Symm_Sklon = Symm_Sklon + List_Sklon[d]
    Middle_Sklon = Symm_Sklon/float(len(List_Sklon))
    print "-------Среднее склонение данных =",Middle_Sklon

    # Подсчитаем  Количество пациентов, у которых данные больше Среднего склонения
    # Подсчитаем  Количество пациентов, у которых данные меньше Среднего склонения
    kol_Sklon_Bigger = 0
    kol_Sklon_Smaller = 0
    for d in range(len(List_Sklon)):
        if float(List_Sklon[d])>=Middle_Sklon:
            kol_Sklon_Bigger =kol_Sklon_Bigger +1
        if float(List_Sklon[d])<Middle_Sklon:
            kol_Sklon_Smaller =kol_Sklon_Smaller +1
    print "Количество пациентов, у которых данные больше Среднего склонения =",kol_Sklon_Bigger
    print "Количество пациентов, у которых данные меньше Среднего склонения =",kol_Sklon_Smaller

    # Определим вероятности, что пациент младше или старше
    Ver_Sklon_Bigger = kol_Sklon_Bigger/float(number_patients)
    Ver_Sklon_Smaller = kol_Sklon_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых данные больше Среднего склонения  =",Ver_Sklon_Bigger    
    print "Вероятность пациентов, у которых данные меньше Среднего склонения =",Ver_Sklon_Smaller

    kol_Sklon_Smaller_Z = 0 
    kol_Sklon_Smaller_B = 0
    kol_Sklon_Bigger_Z = 0
    kol_Sklon_Bigger_B = 0

    Ver_Sklon_Smaller_Z = 0 
    Ver_Sklon_Smaller_B = 0
    Ver_Sklon_Bigger_Z = 0
    Ver_Sklon_Bigger_B = 0
    for d in range(len(List_Sklon)):
        # меньше
        if (float(List_Sklon[d])<Middle_Sklon)and (int(List_Rez[d])== 1):       
            kol_Sklon_Smaller_Z = kol_Sklon_Smaller_Z+1
        if (float(List_Sklon[d])<Middle_Sklon)and (int(List_Rez[d])== 2):
            kol_Sklon_Smaller_B = kol_Sklon_Smaller_B+1
        #  больше 
        if (float(List_Sklon[d])>=Middle_Sklon)and (int(List_Rez[d])== 1):
            kol_Sklon_Bigger_Z = kol_Sklon_Bigger_Z+1
        if (float(List_Sklon[d])>=Middle_Sklon)and (int(List_Rez[d])== 2):
            kol_Sklon_Bigger_B = kol_Sklon_Bigger_B+1


    Ver_Sklon_Smaller_Z = kol_Sklon_Smaller_Z/float(number_healthy)
    Ver_Sklon_Smaller_B = kol_Sklon_Smaller_B/float(number_sick)

    Ver_Sklon_Bigger_Z = kol_Sklon_Bigger_Z/float(number_healthy)
    Ver_Sklon_Bigger_B = kol_Sklon_Bigger_B/float(number_sick)

    print "-----данные меньше"
    print "Здоровые = ",Ver_Sklon_Smaller_Z
    print "Больные = ",Ver_Sklon_Smaller_B
    print "-----данные больше"
    print "Здоровые = ",Ver_Sklon_Bigger_Z
    print "Больные = ",Ver_Sklon_Bigger_B

    #Таблица Баесовских вероятностей
    V_Sklon_1 = 0
    V_Sklon_2 = 0
    V_Sklon_3 = 0
    V_Sklon_4 = 0

    #Вероятность, что данные меньше + здоров
    V_Sklon_1 = float(Probability_healthy)*Ver_Sklon_Smaller_Z/float(Ver_Sklon_Smaller)

    #Вероятность, что данные меньше + болен
    V_Sklon_2 = float(Probability_sick)*Ver_Sklon_Smaller_B/float(Ver_Sklon_Smaller)

    #Вероятность, что данные больше + здоров
    V_Sklon_3 = float(Probability_healthy)*Ver_Sklon_Bigger_Z/float(Ver_Sklon_Bigger)
    #Вероятность, что данные больше + болен
    V_Sklon_4 = float(Probability_sick)*Ver_Sklon_Bigger_B/float(Ver_Sklon_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что данные меньше + здоров =",V_Sklon_1
    print "Вероятность, что данные меньше + болен =",V_Sklon_2
    print "Вероятность, что данные больше + здоров =",V_Sklon_3
    print "Вероятность, что данные больше + болен =",V_Sklon_4
    print "----------------------------------------------"


    #Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопией
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопие -------"

    Symm_Sosyd = 0
    for d in range(len(List_Sosyd)):
        Symm_Sosyd = Symm_Sosyd + List_Sosyd[d]
    Middle_Sosyd = Symm_Sosyd/float(len(List_Sosyd))
    print "-------Среднее количество основных сосудов =",Middle_Sosyd

    # Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего 
    # Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего 
    kol_Sosyd_Bigger = 0
    kol_Sosyd_Smaller = 0
    for d in range(len(List_Sosyd)):
        if float(List_Sosyd[d])>=Middle_Sosyd:
            kol_Sosyd_Bigger =kol_Sosyd_Bigger +1
        if float(List_Sosyd[d])<Middle_Sosyd:
            kol_Sosyd_Smaller =kol_Sosyd_Smaller +1
    print "Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего =",kol_Sosyd_Bigger
    print "Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего  =",kol_Sosyd_Smaller

    # Определим вероятности, что пациент младше или старше
    Ver_Sosyd_Bigger = kol_Sosyd_Bigger/float(number_patients)
    Ver_Sosyd_Smaller = kol_Sosyd_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых количество основных сосудов больше Среднего =",Ver_Sosyd_Bigger    
    print "Вероятность пациентов, у которых количество основных сосудов меньше Среднего =",Ver_Sosyd_Smaller

    kol_Sosyd_Smaller_Z = 0 
    kol_Sosyd_Smaller_B = 0
    kol_Sosyd_Bigger_Z = 0
    kol_Sosyd_Bigger_B = 0

    Ver_Sosyd_Smaller_Z = 0 
    Ver_Sosyd_Smaller_B = 0
    Ver_Sosyd_Bigger_Z = 0
    Ver_Sosyd_Bigger_B = 0
    for d in range(len(List_Sosyd)):
        # меньше
        if (float(List_Sosyd[d])<Middle_Sosyd)and (int(List_Rez[d])== 1):       
            kol_Sosyd_Smaller_Z = kol_Sosyd_Smaller_Z+1
        if (float(List_Sosyd[d])<Middle_Sosyd)and (int(List_Rez[d])== 2):
            kol_Sosyd_Smaller_B = kol_Sosyd_Smaller_B+1
        #  больше 
        if (float(List_Sosyd[d])>=Middle_Sosyd)and (int(List_Rez[d])== 1):
            kol_Sosyd_Bigger_Z = kol_Sosyd_Bigger_Z+1
        if (float(List_Sosyd[d])>=Middle_Sosyd)and (int(List_Rez[d])== 2):
            kol_Sosyd_Bigger_B = kol_Sosyd_Bigger_B+1


    Ver_Sosyd_Smaller_Z = kol_Sosyd_Smaller_Z/float(number_healthy)
    Ver_Sosyd_Smaller_B = kol_Sosyd_Smaller_B/float(number_sick)

    Ver_Sosyd_Bigger_Z = kol_Sosyd_Bigger_Z/float(number_healthy)
    Ver_Sosyd_Bigger_B = kol_Sosyd_Bigger_B/float(number_sick)

    print "-----количество основных сосудов меньше Среднего"
    print "Здоровые = ",Ver_Sosyd_Smaller_Z
    print "Больные = ",Ver_Sosyd_Smaller_B
    print "-----количество основных сосудов больше Среднего"
    print "Здоровые = ",Ver_Sosyd_Bigger_Z
    print "Больные = ",Ver_Sosyd_Bigger_B

    #Таблица Баесовских вероятностей
    V_Sosyd_1 = 0
    V_Sosyd_2 = 0
    V_Sosyd_3 = 0
    V_Sosyd_4 = 0

    #Вероятность, что количество основных сосудов меньше Среднего + здоров
    V_Sosyd_1 = float(Probability_healthy)*Ver_Sosyd_Smaller_Z/float(Ver_Sosyd_Smaller)
    #Вероятность, что количество основных сосудов меньше Среднего + болен
    V_Sosyd_2 = float(Probability_sick)*Ver_Sosyd_Smaller_B/float(Ver_Sosyd_Smaller)

    #Вероятность, что количество основных сосудов больше Среднего + здоров
    V_Sosyd_3 = float(Probability_healthy)*Ver_Sosyd_Bigger_Z/float(Ver_Sosyd_Bigger)
    #Вероятность, что количество основных сосудов больше Среднего + болен
    V_Sosyd_4 = float(Probability_sick)*Ver_Sosyd_Bigger_B/float(Ver_Sosyd_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что количество основных сосудов меньше Среднего + здоров =",V_Sosyd_1
    print "Вероятность, что количество основных сосудов меньше Среднего + болен =",V_Sosyd_2
    print "Вероятность, что количество основных сосудов больше Среднего + здоров =",V_Sosyd_3
    print "Вероятность, что количество основных сосудов больше Среднего + болен =",V_Sosyd_4
    print "----------------------------------------------"

    #Параметр №13 степень повреждения сосудов
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "-------Параметр №13 степень повреждения сосудов -------"

    Symm_SPS = 0
    for d in range(len(List_SPS)):
        Symm_SPS = Symm_SPS + List_SPS[d]
    Middle_SPS = Symm_SPS/float(len(List_SPS))
    print "-------Средняя степень повреждения сосудов =",Middle_SPS

    # Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  больше Среднего 
    # Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  меньше Среднего 
    kol_SPS_Bigger = 0
    kol_SPS_Smaller = 0
    for d in range(len(List_SPS)):
        if float(List_SPS[d])>=Middle_SPS:
            kol_SPS_Bigger =kol_SPS_Bigger +1
        if float(List_SPS[d])<Middle_SPS:
            kol_SPS_Smaller =kol_SPS_Smaller +1
    print "Количество пациентов, у которых степень повреждения сосудов  больше Среднего =",kol_SPS_Bigger
    print "Количество пациентов, у которых степень повреждения сосудов  меньше Среднего =",kol_SPS_Smaller

    # Определим вероятности, что степень повреждения сосудов меньше или больше 
    Ver_SPS_Bigger = kol_SPS_Bigger/float(number_patients)
    Ver_SPS_Smaller = kol_SPS_Smaller/float(number_patients)

    print "Вероятность пациентов, у которых степень повреждения сосудов  больше Среднего  =",Ver_SPS_Bigger    
    print "Вероятность пациентов, у которых степень повреждения сосудов  меньше Среднего =",Ver_SPS_Smaller

    kol_SPS_Smaller_Z = 0 
    kol_SPS_Smaller_B = 0
    kol_SPS_Bigger_Z = 0
    kol_SPS_Bigger_B = 0

    Ver_SPS_Smaller_Z = 0 
    Ver_SPS_Smaller_B = 0
    Ver_SPS_Bigger_Z = 0
    Ver_SPS_Bigger_B = 0
    for d in range(len(List_SPS)):
        # меньше
        if (float(List_SPS[d])<Middle_SPS)and (int(List_Rez[d])== 1):       
            kol_SPS_Smaller_Z = kol_SPS_Smaller_Z+1
        if (float(List_SPS[d])<Middle_SPS)and (int(List_Rez[d])== 2):
            kol_SPS_Smaller_B = kol_SPS_Smaller_B+1
        #  больше 
        if (float(List_SPS[d])>=Middle_SPS)and (int(List_Rez[d])== 1):
            kol_SPS_Bigger_Z = kol_SPS_Bigger_Z+1
        if (float(List_SPS[d])>=Middle_SPS)and (int(List_Rez[d])== 2):
            kol_SPS_Bigger_B = kol_SPS_Bigger_B+1


    Ver_SPS_Smaller_Z = kol_SPS_Smaller_Z/float(number_healthy)
    Ver_SPS_Smaller_B = kol_SPS_Smaller_B/float(number_sick)

    Ver_SPS_Bigger_Z = kol_SPS_Bigger_Z/float(number_healthy)
    Ver_SPS_Bigger_B = kol_SPS_Bigger_B/float(number_sick)

    print "-----степень повреждения сосудов  меньше"
    print "Здоровые = ",Ver_SPS_Smaller_Z
    print "Больные = ",Ver_SPS_Smaller_B
    print "-----степень повреждения сосудов больше"
    print "Здоровые = ",Ver_SPS_Bigger_Z
    print "Больные = ",Ver_SPS_Bigger_B

    #Таблица Баесовских вероятностей
    V_SPS_1 = 0
    V_SPS_2 = 0
    V_SPS_3 = 0
    V_SPS_4 = 0

    #Вероятность, что степень повреждения сосудов  меньше + здоров
    V_SPS_1 = float(Probability_healthy)*Ver_SPS_Smaller_Z/float(Ver_SPS_Smaller)
    #Вероятность, что степень повреждения сосудов  меньше + болен
    V_SPS_2 = float(Probability_sick)*Ver_SPS_Smaller_B/float(Ver_SPS_Smaller)

    #Вероятность, что степень повреждения сосудов больше + здоров
    V_SPS_3 = float(Probability_healthy)*Ver_SPS_Bigger_Z/float(Ver_SPS_Bigger)
    #Вероятность, что степень повреждения сосудов больше + болен
    V_SPS_4 = float(Probability_sick)*Ver_SPS_Bigger_B/float(Ver_SPS_Bigger)

    print "----------------------------------------------"
    print "Вероятность, что степень повреждения сосудов меньше + здоров =",V_SPS_1
    print "Вероятность, что степень повреждения сосудов меньше + болен=",V_SPS_2
    print "Вероятность, что степень повреждения сосудов больше + здоров =",V_SPS_3
    print "Вероятность, что степень повреждения сосудов больше + болен =",V_SPS_4
    print "----------------------------------------------"

