import util as u
import Rectangle as r
import DataIn as di
import Graphics as g


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

g.set_draws(W,H,rectangles)
g.draw()
"""

W, H, N, rectangles = di.Read()
#u.merge_sort(rectangles)

def guillotine(W, H, N, rectangles):
    rectangles = u.merge_sort(rectangles)

    if (N < 1):
        g.set_draws(W, H, rectangles)
        g.draw()
        return
    
    aux = rectangles[0]

    aux.x = 0
    aux.y = 0
    aux.xx = aux.x + aux.w
    aux.yy = aux.y + aux.h
    actualx = aux
    actualy = aux

    cutted = []
    noncutted = []
    cutted.append(aux)

    for i in range (1, len(rectangles)):

        cut, rectangles[i] = u.fit(rectangles[i], actualx, actualy, W, H)
        if (cut == 1):
            rectangles[i].x=actualx.xx
            rectangles[i].y=actualy.y
            rectangles[i].xx=rectangles[i].w+rectangles[i].x
            rectangles[i].yy=rectangles[i].h+rectangles[i].y
            actualx=rectangles[i]
            cutted.append(rectangles[i])
        elif(cut == 2):
            rectangles[i].x=aux.x
            rectangles[i].y=actualy.yy
            rectangles[i].xx=rectangles[i].w+rectangles[i].x
            rectangles[i].yy=rectangles[i].h+rectangles[i].y
            actualy=rectangles[i]
            actualx=rectangles[i]
            cutted.append(rectangles[i])
        elif(cut==3):
            noncutted.append(rectangles[i])
            print("La pieza ", rectangles[i].label, " no ha sido cortada")

    for i in range(len(rectangles)):
        print(rectangles[i].label, rectangles[i].orientation)

    for i in range(len(noncutted)):
        print(noncutted[i].label)

    #TODO: recursividad con el arreglo noncutted para terminar de acomodar las piezas en los espacios sobrantes
    g.set_draws(W,H,cutted)
    g.draw()


guillotine(W, H, N, rectangles)
