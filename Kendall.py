# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scipy
import scipy.stats

# Corelation
##scipy.stats. kendalltau ( X , Y , initial_lexsort = True )
def Kendall (List_Age,List_Pol,List_Har,List_VG,List_YH,List_YS,List_Card,List_MaxP,List_Sten,List_StepTest,List_Sklon,List_Sosyd,List_Sps,List_Rez):
    print '-----------------------KENDALL CORRELATION-----------------------'

    print '-------------Параметр №1 Возраст'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Age,List_Rez)[0]

    print '-------------Параметр №2 Пол'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.spearmanr(List_Pol,List_Rez)[0]

    print '-------------Параметр №3 Характер боли в сердце'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Har,List_Rez)[0]

    print '-------------Параметр №4 верхняя граница давления в состоянии покоя'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_VG,List_Rez)[0]

    print '-------------Параметр №5 уровень холестерина в крови mg/dl'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_YH,List_Rez)[0]

    print '-------------Параметр №6 уровень сахара в крови больший 120 mg/dl'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_YS,List_Rez)[0]

    print '-------------Параметр №7 результаты кардиограммы в состоянии покоя (values 0,1,2)'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Card,List_Rez)[0]

    print '-------------Параметр №8 максимальная величина пульса'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_MaxP,List_Rez)[0]

    print '-------------Параметр №9 наличие стенокардии в анамнезе'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Sten,List_Rez)[0]

    print '-------------Параметр №10 данные степ-теста'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_StepTest,List_Rez)[0]

    print '-------------Параметр №11 склонение данных по степ-тесту'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Sklon,List_Rez)[0]

    print '-------------Параметр №12 количество основных сосудов (0-3) выявленных рентгеноскопие'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Sosyd,List_Rez)[0]

    print '-------------Параметр №13 степень повреждения сосудов'
    print "Взаимсовязь c диагнозом"
    print scipy.stats.kendalltau(List_Sps,List_Rez)[0]