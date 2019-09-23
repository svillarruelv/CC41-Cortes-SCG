import util as u
import Rectangle as r
import DataIn as di

"""
r1 = r.Rectangle(0, 0,"A", 40, 10)

r2 = r.Rectangle(0, 0,"B", 10, 20)

r3 = r.Rectangle( 0, 0,"C", 300, 2)

a=[]
a.append(r1)
a.append(r2)
a.append(r3)
a = [3,1,8,46,5841,8,452,2]

b = u.merge_sort(a)

for i in range(len(b)):
    print(b[i].label)
    print(b[i].area)

W = 720
H = 670

"""

W, H, N, rectangles = di.Read(demo.txt)
u.merge_sort(rectangles)

def guillotine(W, H, N, rectangles):
    aux = rectangles[0]
    rectangles = rectangles[1:]



