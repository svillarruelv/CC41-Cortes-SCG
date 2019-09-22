import util as u
import Rectangle as r

r1 = r.Rectangle(0, 0,"A", 40, 10)

r2 = r.Rectangle(0, 0,"B", 10, 20)

r3 = r.Rectangle( 0, 0,"C", 300, 2)


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

W = 720
H = 670


