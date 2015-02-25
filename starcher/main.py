#!/usr/bin/env python
#-*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from models import Dosificacion

class ResPopup(Popup):
    
    dosif = ObjectProperty('')

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    
class CalcDosifForm(BoxLayout):
    
    dc = ObjectProperty()
    da = ObjectProperty()
    pVc = ObjectProperty()
    pWa = ObjectProperty()
    tv = ObjectProperty()
    dh = ObjectProperty()
    
    def calcular(self):
        res = ResPopup()
        # Dosificacion(dc, da, pVc, pWa, Vt, dh)
        res.dosif = Dosificacion(float(self.dc.text), float(self.da.text), 
                                float(self.pVc.text)/100.0, float(self.pWa.text)/100.0, 
                                float(self.tv.text), float(self.dh.text))
        res.open()

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

class CalcDosifApp(App):
    pass

# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

if __name__ == '__main__':
    CalcDosifApp().run()
