#Clase Rectangulo
class Prism:
    def __init__(self, label, w, h, l):
        self.x = 0
        self.y = 0
        self.z = 0
        self.label = label
        self.w = w
        self.h = h
        self.l = l
        self.volume = w*h*l
        self.orientation = 1
        self.sheet = 1
        self.xx = 0
        self.yy = 0
        self.zz = 0
