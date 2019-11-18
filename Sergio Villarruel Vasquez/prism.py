
class Prism:
    def __init__(self, label, h, w, l):
        self.x = 0
        self.y = 0
        self.z = 0
        self.label = label
        self.h = h
        self.w = w
        self.l = l
        self.height = h
        self.width = w
        self.large = l
        self.volume = w*h*l
        self.room = 0
        self.orientation=1

    def rotate(self, n):
        self.x=0
        self.y=0
        self.z=0
        self.orientation = n
        if n == 1:
            self.h = self.height
            self.w = self.width
            self.l = self.large
        elif n==2:
            self.h = self.height
            self.w = self.large
            self.l = self.width
        elif n==3:
            self.h = self.width
            self.w = self.height
            self.l = self.large
        elif n==4:
            self.h = self.width
            self.w = self.large
            self.l = self.height
        elif n==5:
            self.h = self.large
            self.w = self.height
            self.l = self.width
        elif n==6: 
            self.h = self.large
            self.w = self.width
            self.l = self.height