import canvas as c
import prism as p
import util3D as u
import dataOut3D as do

def read(path):
    archivo = open(path, 'r')
    data = archivo.read()
    data = data.split()
    print(data)
    w = int(data[0])
    h = int(data[1])
    l = int(data[2])
    n = int(data[3])
    prisms = []
    for i in range(4, len(data), 5):
        for j in range(int(data[i])):
            aux = p.Prism((data[i+1]), (int(data[i+2])), (int(data[i+3])), (int(data[i+4])))
            prisms.append(aux)
    return w, h, l, len(prisms), prisms

W, H, L, N, _PRISMS = read("demo.txt")


_PRISMS = u.merge_sort(_PRISMS)
for i in range(len(_PRISMS)):
    print(_PRISMS[i].w,_PRISMS[i].h,_PRISMS[i].l,_PRISMS[i].label,_PRISMS[i].volume)
print(W, H, L)


ORDER = 1
_CANVAS = c.Canvas(0, 0, 0, W, H, L, ORDER)
canvasnotused = []
cutted = []
cuts = 0
#print(W, H, L, N, CANVAS, PRISMS)

def tridim(W,H,L,N, _PRISMS, _CANVAS, ORDER):

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

                #Corte inferior
                c1 = c.Canvas(prisms[j].xx, prisms[j].y, prisms[j].z,
                canvas.w-prisms[j].w, canvas.h, prisms[j].l, ORDER)
                c2 = c.Canvas(prisms[j].x, prisms[j].yy, prisms[j].z,
                prisms[j].w, canvas.h-prisms[j].h, prisms[j].l, ORDER)
                c3 = c.Canvas(prisms[j].x, prisms[j].y, prisms[j].zz,
                canvas.w, canvas.h, canvas.l-prisms[j].l, ORDER)

                if not (prisms[j] in cutted):
                    cutted.append(prisms[j])
                    prisms.remove(prisms[j])

                divide(c1, prisms)
                divide(c2, prisms)
                divide(c3, prisms)
                
                return

        canvasnotused.append(canvas)

    divide(_CANVAS, _PRISMS)

    #TODO: check this
    if _PRISMS:
        #tienen que ser de ese canvas
        u.extra(W, H, L, canvasnotused, _PRISMS, cutted, ORDER)

    if _PRISMS:
        ORDER += 1
        newcanvas = c.Canvas(0,0,0,W,H,L,ORDER)
        tridim(W,H,L,len(_PRISMS), _PRISMS, newcanvas, ORDER)
        return


    #TODO: make this
    waste, volume, totalVolume = u.waste(W, H, L, canvasnotused, ORDER)
    do.results(ORDER, waste, volume, totalVolume, cuts, cutted)
    #g.set_draws(ORDER, W, H, cutted)
    #g.draw()

tridim(W, H, L, N, _PRISMS, _CANVAS, ORDER)