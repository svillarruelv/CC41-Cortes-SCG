import util as u

class Rectangle:
    def __init__(self, l, x, y, w, h):
        self.x = x
        self.y = y
        self.label = l
        self.w = w
        self.h = h
        self.area = w*h
        self.orientation = "N"
        self.sheet = 1

r1 = Rectangle("A", 0, 0, 40, 10)

r2 = Rectangle("B", 0, 0, 10, 20)

r3 = Rectangle("C", 0, 0, 300, 2)


#print(r1.x, r1.y, r1.label, r1.w, r1.h, r1.orientation, r1.sheet, r1.area)

a=[]
a.append(r1)
a.append(r2)
a.append(r3)
#a = [3,1,8,46,5841,8,452,2]

b = u.merge_sort(a)

for i in range(len(b)):
    print(b[i].label)
    print(b[i].area)
