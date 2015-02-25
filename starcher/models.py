#!/usr/bin/env python
#-*- coding:utf-8 -*-

def Dosificacion(dc, da, pVc, pWa, Vt, dh):
    """Genera los pesos y volumenes de agua, compuesto primario (cp)
    y almidon (alm) siguiendo una proporcion de Vc = pVc Vt y Wa = pWa Wt
    
    dc = densidad compuesto primario
    da = densidad almidon
    pVc = % del volumen total que ocupa el compuesto principal
    pWa = % del peso total que ocupa el almidon
    dh = densidad del agua
    Vt = volumen total en ml
    """

    #Calculo del factor constante gamma
    numGamma = (1 - pVc)*(1 - pWa)*da - pWa*pVc*dc
    denomGamma = (1 - pWa)*da + pWa*dh
    gamma = numGamma / denomGamma

    #Calculo de parametros
    Vh = gamma*Vt
    Wt = ( dc*pVc*Vt + dh*Vh )/(1-pWa)

    Wh = dh*Vh
    Wa = pWa*Wt
    Va = Wa/da
    Vc = pVc*Vt
    Wc = dc*Vc

    #Generacion cadena de resultados
    Res = "Vcp: " + str(round(pVc*100,3)) + "%Vt      Wa: " + str(round(pWa*100,3)) + "%Wt\n\n"
    Res += "Vt: " + str(round(Vt,3)) + " ml      Wt: " + str(round(Wt,3)) + " g\n\n"
    Res += "Vcp: " + str(round(Vc,3)) + " ml      Wcp: " + str(round(Wc,3)) + " g\n\n"
    Res += "Va: " + str(round(Va,3)) + " ml      Wa: " + str(round(Wa,3)) + " g\n\n"
    Res += "Vh: " + str(round(Vh,3)) + " ml      Wh: " + str(round(Wh,3)) + " g"

    return Res
