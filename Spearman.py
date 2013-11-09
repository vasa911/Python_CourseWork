# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scipy
import scipy.stats

# Corelation
#scipy.stats.spearmanr(a, b=None, axis=0)[source]
#scipy.stats. kendalltau ( X , Y , initial_lexsort = True )
def Spearman (Sp_Age,Sp_Pol,Sp_VG,Sp_YH,Sp_YS,Sp_Card,Sp_MaxP,Sp_Sten,Sp_StepTest,Sp_Sklon,Sp_Sosyd,Sp_SPS,Sp_Rez):
    print '-----------------------SPEARMAN CORRELATION-----------------------'
    print '-------------Параметр №1 Возраст'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Age,Sp_Rez)[0]

    print '-------------Параметр №2 Пол'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Pol,Sp_Rez)[0]

    print '-------------Параметр №4 верхняя граница давления в состоянии покоя'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_VG,Sp_Rez)[0]

    print '-------------Параметр №5 уровень холестерина в крови mg/dl'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_YH,Sp_Rez)[0]

    print '-------------Параметр №6 уровень сахара в крови больший 120 mg/dl'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_YS,Sp_Rez)[0]

    print '-------------Параметр №7 результаты кардиограммы в состоянии покоя (values 0,1,2)'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Card,Sp_Rez)[0]

    print '-------------Параметр №8 максимальная величина пульса'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_MaxP,Sp_Rez)[0]

    print '-------------Параметр №9 наличие стенокардии в анамнезе'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Sten,Sp_Rez)[0]

    print '-------------Параметр №10 данные степ-теста'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_StepTest,Sp_Rez)[0]

    print '-------------Параметр №11 склонение данных по степ-тесту'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Sklon,Sp_Rez)[0]

    print '-------------Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопие'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_Sosyd,Sp_Rez)[0]

    print '-------------Параметр №13 степень повреждения сосудов'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(Sp_SPS,Sp_Rez)[0]