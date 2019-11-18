#Clase Prism
class Prism:
    def __init__(self, label, h, w, l):
        self.x = 0
        self.y = 0
        self.z = 0
        self.label = label
        self.h = h
        self.w = w
        self.l = l
        self.volume = w*h*l
        self.room = 1
