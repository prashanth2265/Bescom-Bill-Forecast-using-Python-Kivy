from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label

hcons=""
hcos=""
wcons=""
wcos=""

class MainWindow(Screen):
    pass

class HOMEMETER(Screen):
    hbillr = ObjectProperty(None)
    hmeterr = ObjectProperty(None)

    def hbtn(self):
        homeconsumed(self.hbillr.text, self.hmeterr.text)
        self.hbillr.text = ""
        self.hmeterr.text = ""

def homeconsumed(a,b):
    global hcons, hcos
    def slab(self):
        if self > 30:
            s1 = self - 30
            if s1 > 70:
                s2 = s1 - 70
                return (30 * 3.75) + (70 * 5.2) + (s2 * 6.75)
            else:
                return (30 * 3.75) + (s1 * 5.2)
        else:
            return self * 3.75

    hconsumed = int(b) - int(a)
    tax = (slab(hconsumed) + 200) * 0.04
    hcost = slab(hconsumed) + 200 + tax + (hconsumed * .12)
    hcons=hconsumed
    hcos=round(hcost,2)

class HOUTPUT(Screen):
    hconsumed = ObjectProperty(None)
    hcost = ObjectProperty(None)

    def on_enter(self, *args):
        self.hconsumed.text = "Untis: " + str(hcons)
        self.hcost.text = "Cost: " + str(hcos)

class WATERPUMPMETER(Screen):
    wbillr = ObjectProperty(None)
    wmeterr = ObjectProperty(None)

    def wbtn(self):
        waterconsumed(self.wbillr.text, self.wmeterr.text)
        self.wbillr.text = ""
        self.wmeterr.text = ""

def waterconsumed(a, b):
    global wcons, wcos
    def slab(self):
        if self > 30:
            s1 = self - 30
            if s1 > 70:
                s2 = s1 - 70
                return (30 * 3.75) + (70 * 5.2) + (s2 * 6.75)
            else:
                return (30 * 3.75) + (s1 * 5.2)
        else:
            return self * 3.75
    wconsumed = int(b) - int(a)
    Fixed_charges = 95
    FAC = wconsumed * .12
    tax = (slab(wconsumed) + Fixed_charges) * 0.04
    wcost = slab(wconsumed) + Fixed_charges + tax + FAC
    wcons= wconsumed
    wcos= round(wcost,2)

class WOUTPUT(Screen):
    wconsumed = ObjectProperty(None)
    wcost = ObjectProperty(None)

    def on_enter(self, *args):
        self.wconsumed.text = "Untis: " + str(wcons)
        self.wcost.text = "Cost: " +  str(wcos)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("meter.kv")

class meter(App):
    def build(self):
        return kv

if __name__ == "__main__":
    meter().run()
