
class Room:
    def __init__(self, w, h, l, order):
        self.w = w
        self.h = h
        self.l = l
        self.order = order
        self.volume = w*h*l
        self.volumeused = 0
        self.set = []
    