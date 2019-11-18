import canvas as c
import prism as p
import util3D as u
import dataOut3D as do
import graphics3D as g

def read(path):
    archivo = open(path, 'r')
    data = archivo.read()
    data = data.split()

    w = int(data[0])
    h = int(data[1])
    l = int(data[2])
    n = int(data[3])
    prisms = []
    for i in range(4, len(data), 5):
        for j in range(int(data[i])):
            aux = p.Prism((data[i+1]), (int(data[i+3])), (int(data[i+4])), (int(data[i+2])))
            prisms.append(aux)
    return w, h, l, len(prisms), prisms

L, W, H, N, _PRISMS = read("Rodrigo Lozano Campos\demo.txt")


_PRISMS = u.merge_sort(_PRISMS)

#for i in range(len(_PRISMS)):
#    print(_PRISMS[i].w,_PRISMS[i].h,_PRISMS[i].l,_PRISMS[i].label,_PRISMS[i].volume)
#print(W, H, L)
cuts = 0

ORDER = 1
_CANVAS = c.Canvas(0, 0, 0, W, H, L, ORDER)
canvasnotused = []
cutted = []
#print(W, H, L, N, CANVAS, PRISMS)

def tridim(W,H,L,N, _PRISMS, _CANVAS, ORDER, cutType):

    def divide(canvas, prisms):
        if (len(prisms)<1): 
            canvasnotused.append(canvas)
            return
        for j in range (len(prisms)):
            flag, prisms[j] = u.fitin(canvas, prisms[j])
            if (flag):

                prisms[j].x = canvas.x
                prisms[j].y = canvas.y
                prisms[j].z = canvas.z
                prisms[j].xx = prisms[j].x+prisms[j].w
                prisms[j].yy = prisms[j].y+prisms[j].h
                prisms[j].zz = prisms[j].z+prisms[j].l
                prisms[j].sheet = canvas.order

                #Cortes1
                if cutType ==1:
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, canvas.h, prisms[j].l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    prisms[j].w, canvas.h-prisms[j].h, prisms[j].l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    canvas.w, canvas.h, canvas.l-prisms[j].l, ORDER)
                elif cutType == 2:
                    #Cortes2
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, prisms[j].h, prisms[j].l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    canvas.w, canvas.h-prisms[j].h, prisms[j].l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    canvas.w, canvas.h, canvas.l-prisms[j].l, ORDER)
                elif cutType == 3:
                    #Cortes3
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, canvas.h, canvas.l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    prisms[j].w, canvas.h-prisms[j].h, prisms[j].l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    prisms[j].w, canvas.h, canvas.l-prisms[j].l, ORDER)
                elif cutType == 4:
                    #Cortes4
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, prisms[j].h, prisms[j].l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    canvas.w, canvas.h-prisms[j].h, canvas.l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    canvas.w, prisms[j].h, canvas.l-prisms[j].l, ORDER)
                elif cutType == 5:
                    #Cortes5
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, canvas.h, canvas.l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    prisms[j].w, canvas.h-prisms[j].h, canvas.l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    prisms[j].w, prisms[j].h, canvas.l-prisms[j].l, ORDER)
                elif cutType == 6:
                    #Cortes6
                    c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                    canvas.w-prisms[j].w, prisms[j].h, canvas.l, ORDER)
                    c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                    canvas.w, canvas.h-prisms[j].h, canvas.l, ORDER)
                    c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                    prisms[j].w, prisms[j].h, canvas.l-prisms[j].l, ORDER)


                if not (prisms[j] in cutted):
                    cutted.append(prisms[j])
                    prisms.remove(prisms[j])

                divide(c1, prisms)
                divide(c2, prisms)
                divide(c3, prisms)
                
                return

        canvasnotused.append(canvas)

    divide(_CANVAS, _PRISMS)

    if _PRISMS:
        u.extra(W, H, L, canvasnotused, _PRISMS, cutted, ORDER)

    if _PRISMS:
        ORDER += 1
        newcanvas = c.Canvas(0,0,0,W,H,L,ORDER)
        tridim(W,H,L,len(_PRISMS), _PRISMS, newcanvas, ORDER, cutType)
        return

    waste, volume, totalVolume = u.waste(W, H, L, canvasnotused, ORDER)
    do.results(ORDER, waste, volume, totalVolume, cuts, cutted)
    g.graph(ORDER, cutted)

tridim(W, H, L, N, _PRISMS, _CANVAS, ORDER, 6)