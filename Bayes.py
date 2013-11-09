# -*- coding: utf-8 -*-
from __future__ import unicode_literals
Probability_result_healthy=1
Probability_result_sick=1

#«Байесовский классификатор»
def Bayes_classifier(number_sick,number_healthy,Probability_sick,Probability_healthy,List_param,List_other_param,List_Rez):
    print "\n-----------------------«БАЙЕСОВСКИЙ КЛАССИФИКАТОР»-----------------------"

    #Подсчет значений для основных параметров
    def calculate_parameters(List_Parametr):
        #расчет среднего значения
        Summa_parametr=0
        for i in range(len(List_Parametr)):
            Summa_parametr+=List_Parametr[i]
        Middle_parametr = Summa_parametr/float(len(List_Parametr))
        # Подсчитаем  Количество пациентов,значение параметра которых больше или меньше среднего
        amount_parametr_More = 0
        amount_parametr_Less = 0
        for i in range(len(List_Parametr)):
            if float(List_Parametr[i])>=Middle_parametr:
                amount_parametr_More +=1
            if float(List_Parametr[i])<Middle_parametr:
                amount_parametr_Less +=1
        Probability_parametr_More = amount_parametr_More/float(number_patients)
        Probability_parametr_Less = amount_parametr_Less/float(number_patients)
        #Подсчитываем количество
        Amount_Less_Healthy=0
        Amount_Less_Sick=0
        Amount_More_Healthy=0
        Amount_More_Sick=0
        for i in range(len(List_Parametr)):
            #   меньше среднего значения
            if (float(List_Parametr[i])<Middle_parametr)and (int(List_Rez[i])== 1):
                Amount_Less_Healthy +=1
            if (float(List_Parametr[i])<Middle_parametr)and (int(List_Rez[i])== 2):
                Amount_Less_Sick+=1
            #  больше среднего значения
            if (float(List_Parametr[i])>=Middle_parametr)and (int(List_Rez[i])== 1):
                Amount_More_Healthy+=1
            if (float(List_Parametr[i])>=Middle_parametr)and (int(List_Rez[i])== 2):
               Amount_More_Sick+=1
        #Подсчитываем вероятность
        Probability_Less_Healthy= Amount_Less_Healthy /float(number_healthy)
        Probability_Less_Sick= Amount_Less_Sick/float(number_sick)
        Probability_More_Healthy= Amount_More_Healthy/float(number_healthy)
        Probability_More_Sick = Amount_More_Sick/float(number_sick)
        #Подсчет вероятностей с учетом примитивного классификатора
        #Таблица Баесовских вероятностей
        Probability_Baes_Less_Healthy = 0
        Probability_Baes_Less_Sick = 0
        Probability_Baes_More_Healthy = 0
        Probability_Baes_More_Sick = 0
        #Вероятность, что здоров ,если возраст младше
        Probability_Baes_Less_Healthy = float(Probability_healthy)*Probability_Less_Healthy/float(Probability_parametr_Less )
        #Вероятность, что болен,если возраст младше
        Probability_Baes_Less_Sick = float(Probability_sick)*Probability_Less_Sick/float(Probability_parametr_Less )
        #Вероятность, что здоров ,если возраст старше
        Probability_Baes_More_Healthy = float(Probability_healthy)*Probability_More_Healthy/float(Probability_parametr_More)
        #Вероятность, что болен,если возраст старше
        Probability_Baes_More_Sick = float(Probability_sick)*Probability_More_Sick/float(Probability_parametr_More)
        return (amount_parametr_More,amount_parametr_Less,Probability_parametr_More,Probability_parametr_Less,Probability_Less_Healthy,Probability_Less_Sick,Probability_More_Healthy,Probability_More_Sick,Probability_Baes_Less_Healthy,Probability_Baes_Less_Sick,Probability_Baes_More_Healthy,Probability_Baes_More_Sick, Middle_parametr)


    #Подсчет значений для параметров Пол и Наличие стенокардии
    def calculate_other_parameters(List_Parametr):
        Amount_Parametr_Enabled = 0
        Amount_Parametr_Disabled = 0
        i=0
        for i in range(len(List_Parametr)):
            if float(List_Parametr[i])==0.0:
                Amount_Parametr_Enabled +=1
            if float(List_Parametr[i])==1.0:
                Amount_Parametr_Disabled +=1
        # Определим вероятности, наличия или отсутствие этого параметра
        Probability_Parametr_Enabled = Amount_Parametr_Enabled/float(number_patients)
        Probability_Parametr_Disabled =  Amount_Parametr_Disabled/float(number_patients)

        Amount_Parametr_Disabled_Healthy = 0
        Amount_Parametr_Disabled_Sick = 0
        Amount_Parametr_Enabled_Healthy = 0
        Amount_Parametr_Enabled_Sick = 0

        Probability_Parametr_Disabled_Healthy = 0
        Probability_Parametr_Disabled_Sick = 0
        Probability_Parametr_Enabled_Healthy = 0
        Probability_Parametr_Enabled_Sick = 0

        for i in range(len(List_Parametr)):
            # Disabled
            if (float(List_Parametr[i])==0.0)and (int(List_Rez[i])== 1):
               Amount_Parametr_Disabled_Healthy+=1
            if (float(List_Parametr[i])==0.0)and (int(List_Rez[i])== 2):
                Amount_Parametr_Disabled_Sick +=1
            #  Enabled
            if (float(List_Parametr[i])==1.0)and (int(List_Rez[i])== 1):
                Amount_Parametr_Enabled_Healthy+=1
            if (float(List_Parametr[i])==1.0)and (int(List_Rez[i])== 2):
                 Amount_Parametr_Enabled_Sick+=1

        Probability_Parametr_Disabled_Healthy =  Amount_Parametr_Disabled_Healthy/float(number_healthy)
        Probability_Parametr_Disabled_Sick =  Amount_Parametr_Disabled_Sick/float(number_sick)
        Probability_Parametr_Enabled_Healthy = Amount_Parametr_Enabled_Healthy/float(number_healthy)
        Probability_Parametr_Enabled_Sick = Amount_Parametr_Enabled_Sick/float(number_sick)

        #Таблица Байесовских вероятностей
        Probability_Baes_Parametr_Disabled_Healthy = 0
        Probability_Baes_Parametr_Disabled_Sick = 0
        Probability_Baes_Parametr_Enabled_Healthy = 0
        Probability_Baes_Parametr_Enabled_Sick = 0

        #Вероятность, что параметр присутствует + здоров
        Probability_Baes_Parametr_Disabled_Healthy = float(Probability_healthy)*Probability_Parametr_Disabled_Healthy/float(Probability_Parametr_Enabled)
        #Вероятность, что параметр присутствует + болен
        Probability_Baes_Parametr_Disabled_Sick = float(Probability_sick)*Probability_Parametr_Disabled_Sick/float(Probability_Parametr_Enabled)
        #Вероятность, что параметр присутствует + здоров
        Probability_Baes_Parametr_Enabled_Healthy = float(Probability_healthy)*Probability_Parametr_Enabled_Healthy/float(Probability_Parametr_Disabled)
        #Вероятность, что параметр присутствует + болен
        Probability_Baes_Parametr_Enabled_Sick = float(Probability_sick)*Probability_Parametr_Enabled_Sick/float(Probability_Parametr_Disabled)
        return (Amount_Parametr_Enabled, Amount_Parametr_Disabled,Probability_Parametr_Enabled, Probability_Parametr_Disabled,Probability_Parametr_Disabled_Healthy,Probability_Parametr_Disabled_Sick,Probability_Parametr_Enabled_Healthy,Probability_Parametr_Enabled_Sick,Probability_Baes_Parametr_Disabled_Healthy,Probability_Baes_Parametr_Disabled_Sick,Probability_Baes_Parametr_Enabled_Healthy,Probability_Baes_Parametr_Enabled_Sick)



    def Output_results(Parametr_Vales,Parametr_Name):
        if (Parametr_Name=="List_Sten"):
            output_string ="Количество пациентов, у которых нет стенокардии в анамнезе = "+str(Parametr_Vales[0])+"\nКоличество пациентов, у которых есть стенокардия в анамнезе = "+str(Parametr_Vales[1])+"\nВероятность пациентов, у которых есть стенокардия в анамнезе = "+str(Parametr_Vales[2])+"\nВероятность пациентов, у которых нет стенокардии в анамнезе = "+str(Parametr_Vales[3])+"\nВероятность того, что у пациента  есть стенокардия в анамнезе и он здоров = "+str(Parametr_Vales[4])+"\nВероятность того, что у пациента  есть стенокардия в анамнезе и он болен = "+str(Parametr_Vales[5])+"\nВероятность того, что у пациента нет стенокардии в анамнезе и он здоров = "+str(Parametr_Vales[6])+"\nВероятность того, что у пациента нет стенокардии в анамнезе и он болен = "+str(Parametr_Vales[7])+"\nВероятность, что здоров ,если есть стенокардия в анамнезе = "+str(Parametr_Vales[8])+"\nВероятность, что болен ,если есть стенокардия в анамнезе = "+str(Parametr_Vales[9])+"\nВероятность, что здоров ,если нет стенокардия в анамнезе = "+str(Parametr_Vales[10])+"\nВероятность, что болен ,если нет стенокардия в анамнезе = "+str(Parametr_Vales[11])

        else:
            output_string ="Количечество пациентов, у которых значение параметра больше среднего = "+str(Parametr_Vales[0])+"\nКоличечество пациентов, у которых значение параметра меньше среднего = "+str(Parametr_Vales[1])+"\nВероятность того, что у пациента значение параметра больше среднего = "+str(Parametr_Vales[2])+"\nВероятность того, что у пациента значение параметра меньше среднего = "+str(Parametr_Vales[3])+"\nВероятность того, что у пациента параметр меньше среднего и он здоров = "+str(Parametr_Vales[4])+"\nВероятность того, что у пациента параметр меньше среднего и он болен = "+str(Parametr_Vales[5])+"\nВероятность того, что у пациента параметр больше среднего и он здоров = "+str(Parametr_Vales[6])+"\nВероятность того, что у пациента параметр меньше среднего и он болен = "+str(Parametr_Vales[7])+"\nВероятность, что здоров ,если параметр меньше среднего = "+str(Parametr_Vales[8])+"\nВероятность, что болен ,если параметр меньше среднего = "+str(Parametr_Vales[9])+"\nВероятность, что здоров ,если параметр больше среднего = "+str(Parametr_Vales[10])+"\nВероятность, что болен ,если параметр больше среднего = "+str(Parametr_Vales[11])
        print output_string

    #Вызов функций и определение нужных переменных
    number_patients = len(List_Rez)

    Keys_param=('List_Age','List_Har','List_VG','List_YH','List_YS','List_Card','List_MaxP','List_StepTest','List_Sklon','List_Sosyd','List_Sps')
    Keys_all=('List_Age','List_Har','List_VG','List_YH','List_YS','List_Card','List_MaxP','List_Sten','List_StepTest','List_Sklon','List_Sosyd','List_Sps')
    Result_Vocabluary={'List_Age':0,'List_Har':0,'List_VG':0,'List_VG':0,'List_YH':0,'List_YS':0,'List_Card':0,'List_MaxP':0,'List_StepTest':0,'List_Sklon':0,'List_Sosyd':0,'List_Sps':0,'List_Sten':0}


    #подсчет основных параметров и сохранение в словарь
    j = 0
    for i in List_param:
        a=calculate_parameters(i)
        Result_Vocabluary[Keys_param[j]]=a
        j+=1

    #подсчет параметра Наличие стенокардии  и сохранение в словарь
    a=calculate_other_parameters(List_other_param)
    Result_Vocabluary['List_Sten']=a

    #Список названий параметров
    List_parametrname=('ВОЗРАСТ','ХАРАКТЕР БОЛИ В СЕРДЦЕ','ВЕРХНЯЯ ГРАНИЦА ДАВЛЕНИЯ','УРОВЕНЬ ХОЛЕСТЕРИНА','УРОВЕНЬ САХАРА','РЕЗУЛЬТАТЫ КАРДИОГРАММЫ В СОСТОЯНИИ ПОКОЯ','МАКСИМАЛЬНАЯ ВЕЛИЧИНА ПУЛЬСА','НАЛИЧИЕ СТЕНОКАРДИИ','ДАННЫЕ СТЕП-ТЕСТА','СКЛОНЕНИЕ ДАННЫХ ПО СТЕП-ТЕСТУ','КОЛИЧЕСТВО ОСНОВНЫХ СОСУДОВ','СТЕПЕНЬ ПОВРЕЖДЕНИЯ СОСУДОВ')

    #Цикл вывода значений параметров
    for i in range(len(Keys_all)):
        print"\n------------------------------------------"
        print "Параметр "+List_parametrname[i]
        print"------------------------------------------"
        Output_results(Result_Vocabluary[Keys_all[i]],Keys_all[i])
    return Result_Vocabluary