import time
from Funciones import *
class Reloj:
    def __init__(self):
        self.tiempo=180#En segundos

    def Actualizar(self,a):
        self.mins = str(int(self.tiempo / 60))
        self.secs = str(int(self.tiempo% 60))

        if len(self.mins) == 1:
            self.mins = "0" + self.mins
        if len(self.secs) == 1:
            self.secs = "0" + self.secs
        self.text = "%s : %s" % (self.mins, self.secs)
        #print(self.mins + ":" + self.secs)
        self.tiempo -= 1*a
        printText(self.text,[405,603],80)
