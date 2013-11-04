
# -*- coding: cp1251 -*-
#import scipy
#import scipy.stats
#объявим переменные атрибутов
Per_Age =''
Per_Pol =''
Per_Har =''
Per_VG =''
Per_YH =''
Per_YS =''
Per_Card =''
Per_MaxP =''
Per_Sten =''
Per_StepTest =''
Per_Sklon =''
Per_Sosyd =''
Per_SPS =''

#Выданный результат
Per_Rez =''

#объявим списки для хранения атрибутов
# мой вариант
#9 10 11 12 13 1 2 3 4 5 6 7
Sp_Age = []
Sp_Pol = []
Sp_Har = []
Sp_VG = []
Sp_YH = []
Sp_YS = []
Sp_Card = []
Sp_MaxP = []
Sp_Sten = []
Sp_StepTest = []
Sp_Sklon = []
Sp_Sosyd = []
Sp_SPS = []
#Выданный результат 
Sp_Rez =[]


PathOfFile = "heart.csv"
f=open(PathOfFile,"rb")
li = f.readlines()
f.close()

for stroka in li:
    Per_Age,Per_Pol,Per_Har,Per_VG,Per_YH,Per_YS,Per_Card,Per_MaxP,Per_Sten,Per_StepTest,Per_Sklon,Per_Sosyd,Per_SPS,Per_Rez = stroka.split()  
    Sp_Age.append(float(Per_Age))
    Sp_Pol.append(float(Per_Pol))
    Sp_Har.append(float(Per_Har))
    Sp_VG.append(float(Per_VG))
    Sp_YH.append(float(Per_YH))
    Sp_YS.append(float(Per_YS))
    Sp_Card.append(float(Per_Card))
    Sp_MaxP.append(float(Per_MaxP))
    Sp_Sten.append(float(Per_Sten))
    Sp_StepTest.append(float(Per_StepTest))
    Sp_Sklon.append(float(Per_Sklon))
    Sp_Sosyd.append(float(Per_Sosyd))
    Sp_SPS.append(float(Per_SPS))
    #Выданный результат список
    Sp_Rez.append(float(Per_Rez))

# Corelation
#print "Взаимсовязь между возрастом и диагнозом"
#print scipy.stats.kendalltau(Sp_Age,Sp_Rez)[0]


print "-----------------------Примитивный класификатор-----------------------"
# Подсчитаем общее количество пациентов
kol = len(Sp_Rez)
print "общее количество пациентов =",kol

# Подсчитаем  Количество здоровых пациентов
# Подсчитаем  Количество больных пациентов
sym_B = 0
sym_Z = 0
for i in range(len(Sp_Rez)):
    if Sp_Rez[i]== 1:
        sym_Z = sym_Z + 1
    if Sp_Rez[i]== 2:
        sym_B = sym_B + 1
print "Количество больных пациентов =",sym_B    
print "Количество здоровых пациентов=",sym_Z

# Определим вероятности, что пациент болен или здоров
Ver_B = sym_B/float(kol)
Ver_Z = sym_Z/float(kol)

print "Вероятность больных пациентов =",Ver_B    
print "Вероятность здоровых пациентов=",Ver_Z

#Возьмём пациента и проверим болен он или здоров

#Запишем список, в котором будут хранится выданный диагноз примититвного классификатора
Prim = []
Prim_Z = []
Prim_B = []

print "---------Возьмём пациента и проверим болен он или здоров"
Per_Age0 =''
Per_Pol0 =''
Per_Har0 =''
Per_VG0 =''
Per_YH0 =''
Per_YS0 =''
Per_Card0 =''
Per_MaxP0 =''
Per_Sten0 =''
Per_StepTest0 =''
Per_Sklon0 =''
Per_Sosyd0 =''
Per_SPS0 =''

#Выданный результат
Per_Rez =''

PathOfFile = "pacient.csv"
f=open(PathOfFile,"rb")
li1 = f.readlines()
f.close()
for stroka in li1:
    Per_Age0,Per_Pol0,Per_Har0,Per_VG0,Per_YH0,Per_YS0,Per_Card0,Per_MaxP0,Per_Sten0,Per_StepTest0,Per_Sklon0,Per_Sosyd0,Per_SPS0,Per_Rez0 = stroka.split()  
 
     #Определим болен или здоров пациент
    Itog = ''
    D1 =0
    if Ver_B>Ver_Z:
        Itog = '2'
        D1 = 2
    if Ver_Z>Ver_B:
        Itog = '1'
        D1 = 1
    if Ver_Z==Ver_B:
        Itog = '0'
    Prim.append(D1)
    Prim_Z.append(Ver_Z)
    Prim_B.append(Ver_B)


#«Байесовский классификатор»
print "-----------------------«Байесовский классификатор»-----------------------"
#Параметр №1 Возраст
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print "-------Параметр №1 Возраст-------"
Symm_Age = 0
for d in range(len(Sp_Age)):
    Symm_Age = Symm_Age + Sp_Age[d]
Middle_Age = Symm_Age/float(len(Sp_Age))
print "-------Средний возраст =",Middle_Age," лет"

# Подсчитаем  Количество пациентов, которые старше среднего возраста 
# Подсчитаем  Количество пациентов, которые младше среднего возраста
kol_Age_Bigger = 0
kol_Age_Smaller = 0
for d in range(len(Sp_Age)):
    if float(Sp_Age[d])>=Middle_Age:
        kol_Age_Bigger =kol_Age_Bigger +1
    if float(Sp_Age[d])<Middle_Age:
        kol_Age_Smaller =kol_Age_Smaller +1
print "Количество пациентов, которые старше среднего возраста =",kol_Age_Bigger
print "Количество пациентов, которые младше среднего возраста =",kol_Age_Smaller

# Определим вероятности, что пациент младше или старше
Ver_Age_Bigger = kol_Age_Bigger/float(kol)
Ver_Age_Smaller = kol_Age_Smaller/float(kol)

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
for d in range(len(Sp_Age)):
    # младшие
    #print "Diagnoz =",Sp_Rez[d]
    if (float(Sp_Age[d])<Middle_Age)and (int(Sp_Rez[d])== 1):
        
        kol_Age_Smaller_Z = kol_Age_Smaller_Z+1
    if (float(Sp_Age[d])<Middle_Age)and (int(Sp_Rez[d])== 2):
        kol_Age_Smaller_B = kol_Age_Smaller_B+1
    #  старшие  
    if (float(Sp_Age[d])>=Middle_Age)and (int(Sp_Rez[d])== 1):
        kol_Age_Bigger_Z = kol_Age_Bigger_Z+1
    if (float(Sp_Age[d])>=Middle_Age)and (int(Sp_Rez[d])== 2):
        kol_Age_Bigger_B = kol_Age_Bigger_B+1


Ver_Age_Smaller_Z = kol_Age_Smaller_Z/float(sym_Z)
Ver_Age_Smaller_B = kol_Age_Smaller_B/float(sym_B)

Ver_Age_Bigger_Z = kol_Age_Bigger_Z/float(sym_Z)
Ver_Age_Bigger_B = kol_Age_Bigger_B/float(sym_B)

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
V_Age_1 = float(Ver_Z)*Ver_Age_Smaller_Z/float(Ver_Age_Smaller)

#Вероятность, что болен,если возраст младше
V_Age_2 = float(Ver_B)*Ver_Age_Smaller_B/float(Ver_Age_Smaller)
#Вероятность, что здоров ,если возраст старше
V_Age_3 = float(Ver_Z)*Ver_Age_Bigger_Z/float(Ver_Age_Bigger)

#Вероятность, что болен,если возраст старше
V_Age_4 = float(Ver_B)*Ver_Age_Bigger_B/float(Ver_Age_Bigger)
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
for d in range(len(Sp_Pol)):
    if float(Sp_Pol[d])==0.0:
        kol_Pol_Myj =kol_Pol_Myj +1
    if float(Sp_Pol[d])==1.0:
        kol_Pol_Jen =kol_Pol_Jen +1
print "Количество пациентов-мужчин =",kol_Pol_Myj
print "Количество пациентов-женщин =",kol_Pol_Jen
# Определим вероятности, что пациент-мужчина или пациент-женщина
Ver_Pol_Myj = kol_Pol_Myj/float(kol)
Ver_Pol_Jen = kol_Pol_Jen/float(kol)

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

for d in range(len(Sp_Pol)):
    # мужчины
    if (float(Sp_Pol[d])==0.0)and (int(Sp_Rez[d])== 1):       
        kol_Pol_Myj_Z = kol_Pol_Myj_Z+1
    if (float(Sp_Pol[d])==0.0)and (int(Sp_Rez[d])== 2):
        kol_Pol_Myj_B = kol_Pol_Myj_B+1
    #  женщины  
    if (float(Sp_Pol[d])==1.0)and (int(Sp_Rez[d])== 1):
        kol_Pol_Jen_Z = kol_Pol_Jen_Z + 1
    if (float(Sp_Pol[d])==1.0)and (int(Sp_Rez[d])== 2):
        kol_Pol_Jen_B = kol_Pol_Jen_B+1

Ver_Pol_Myj_Z = kol_Pol_Myj_Z/float(sym_Z) 
Ver_Pol_Myj_B = kol_Pol_Myj_B/float(sym_B)
Ver_Pol_Jen_Z = kol_Pol_Jen_Z/float(sym_Z)
Ver_Pol_Jen_B = kol_Pol_Jen_B/float(sym_B)

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
V_Pol_1 = float(Ver_Z)*Ver_Pol_Myj_Z/float(Ver_Pol_Myj)
#Вероятность, что пациент-мужчина + болен
V_Pol_2 = float(Ver_B)*Ver_Pol_Myj_B/float(Ver_Pol_Myj)

#Вероятность, что пациент-женщина + здоров
V_Pol_3 = float(Ver_Z)*Ver_Pol_Jen_Z/float(Ver_Pol_Jen)
#Вероятность, что пациент-женщина + болен
V_Pol_4 = float(Ver_B)*Ver_Pol_Jen_B/float(Ver_Pol_Jen)

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
for d in range(len(Sp_VG)):
    Symm_VG = Symm_VG + Sp_VG[d]
Middle_VG = Symm_VG/float(len(Sp_VG))
print "-------Среднее значение границы давления в состоянии покоя =",Middle_VG

# Подсчитаем  Количество пациентов с большей границей давления
# Подсчитаем  Количество пациентов, с меньшей границей давления
kol_VG_Smaller = 0
kol_VG_Bigger = 0

for d in range(len(Sp_VG)):
    if float(Sp_VG[d])>=Middle_VG:
        kol_VG_Bigger =kol_VG_Bigger +1
    if float(Sp_VG[d])<Middle_VG:
        kol_VG_Smaller =kol_VG_Smaller +1
print "Количество пациентов с меньшей границей давления=",kol_VG_Smaller
print "Количество пациентов с большей границей давления=",kol_VG_Bigger

# Определим вероятности, что пациент младше или старше
Ver_VG_Smaller = kol_VG_Smaller/float(kol)
Ver_VG_Bigger = kol_VG_Bigger/float(kol)

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
for d in range(len(Sp_VG)):
    # младшие
    #print "Diagnoz =",Sp_Rez[d]
    if (float(Sp_VG[d])<Middle_VG)and (int(Sp_Rez[d])== 1):       
        kol_VG_Smaller_Z = kol_VG_Smaller_Z+1
    if (float(Sp_VG[d])<Middle_VG)and (int(Sp_Rez[d])== 2):
        kol_VG_Smaller_B = kol_VG_Smaller_B+1
    #  старшие  
    if (float(Sp_VG[d])>=Middle_VG)and (int(Sp_Rez[d])== 1):
        kol_VG_Bigger_Z = kol_VG_Bigger_Z+1
    if (float(Sp_VG[d])>=Middle_VG)and (int(Sp_Rez[d])== 2):
        kol_VG_Bigger_B = kol_VG_Bigger_B+1


Ver_VG_Smaller_Z = kol_VG_Smaller_Z/float(sym_Z)
Ver_VG_Smaller_B = kol_VG_Smaller_B/float(sym_B)

Ver_VG_Bigger_Z = kol_VG_Bigger_Z/float(sym_Z)
Ver_VG_Bigger_B = kol_VG_Bigger_B/float(sym_B)

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
V_VG_1 = float(Ver_Z)*Ver_VG_Smaller_Z/float(Ver_VG_Smaller)

#Вероятность, что болен,если граница меньше
V_VG_2 = float(Ver_B)*Ver_VG_Smaller_B/float(Ver_VG_Smaller)
#Вероятность, что здоров ,если граница больше
V_VG_3 = float(Ver_Z)*Ver_VG_Bigger_Z/float(Ver_VG_Bigger)

#Вероятность, что болен,если граница больше
V_VG_4 = float(Ver_B)*Ver_VG_Bigger_B/float(Ver_VG_Bigger)
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
for d in range(len(Sp_YH)):
    Symm_YH = Symm_YH + Sp_YH[d]
Middle_YH = Symm_YH/float(len(Sp_YH))
print "-------Средний уровень холестерина в крови =",Middle_YH," mg/dl"

# Подсчитаем  Количество пациентов, у которых уровень холестерина больше среднего
# Подсчитаем  Количество пациентов, у которыхуровень холестерина меньше среднего
kol_YH_Bigger = 0
kol_YH_Smaller = 0
for d in range(len(Sp_YH)):
    if float(Sp_YH[d])>=Middle_YH:
        kol_YH_Bigger =kol_YH_Bigger +1
    if float(Sp_YH[d])<Middle_YH:
        kol_YH_Smaller =kol_YH_Smaller +1
print "Количество пациентов, у которых уровень холестерина больше среднего =",kol_YH_Bigger
print "Количество пациентов, у которых уровень холестерина меньше среднего =",kol_YH_Smaller

# Определим вероятности, что у пациента уровнеь больше или меньше
Ver_YH_Bigger = kol_YH_Bigger/float(kol)
Ver_YH_Smaller = kol_YH_Smaller/float(kol)

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
for d in range(len(Sp_YH)):
    # младшие
    #print "Diagnoz =",Sp_Rez[d]
    if (float(Sp_YH[d])<Middle_YH)and (int(Sp_Rez[d])== 1):       
        kol_YH_Smaller_Z = kol_YH_Smaller_Z+1
    if (float(Sp_YH[d])<Middle_YH)and (int(Sp_Rez[d])== 2):
        kol_YH_Smaller_B = kol_YH_Smaller_B+1
    #  старшие  
    if (float(Sp_YH[d])>=Middle_YH)and (int(Sp_Rez[d])== 1):
        kol_YH_Bigger_Z = kol_YH_Bigger_Z+1
    if (float(Sp_YH[d])>=Middle_YH)and (int(Sp_Rez[d])== 2):
        kol_YH_Bigger_B = kol_YH_Bigger_B+1


Ver_YH_Smaller_Z = kol_YH_Smaller_Z/float(sym_Z)
Ver_YH_Smaller_B = kol_YH_Smaller_B/float(sym_B)

Ver_YH_Bigger_Z = kol_YH_Bigger_Z/float(sym_Z)
Ver_YH_Bigger_B = kol_YH_Bigger_B/float(sym_B)

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
V_YH_1 = float(Ver_Z)*Ver_YH_Smaller_Z/float(Ver_YH_Smaller)
#Вероятность, что болен,если уровень холестерина меньше среднего
V_YH_2 = float(Ver_B)*Ver_YH_Smaller_B/float(Ver_YH_Smaller)

#Вероятность, что здоров ,если уровень холестерина больше среднего
V_YH_3 = float(Ver_Z)*Ver_YH_Bigger_Z/float(Ver_YH_Bigger)
#Вероятность, что болен,если уровень холестерина больше среднего
V_YH_4 = float(Ver_B)*Ver_YH_Bigger_B/float(Ver_YH_Bigger)
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
for d in range(len(Sp_YS)):
    Symm_YS = Symm_YS + Sp_YS[d]
Middle_YS = Symm_YS/float(len(Sp_YS))
print "-------Средний уровень сахара в крови =",Middle_YS," mg/dl"

# Подсчитаем  Количество пациентов, у которых уровень сахара больше 120
# Подсчитаем  Количество пациентов, у которых уровень сахара меньше 120
kol_YS_Bigger = 0
kol_YS_Smaller = 0
for d in range(len(Sp_YS)):
    if float(Sp_YS[d])>=Middle_YS:
        kol_YS_Bigger =kol_YS_Bigger +1
    if float(Sp_YS[d])<Middle_YH:
        kol_YS_Smaller =kol_YS_Smaller +1
print "Количество пациентов, у которых уровень сахара больше среднего =",kol_YS_Bigger
print "Количество пациентов, у которых уровень сахара меньше среднего =",kol_YS_Smaller

# Определим вероятности, что у пациента уровень больше или меньше
Ver_YS_Bigger = kol_YS_Bigger/float(kol)
Ver_YS_Smaller = kol_YS_Smaller/float(kol)

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
for d in range(len(Sp_YS)):
    # младшие
    #print "Diagnoz =",Sp_Rez[d]
    if (float(Sp_YS[d])<Middle_YS)and (int(Sp_Rez[d])== 1):       
        kol_YS_Smaller_Z = kol_YS_Smaller_Z+1
    if (float(Sp_YS[d])<Middle_YS)and (int(Sp_Rez[d])== 2):
        kol_YS_Smaller_B = kol_YS_Smaller_B+1
    #  старшие  
    if (float(Sp_YS[d])>=Middle_YS)and (int(Sp_Rez[d])== 1):
        kol_YS_Bigger_Z = kol_YS_Bigger_Z+1
    if (float(Sp_YS[d])>=Middle_YS)and (int(Sp_Rez[d])== 2):
        kol_YS_Bigger_B = kol_YS_Bigger_B+1


Ver_YS_Smaller_Z = kol_YS_Smaller_Z/float(sym_Z)
Ver_YS_Smaller_B = kol_YS_Smaller_B/float(sym_B)

Ver_YS_Bigger_Z = kol_YS_Bigger_Z/float(sym_Z)
Ver_YS_Bigger_B = kol_YS_Bigger_B/float(sym_B)

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
V_YS_1 = float(Ver_Z)*Ver_YS_Smaller_Z/float(Ver_YS_Smaller)
#Вероятность, что болен,если уровень сахара меньше 120
V_YS_2 = float(Ver_B)*Ver_YS_Smaller_B/float(Ver_YS_Smaller)

#Вероятность, что здоров ,если уровень сахара больше 120
V_YS_3 = float(Ver_Z)*Ver_YS_Bigger_Z/float(Ver_YS_Bigger)
#Вероятность, что болен,если уровень сахара больше 120
V_YS_4 = float(Ver_B)*Ver_YS_Bigger_B/float(Ver_YS_Bigger)
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
for d in range(len(Sp_Card)):
    Symm_Card = Symm_Card + Sp_Card[d]
Middle_Card = Symm_Card/float(len(Sp_Card))
print "-------Средние результаты кардиограммы=",Middle_Card

# Подсчитаем  Количество пациентов, у которых результаты кардиограммы больше среднего
# Подсчитаем  Количество пациентов, у которых результаты кардиограммы меньше среднего
kol_Card_Bigger = 0
kol_Card_Smaller = 0

for d in range(len(Sp_Card)):
    if float(Sp_Card[d])>=Middle_Card:
        kol_Card_Bigger =kol_Card_Bigger +1
    if float(Sp_Card[d])<Middle_Card:
        kol_Card_Smaller =kol_Card_Smaller +1
print "Количество пациентов, которые имеют результаты кардиограммы больше среднего =",kol_Card_Bigger
print "Количество пациентов, которые имеют результаты кардиограммы меньше среднего =",kol_Card_Smaller

# Определим вероятности, что у пациента результаты кардиограммы больше или меньше
Ver_Card_Bigger = kol_Card_Bigger/float(kol)
Ver_Card_Smaller = kol_Card_Smaller/float(kol)

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

for d in range(len(Sp_Card)):
    # младшие
    #print "Diagnoz =",Sp_Rez[d]
    if (float(Sp_Card[d])<Middle_Card)and (int(Sp_Rez[d])== 1):       
        kol_Card_Smaller_Z = kol_Card_Smaller_Z+1
    if (float(Sp_Card[d])<Middle_Card)and (int(Sp_Rez[d])== 2):
        kol_Card_Smaller_B = kol_Card_Smaller_B+1
    #  старшие  
    if (float(Sp_Card[d])>=Middle_Card)and (int(Sp_Rez[d])== 1):
        kol_Card_Bigger_Z = kol_Card_Bigger_Z+1
    if (float(Sp_Card[d])>=Middle_Card)and (int(Sp_Rez[d])== 2):
        kol_Card_Bigger_B = kol_Card_Bigger_B+1

Ver_Card_Smaller_Z = kol_Card_Smaller_Z/float(sym_Z)
Ver_Card_Smaller_B = kol_Card_Smaller_B/float(sym_B)

Ver_Card_Bigger_Z = kol_Card_Bigger_Z/float(sym_Z)
Ver_Card_Bigger_B = kol_Card_Bigger_B/float(sym_B)

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
V_Card_1 = float(Ver_Z)*Ver_Card_Smaller_Z/float(Ver_Card_Smaller)
#Вероятность, что Результаты кардиограммы меньше среднего уровня + болен
V_Card_2 = float(Ver_B)*Ver_Card_Smaller_B/float(Ver_Card_Smaller)

#Вероятность, что Результаты кардиограммы больше среднего уровня + здоров 
V_Card_3 = float(Ver_Z)*Ver_Card_Bigger_Z/float(Ver_Card_Bigger)
#Вероятность, что Результаты кардиограммы больше среднего уровня + болен 
V_Card_4 = float(Ver_B)*Ver_Card_Bigger_B/float(Ver_Card_Bigger)


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
for d in range(len(Sp_MaxP)):
    Symm_MaxP = Symm_MaxP + Sp_MaxP[d]
Middle_MaxP = Symm_MaxP/float(len(Sp_MaxP))
print "-------Среднее значение максимальной величины пульса =",Middle_MaxP

# Подсчитаем  Количество пациентов, у которых максимальная величина пульса меньше среднестатистической
# Подсчитаем  Количество пациентов, у которых максимальная величина пульса больше среднестатистической
kol_MaxP_Bigger = 0
kol_MaxP_Smaller = 0

for d in range(len(Sp_MaxP)):
    if float(Sp_MaxP[d])>=Middle_MaxP:
        kol_MaxP_Bigger =kol_MaxP_Bigger +1
    if float(Sp_MaxP[d])<Middle_MaxP:
        kol_MaxP_Smaller =kol_MaxP_Smaller +1
print "Количество пациентов, у которых максимальная величина пульса меньше среднестатистической =",kol_MaxP_Bigger
print "Количество пациентов, у которых максимальная величина пульса больше среднестатистической=",kol_MaxP_Smaller

# Определим вероятности, что у пациента характер болей больше или меньше
Ver_MaxP_Bigger = kol_MaxP_Bigger/float(kol)
Ver_MaxP_Smaller = kol_MaxP_Smaller/float(kol)

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

for d in range(len(Sp_MaxP)):
    # младшие
    if (float(Sp_MaxP[d])<Middle_MaxP)and (int(Sp_Rez[d])== 1):       
        kol_MaxP_Smaller_Z = kol_MaxP_Smaller_Z+1
    if (float(Sp_MaxP[d])<Middle_MaxP)and (int(Sp_Rez[d])== 2):
        kol_MaxP_Smaller_B = kol_MaxP_Smaller_B+1
    #  старшие  
    if (float(Sp_MaxP[d])>=Middle_MaxP)and (int(Sp_Rez[d])== 1):
        kol_MaxP_Bigger_Z = kol_MaxP_Bigger_Z+1
    if (float(Sp_MaxP[d])>=Middle_MaxP)and (int(Sp_Rez[d])== 2):
        kol_MaxP_Bigger_B = kol_MaxP_Bigger_B+1

Ver_MaxP_Smaller_Z = kol_MaxP_Smaller_Z/float(sym_Z)
Ver_MaxP_Smaller_B = kol_MaxP_Smaller_B/float(sym_B)

Ver_MaxP_Bigger_Z = kol_MaxP_Bigger_Z/float(sym_Z)
Ver_MaxP_Bigger_B = kol_MaxP_Bigger_B/float(sym_B)

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
V_MaxP_1 = float(Ver_Z)*Ver_MaxP_Smaller_Z/float(Ver_MaxP_Smaller)
#Вероятность, что Максимальная величина пульса меньше среднестатистической + болен
V_MaxP_2 = float(Ver_B)*Ver_MaxP_Smaller_B/float(Ver_MaxP_Smaller)

#Вероятность, что Максимальная величина пульса больше среднестатистической + здоров 
V_MaxP_3 = float(Ver_Z)*Ver_MaxP_Bigger_Z/float(Ver_MaxP_Bigger)
#Вероятность, что Максимальная величина пульса больше среднестатистической + болен 
V_MaxP_4 = float(Ver_B)*Ver_MaxP_Bigger_B/float(Ver_MaxP_Bigger)


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
for d in range(len(Sp_Sten)):
    if float(Sp_Sten[d])==0.0:
        kol_Sten_Myj =kol_Sten_Myj +1
    if float(Sp_Sten[d])==1.0:
        kol_Sten_Jen =kol_Sten_Jen +1
print "Количество пациентов, у которых нет стенокардии в анамнезе =",kol_Sten_Myj
print "Количество пациентов, у которых есть стенокардия в анамнезе =",kol_Sten_Jen
# Определим вероятности, что есть ли стенокардия
Ver_Sten_Myj = kol_Sten_Myj/float(kol)
Ver_Sten_Jen = kol_Sten_Jen/float(kol)

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

for d in range(len(Sp_Sten)):
    # есть
    if (float(Sp_Sten[d])==0.0)and (int(Sp_Rez[d])== 1):       
        kol_Sten_Myj_Z = kol_Sten_Myj_Z+1
    if (float(Sp_Sten[d])==0.0)and (int(Sp_Rez[d])== 2):
        kol_Sten_Myj_B = kol_Sten_Myj_B+1
    #  нет  
    if (float(Sp_Sten[d])==1.0)and (int(Sp_Rez[d])== 1):
        kol_Sten_Jen_Z = kol_Sten_Jen_Z + 1
    if (float(Sp_Sten[d])==1.0)and (int(Sp_Rez[d])== 2):
        kol_Sten_Jen_B = kol_Sten_Jen_B+1

Ver_Sten_Myj_Z = kol_Sten_Myj_Z/float(sym_Z) 
Ver_Sten_Myj_B = kol_Sten_Myj_B/float(sym_B)
Ver_Sten_Jen_Z = kol_Sten_Jen_Z/float(sym_Z)
Ver_Sten_Jen_B = kol_Sten_Jen_B/float(sym_B)

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
V_Sten_1 = float(Ver_Z)*Ver_Sten_Myj_Z/float(Ver_Sten_Myj)
#Вероятность, что есть стенокардия в анамнезе + болен
V_Sten_2 = float(Ver_B)*Ver_Sten_Myj_B/float(Ver_Sten_Myj)

#Вероятность, что нет стенокардии в анамнезе + здоров
V_Sten_3 = float(Ver_Z)*Ver_Sten_Jen_Z/float(Ver_Sten_Jen)
#Вероятность, что нет стенокардии в анамнезе + болен
V_Sten_4 = float(Ver_B)*Ver_Sten_Jen_B/float(Ver_Sten_Jen)

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
for d in range(len(Sp_StepTest)):
    Symm_StepTest = Symm_StepTest + Sp_StepTest[d]
Middle_StepTest = Symm_StepTest/float(len(Sp_StepTest))
print "-------Средние данные степ-теста =",Middle_StepTest

# Подсчитаем  Количество пациентов, у которых данные степ-теста больше среднего
# Подсчитаем  Количество пациентов, у которых данные степ-теста меньше среднего
kol_StepTest_Bigger = 0
kol_StepTest_Smaller = 0
for d in range(len(Sp_StepTest)):
    if float(Sp_StepTest[d])>=Middle_StepTest:
        kol_StepTest_Bigger =kol_StepTest_Bigger +1
    if float(Sp_StepTest[d])<Middle_StepTest:
        kol_StepTest_Smaller =kol_StepTest_Smaller +1
print "Количество пациентов, у которых данные степ-теста больше среднего =",kol_StepTest_Bigger
print "Количество пациентов, у которых данные степ-теста меньше среднего =",kol_StepTest_Smaller

# Определим вероятности, что данные больше или меньше 
Ver_StepTest_Bigger = kol_StepTest_Bigger/float(kol)
Ver_StepTest_Smaller = kol_StepTest_Smaller/float(kol)

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
for d in range(len(Sp_StepTest)):
    #меньше
    if (float(Sp_StepTest[d])<Middle_StepTest)and (int(Sp_Rez[d])== 1):       
        kol_StepTest_Smaller_Z = kol_StepTest_Smaller_Z+1
    if (float(Sp_StepTest[d])<Middle_StepTest)and (int(Sp_Rez[d])== 2):
        kol_StepTest_Smaller_B = kol_StepTest_Smaller_B+1
    #  больше  
    if (float(Sp_StepTest[d])>=Middle_StepTest)and (int(Sp_Rez[d])== 1):
        kol_StepTest_Bigger_Z = kol_StepTest_Bigger_Z+1
    if (float(Sp_StepTest[d])>=Middle_StepTest)and (int(Sp_Rez[d])== 2):
        kol_StepTest_Bigger_B = kol_StepTest_Bigger_B+1


Ver_StepTest_Smaller_Z = kol_StepTest_Smaller_Z/float(sym_Z)
Ver_StepTest_Smaller_B = kol_StepTest_Smaller_B/float(sym_B)

Ver_StepTest_Bigger_Z = kol_StepTest_Bigger_Z/float(sym_Z)
Ver_StepTest_Bigger_B = kol_StepTest_Bigger_B/float(sym_B)

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
V_StepTest_1 = float(Ver_Z)*Ver_StepTest_Smaller_Z/float(Ver_StepTest_Smaller)
#Вероятность, что болен, если данные меньше
V_StepTest_2 = float(Ver_B)*Ver_StepTest_Smaller_B/float(Ver_StepTest_Smaller)

#Вероятность, что здоров, если данные больше
V_StepTest_3 = float(Ver_Z)*Ver_StepTest_Bigger_Z/float(Ver_StepTest_Bigger)
#Вероятность, что болен, если данные больше
V_StepTest_4 = float(Ver_B)*Ver_StepTest_Bigger_B/float(Ver_StepTest_Bigger)
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
for d in range(len(Sp_Sklon)):
    Symm_Sklon = Symm_Sklon + Sp_Sklon[d]
Middle_Sklon = Symm_Sklon/float(len(Sp_Sklon))
print "-------Среднее склонение данных =",Middle_Sklon

# Подсчитаем  Количество пациентов, у которых данные больше Среднего склонения
# Подсчитаем  Количество пациентов, у которых данные меньше Среднего склонения
kol_Sklon_Bigger = 0
kol_Sklon_Smaller = 0
for d in range(len(Sp_Sklon)):
    if float(Sp_Sklon[d])>=Middle_Sklon:
        kol_Sklon_Bigger =kol_Sklon_Bigger +1
    if float(Sp_Sklon[d])<Middle_Sklon:
        kol_Sklon_Smaller =kol_Sklon_Smaller +1
print "Количество пациентов, у которых данные больше Среднего склонения =",kol_Sklon_Bigger
print "Количество пациентов, у которых данные меньше Среднего склонения =",kol_Sklon_Smaller

# Определим вероятности, что пациент младше или старше
Ver_Sklon_Bigger = kol_Sklon_Bigger/float(kol)
Ver_Sklon_Smaller = kol_Sklon_Smaller/float(kol)

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
for d in range(len(Sp_Sklon)):
    # меньше
    if (float(Sp_Sklon[d])<Middle_Sklon)and (int(Sp_Rez[d])== 1):       
        kol_Sklon_Smaller_Z = kol_Sklon_Smaller_Z+1
    if (float(Sp_Sklon[d])<Middle_Sklon)and (int(Sp_Rez[d])== 2):
        kol_Sklon_Smaller_B = kol_Sklon_Smaller_B+1
    #  больше 
    if (float(Sp_Sklon[d])>=Middle_Sklon)and (int(Sp_Rez[d])== 1):
        kol_Sklon_Bigger_Z = kol_Sklon_Bigger_Z+1
    if (float(Sp_Sklon[d])>=Middle_Sklon)and (int(Sp_Rez[d])== 2):
        kol_Sklon_Bigger_B = kol_Sklon_Bigger_B+1


Ver_Sklon_Smaller_Z = kol_Sklon_Smaller_Z/float(sym_Z)
Ver_Sklon_Smaller_B = kol_Sklon_Smaller_B/float(sym_B)

Ver_Sklon_Bigger_Z = kol_Sklon_Bigger_Z/float(sym_Z)
Ver_Sklon_Bigger_B = kol_Sklon_Bigger_B/float(sym_B)

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
V_Sklon_1 = float(Ver_Z)*Ver_Sklon_Smaller_Z/float(Ver_Sklon_Smaller)

#Вероятность, что данные меньше + болен
V_Sklon_2 = float(Ver_B)*Ver_Sklon_Smaller_B/float(Ver_Sklon_Smaller)

#Вероятность, что данные больше + здоров
V_Sklon_3 = float(Ver_Z)*Ver_Sklon_Bigger_Z/float(Ver_Sklon_Bigger)
#Вероятность, что данные больше + болен
V_Sklon_4 = float(Ver_B)*Ver_Sklon_Bigger_B/float(Ver_Sklon_Bigger)

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
for d in range(len(Sp_Sosyd)):
    Symm_Sosyd = Symm_Sosyd + Sp_Sosyd[d]
Middle_Sosyd = Symm_Sosyd/float(len(Sp_Sosyd))
print "-------Среднее количество основных сосудов =",Middle_Sosyd

# Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего 
# Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего 
kol_Sosyd_Bigger = 0
kol_Sosyd_Smaller = 0
for d in range(len(Sp_Sosyd)):
    if float(Sp_Sosyd[d])>=Middle_Sosyd:
        kol_Sosyd_Bigger =kol_Sosyd_Bigger +1
    if float(Sp_Sosyd[d])<Middle_Sosyd:
        kol_Sosyd_Smaller =kol_Sosyd_Smaller +1
print "Подсчитаем  Количество пациентов, у которых количество основных сосудов больше Среднего =",kol_Sosyd_Bigger
print "Подсчитаем  Количество пациентов, у которых количество основных сосудов меньше Среднего  =",kol_Sosyd_Smaller

# Определим вероятности, что пациент младше или старше
Ver_Sosyd_Bigger = kol_Sosyd_Bigger/float(kol)
Ver_Sosyd_Smaller = kol_Sosyd_Smaller/float(kol)

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
for d in range(len(Sp_Sosyd)):
    # меньше
    if (float(Sp_Sosyd[d])<Middle_Sosyd)and (int(Sp_Rez[d])== 1):       
        kol_Sosyd_Smaller_Z = kol_Sosyd_Smaller_Z+1
    if (float(Sp_Sosyd[d])<Middle_Sosyd)and (int(Sp_Rez[d])== 2):
        kol_Sosyd_Smaller_B = kol_Sosyd_Smaller_B+1
    #  больше 
    if (float(Sp_Sosyd[d])>=Middle_Sosyd)and (int(Sp_Rez[d])== 1):
        kol_Sosyd_Bigger_Z = kol_Sosyd_Bigger_Z+1
    if (float(Sp_Sosyd[d])>=Middle_Sosyd)and (int(Sp_Rez[d])== 2):
        kol_Sosyd_Bigger_B = kol_Sosyd_Bigger_B+1


Ver_Sosyd_Smaller_Z = kol_Sosyd_Smaller_Z/float(sym_Z)
Ver_Sosyd_Smaller_B = kol_Sosyd_Smaller_B/float(sym_B)

Ver_Sosyd_Bigger_Z = kol_Sosyd_Bigger_Z/float(sym_Z)
Ver_Sosyd_Bigger_B = kol_Sosyd_Bigger_B/float(sym_B)

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
V_Sosyd_1 = float(Ver_Z)*Ver_Sosyd_Smaller_Z/float(Ver_Sosyd_Smaller)
#Вероятность, что количество основных сосудов меньше Среднего + болен
V_Sosyd_2 = float(Ver_B)*Ver_Sosyd_Smaller_B/float(Ver_Sosyd_Smaller)

#Вероятность, что количество основных сосудов больше Среднего + здоров
V_Sosyd_3 = float(Ver_Z)*Ver_Sosyd_Bigger_Z/float(Ver_Sosyd_Bigger)
#Вероятность, что количество основных сосудов больше Среднего + болен
V_Sosyd_4 = float(Ver_B)*Ver_Sosyd_Bigger_B/float(Ver_Sosyd_Bigger)

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
for d in range(len(Sp_SPS)):
    Symm_SPS = Symm_SPS + Sp_SPS[d]
Middle_SPS = Symm_SPS/float(len(Sp_SPS))
print "-------Средняя степень повреждения сосудов =",Middle_SPS

# Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  больше Среднего 
# Подсчитаем  Количество пациентов, у которых степень повреждения сосудов  меньше Среднего 
kol_SPS_Bigger = 0
kol_SPS_Smaller = 0
for d in range(len(Sp_SPS)):
    if float(Sp_SPS[d])>=Middle_SPS:
        kol_SPS_Bigger =kol_SPS_Bigger +1
    if float(Sp_SPS[d])<Middle_SPS:
        kol_SPS_Smaller =kol_SPS_Smaller +1
print "Количество пациентов, у которых степень повреждения сосудов  больше Среднего =",kol_SPS_Bigger
print "Количество пациентов, у которых степень повреждения сосудов  меньше Среднего =",kol_SPS_Smaller

# Определим вероятности, что степень повреждения сосудов меньше или больше 
Ver_SPS_Bigger = kol_SPS_Bigger/float(kol)
Ver_SPS_Smaller = kol_SPS_Smaller/float(kol)

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
for d in range(len(Sp_SPS)):
    # меньше
    if (float(Sp_SPS[d])<Middle_SPS)and (int(Sp_Rez[d])== 1):       
        kol_SPS_Smaller_Z = kol_SPS_Smaller_Z+1
    if (float(Sp_SPS[d])<Middle_SPS)and (int(Sp_Rez[d])== 2):
        kol_SPS_Smaller_B = kol_SPS_Smaller_B+1
    #  больше 
    if (float(Sp_SPS[d])>=Middle_SPS)and (int(Sp_Rez[d])== 1):
        kol_SPS_Bigger_Z = kol_SPS_Bigger_Z+1
    if (float(Sp_SPS[d])>=Middle_SPS)and (int(Sp_Rez[d])== 2):
        kol_SPS_Bigger_B = kol_SPS_Bigger_B+1


Ver_SPS_Smaller_Z = kol_SPS_Smaller_Z/float(sym_Z)
Ver_SPS_Smaller_B = kol_SPS_Smaller_B/float(sym_B)

Ver_SPS_Bigger_Z = kol_SPS_Bigger_Z/float(sym_Z)
Ver_SPS_Bigger_B = kol_SPS_Bigger_B/float(sym_B)

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
V_SPS_1 = float(Ver_Z)*Ver_SPS_Smaller_Z/float(Ver_SPS_Smaller)
#Вероятность, что степень повреждения сосудов  меньше + болен
V_SPS_2 = float(Ver_B)*Ver_SPS_Smaller_B/float(Ver_SPS_Smaller)

#Вероятность, что степень повреждения сосудов больше + здоров
V_SPS_3 = float(Ver_Z)*Ver_SPS_Bigger_Z/float(Ver_SPS_Bigger)
#Вероятность, что степень повреждения сосудов больше + болен
V_SPS_4 = float(Ver_B)*Ver_SPS_Bigger_B/float(Ver_SPS_Bigger)

print "----------------------------------------------"
print "Вероятность, что степень повреждения сосудов меньше + здоров =",V_SPS_1
print "Вероятность, что степень повреждения сосудов меньше + болен=",V_SPS_2
print "Вероятность, что степень повреждения сосудов больше + здоров =",V_SPS_3
print "Вероятность, что степень повреждения сосудов больше + болен =",V_SPS_4
print "----------------------------------------------"

#Списки для итогов 3 вероятностей и начального значения
Spisok_D1 = []
Spisok_D2 = []
Spisok_D3 = []
Spisok_Na4 = []


PathOfFile = "pacient.csv"
f=open(PathOfFile,"rb")
li1 = f.readlines()
f.close()
kk= 0
for stroka in li1:
    Per_Age1,Per_Pol1,Per_Har1,Per_VG1,Per_YH1,Per_YS1,Per_Card1,Per_MaxP1,Per_Sten1,Per_StepTest1,Per_Sklon1,Per_Sosyd1,Per_SPS1,Per_Rez1 = stroka.split()  
    
    print "----------------------------------------Пациент имеет такие атрибуты:"
    print " возраст =",Per_Age1
    print " пол =",Per_Pol1
    print " характер боли в сердце (один из четырех)=",Per_Har1
    print " верхняя граница давления в состоянии покоя	=",Per_VG1
    print " уровень холестерина в крови mg/dl =",Per_YH1
    print " уровень сахара в крови больший 120 mg/dl=",Per_YS1
    print " результаты кардиограммы в состоянии покоя (values 0,1,2)=",Per_Card1
    print " максимальная величина пульса=",Per_MaxP1
    print " наличие стенокардии в анамнезе=",Per_Sten1
    print " данные степ-теста=",Per_StepTest1
    print " склонение данных по степ-тесту=",Per_Sklon1
    print " количество основных сосудов (0-3) выявленных рентгеноскопие =",Per_Sosyd1
    print " степень повреждения сосудов =",Per_SPS1
    print "--------------------------------------------------------"

    print "--------------ПРИМИТИВНЫЙ КЛАССИФКАТОР------------------------------------------"
    per_prim = ''
    #print 'kk =',kk
    #print Prim
    per_prim = Prim[kk]
    if Prim[kk]==1 :
        print " Диагноз = ЗДОРОВ"
    if Prim[kk]==2 :
        print " Диагноз= БОЛЕН"
    print " Вероятность, что пациент здоров = ",Prim_Z[kk]
    print " Вероятность, что пациент болен = ",Prim_B[kk]
       
    if Itog==Per_Rez1:
        print"--------Диагнозы совпали!"
    if Itog<>Per_Rez1:
        print "--------Диагнозы не совпали"
    print "--------------------------------------------------------"
    
    #Определим болен или здоров пациент
    print " Определим диагноз больного по построенному классфикатору:"

    P_Z = 1
    P_B = 1

    #Параметр №1 Возраст
    if float(Per_Age1)<Middle_Age:
        P_Z =float(P_Z) * float(V_Age_1)
        P_B =float(P_B) * float(V_Age_2)
    if float(Per_Age1)>=Middle_Age:
        P_Z = float(P_Z) * float(V_Age_3)
        P_B = float(P_B) * float(V_Age_4)
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
  
    #Параметр №2 Пол
    if float(Per_Pol1)==0.0:
        P_Z =P_Z * V_Pol_1
        P_B =P_B * V_Pol_2
    if float(Per_Pol1)==1.0:
        P_Z =P_Z * V_Pol_3
        P_B =P_B * V_Pol_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
    
    #Параметр №4 верхняя граница давления в состоянии покоя
    if float(Per_VG1)<Middle_VG:
        P_Z =P_Z * V_VG_1
        P_B =P_B * V_VG_2
    if float(Per_VG1)>=Middle_VG:
        P_Z = P_Z * V_VG_3
        P_B = P_B * V_VG_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B

    #Параметр №5 уровень холестерина в крови mg/dl
    if float(Per_YH1)<Middle_YH:
        P_Z =P_Z * V_YH_1
        P_B =P_B * V_YH_2
    if float(Per_YH1)>=Middle_YH:
        P_Z = P_Z * V_YH_3
        P_B = P_B * V_YH_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B

    #Параметр №6 уровень сахара в крови больший 120 mg/dl   
    if float(Per_YS1)<Middle_YH:
        P_Z =P_Z * V_YS_1
        P_B =P_B * V_YS_2
    if float(Per_YS1)>=Middle_YH:
        P_Z = P_Z * V_YS_3
        P_B = P_B * V_YS_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
        
    #Параметр №7 результаты кардиограммы в состоянии покоя (values 0,1,2)
    if float(Per_Card1)<Middle_Card:
        P_Z =P_Z * V_Card_1
        P_B =P_B * V_Card_2
    if float(Per_Card1)>=Middle_Card:
        P_Z = P_Z * V_Card_3
        P_B = P_B * V_Card_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
    
    #Параметр №8 максимальная величина пульса
 #   if float(Per_MaxP1)<Middle_MaxP:
#        P_Z =P_Z * V_MaxP_1
#        P_B =P_B * V_MaxP_2
#    if float(Per_MaxP1)>=Middle_MaxP:
#        P_Z = P_Z * V_MaxP_3
#        P_B = P_B * V_MaxP_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
    
    #Параметр №9 наличие стенокардии в анамнезе
    if float(Per_Sten1)==0.0:
        P_Z =P_Z * V_Sten_1
        P_B =P_B * V_Sten_2
    if float(Per_Sten1)==1.0:
        P_Z =P_Z * V_Sten_3
        P_B =P_B * V_Sten_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
    
    #Параметр №10 данные степ-теста
    if float(Per_StepTest1)<Middle_StepTest:
        P_Z =P_Z * V_StepTest_1
        P_B =P_B * V_StepTest_2
    if float(Per_StepTest1)>=Middle_StepTest:
        P_Z = P_Z * V_StepTest_3
        P_B = P_B * V_StepTest_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B

    #Параметр №11 склонение данных по степ-тесту
    if float(Per_Sklon1)<Middle_Sklon:
        P_Z =P_Z * V_Sklon_1
        P_B =P_B * V_Sklon_2
    if float(Per_Sklon1)>=Middle_Sklon:
        P_Z = P_Z * V_Sklon_3
        P_B = P_B * V_Sklon_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
    
    #Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопие
    if float(Per_Sosyd1)<Middle_Sosyd:
        P_Z =P_Z * V_Sosyd_1
        P_B =P_B * V_Sosyd_2
    if float(Per_Sosyd1)>=Middle_Sosyd:
        P_Z = P_Z * V_Sosyd_3
        P_B = P_B * V_Sosyd_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B
   
    #Параметр №13 степень повреждения сосудов
    if float(Per_SPS1)<Middle_SPS:
        P_Z =P_Z * V_SPS_1
        P_B =P_B * V_SPS_2
    if float(Per_SPS1)>=Middle_SPS:
        P_Z = P_Z * V_SPS_3
        P_B = P_B * V_SPS_4
    #print "вероятность, что пациент здоров = ",P_Z
    #print "вероятность, что пациент болен = ",P_B


    REZ_na4alniy =''
    if Per_Rez1=='1' :
        REZ_na4alniy ='ЗДОРОВ'
        print "Признанный диагноз= ЗДОРОВ"
    if Per_Rez1=='2' :
        REZ_na4alniy ='БОЛЕН'
        print " Признанный диагноз= БОЛЕН"

    #Определим болен или здоров пациент
    print "--------Определим болен или здоров пациент--------"
    print "вероятность, что пациент здоров = ",P_Z
    print "вероятность, что пациент болен = ",P_B
    D2 =0
    if P_B>P_Z:
        Itog_B = 'БОЛЕН'
        D2 = 2
    if P_Z>P_B:
        Itog_B = 'ЗДОРОВ'
        D2 = 1
    if P_Z==P_B:
        Itog_B = 'НЕ понятно'
    print "Диагноз, поставленный программой=",Itog_B   
    if Itog_B==REZ_na4alniy:
        print"--------Диагнозы совпали!"
    if Itog_B<>REZ_na4alniy:
        print "--------Диагнозы не совпали"


    #Определим болен или здоров пациент с учётом рисков
    print "--------Определим болен или здоров пациент с учётом рисков--------"

    Skazat_bolnomy_4to_Zdorov = 15
    Skazat_Zdorovomy_4to_Bolen = 1
    print "Данные исходные "
    print "Сказать больному, что он здоров =",Skazat_bolnomy_4to_Zdorov
    print "Сказать здоровому, что он болен =",Skazat_Zdorovomy_4to_Bolen

    #нормируем
    symma = Skazat_bolnomy_4to_Zdorov+Skazat_Zdorovomy_4to_Bolen
    Skazat_bolnomy_4to_Zdorov1 = Skazat_bolnomy_4to_Zdorov/float(symma)*Ver_B
    Skazat_Zdorovomy_4to_Bolen1 = Skazat_Zdorovomy_4to_Bolen/float(symma)*Ver_Z
    Itog_R = ''
    D3 = 0
    P_B_1 =P_B*Skazat_bolnomy_4to_Zdorov1
    P_Z_1 =P_Z*Skazat_Zdorovomy_4to_Bolen1
    print "вероятность, что пациент здоров с учётом рисков= ",P_Z_1
    print "вероятность, что пациент болен с учётом рисков= ",P_B_1

    D3 = 0
    if P_Z_1<P_B_1:
        Itog_R = 'БОЛЕН'
        D3 = 2
    if P_Z_1>P_B_1:
        Itog_R = 'ЗДОРОВ'
        D3 = 1
    if P_Z_1==P_B_1:
        Itog_R = 'НЕ понятно'
    print "Диагноз, поставленный программой с учётом рисков=",Itog_R
    kk= kk+1

    if Itog_R==REZ_na4alniy:
        print"--------Диагнозы совпали!"
    if Itog_R<>REZ_na4alniy:
        print "--------Диагнозы не совпали"

    #Списки для итогов 3 вероятностей и начального значения
    Spisok_D1.append(D1)
    Spisok_D2.append(D2)
    Spisok_D3.append(D3)
    Spisok_Na4.append(int(Per_Rez1))


print "_________________Оценка классификаторов_________________"
#Примитивный



# Правильно определённые больные
TP1 = 0
# Человек здоров, а его причислили к больному
FP1 = 0
# Человек болен, а его причислили к здоровому
FN1 = 0
# Правильно определённые здоровые
TN1 = 0


#Байесовский
# Правильно определённые больные
TP2 = 0
# Человек здоров, а его причислили к больному
FP2 = 0
# Человек болен, а его причислили к здоровому
FN2 = 0
# Правильно определённые здоровые
TN2 = 0

#Байесовский с учётом рисков
# Правильно определённые больные
TP3 = 0
# Человек здоров, а его причислили к больному
FP3 = 0
# Человек болен, а его причислили к здоровому
FN3 = 0
# Правильно определённые здоровые
TN3 = 0

print Spisok_D1
print Spisok_D2
print Spisok_D3
print Spisok_Na4

for hh in range(len(Spisok_D3)):
#Примитивный
    if (Spisok_Na4[hh]==2) and (Spisok_D1[hh]==2):        
        # Правильно определённые больные
        TP1 = TP1 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D1[hh]==2):        
        # Человек здоров, а его причислили к больному
        FP1 = FP1 + 1
    if (Spisok_Na4[hh]==2) and (Spisok_D1[hh]==1):        
        # Человек болен, а его причислили к здоровому
        FN1 = FN1 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D1[hh]==1):        
        # Правильно определённые здоровые
        TN1 = TN1 + 1
#Байесовский
    if (Spisok_Na4[hh]==2) and (Spisok_D2[hh]==2):        
        # Правильно определённые больные
        TP2 = TP2 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D2[hh]==2):        
        # Человек здоров, а его причислили к больному
        FP2 = FP2 + 1
    if (Spisok_Na4[hh]==2) and (Spisok_D2[hh]==1):        
        # Человек болен, а его причислили к здоровому
        FN2 = FN2 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D2[hh]==1):        
        # Правильно определённые здоровые
        TN2 = TN2 + 1
#Байесовский с учётом рисков
    if (Spisok_Na4[hh]==2) and (Spisok_D3[hh]==2):        
        # Правильно определённые больные
        TP3 = TP3 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D3[hh]==2):        
        # Человек здоров, а его причислили к больному
        FP3 = FP3 + 1
    if (Spisok_Na4[hh]==2) and (Spisok_D3[hh]==1):        
        # Человек болен, а его причислили к здоровому
        FN3 = FN3 + 1
    if (Spisok_Na4[hh]==1) and (Spisok_D3[hh]==1):        
        # Правильно определённые здоровые
        TN3 = TN3 + 1





#Примитивный
NP1=TP1-FN1
NN1=TN1-FP1

#Байесовский 
NP2=TP2-FN2
NN2=TN2-FP2

#Байесовский с учётом рисков
NP3=TP3-FN3
NN3=TN3-FP3

# расчитаем нормировочные уровни
#Примитивный
n_TP1=(TP1/float(NP1))
n_FP1=(FP1/float(FN1))
n_FN1=(FN1/float(NP1))
n_TN1=(TN1/float(NN1))

#Байесовский
n_TP2=(TP2/float(NP2))
n_FP2=(FP2/float(FN2))
n_FN2=(FN2/float(NP2))
n_TN2=(TN2/float(NN2)) 

#Байесовский с учётом рисков
n_TP3=(TP3/float(NP3))
n_FP3=(FP3/float(FN3))
n_FN3=(FN3/float(NP3))
n_TN3=(TN3/float(NN3))



print "---------------------------расчитаем \'precision\' и \'recall\'"

#Примитивный
if (TP1==0)and(FP1==0):
    precision1 = 0
else:
    precision1 =1.0*TP1/float(TP1+FP1)
if (TP1==0)and(FN1==0):
    recall1 = 0
else:
    recall1 = 1.0*TP1/float(TP1+FN1)

#Байесовский
precision2 =TP2/(TP2+FP2)
recall2 = TP2/(TP2+FN2)
if (TP2==0)and(FP2==0):
    precision2 = 0
else:
    precision2 =1.0*TP2/float(TP2+FP2)
if (TP2==0)and(FN2==0):
    recall2 = 0
else:
    recall2= 1.0*TP2/float(TP2+FN2)

#Байесовский с учётом рисков
precision3 =TP3/(TP3+FP3)
recall3 = TP3/(TP3+FN3)
if (TP3==0)and(FP3==0):
    precision3 = 0
else:
    precision3 =1.0*TP3/float(TP3+FP3)
if (TP3==0)and(FN3==0):
    recall3 = 0
else:
    recall3= 1.0*TP3/float(TP3+FN3)


# Выведем полученные значения
print "-------------------------- Примитивный классификатор"

print "--- Число опознаний"
print "TP =",TP1
print "FP =",FP1
print "FN =",FN1
print "TN =",TN1

print "Не расчитываются нормировочные уровни,Точность и отзывчивость не расчитываются, потому что все диагнозы ЗДОРОВ"

print "-------------------------- Байесовский классификатор"

print "--- Число опознаний"
print "TP =",TP2
print "FP =",FP2
print "FN =",FN2
print "TN =",TN2

print "--- нормировочные уровни"
print "n_TP =",n_TP2
print "n_FP =",n_FP2
print "n_FN =",n_FN2
print "n_TN =",n_TN2

print "--- Точность и отзывчивость"
print "precision =",precision2
print "recall =",recall2


print "-------------------------- Байесовский классификатор с учётом рисков"
print "--- Число опознаний"
print "TP =",TP3
print "FP =",FP3
print "FN =",FN3
print "TN =",TN3

print "--- нормировочные уровни"
print "n_TP =",n_TP3
print "n_FP =",n_FP3
print "n_FN =",n_FN3
print "n_TN =",n_TN3

print "--- Точность и отзывчивость"
print "precision =",precision3
print "recall =",recall3


