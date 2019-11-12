import canvas as c
import prism as p

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
            aux = p.Prism((data[i+1]), (int(data[i+2])), (int(data[i+3])), (int(data[i+4])))
            prisms.append(aux)
    return w, h, l, n, prisms

W, H, L, N, _PRISMS = read("Rodrigo Lozano Campos\demo.txt")
 
_CANVAS = c.Canvas(0, 0, 0, W, H, L, 1)
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
            flag, prisms[j] = uc.fitin(canvas, prisms[j])
            if (flag):

                rectangles[j].x = canvas.x
                rectangles[j].y = canvas.y
                rectangles[j].xx = rectangles[j].x+rectangles[j].w
                rectangles[j].yy = rectangles[j].y+rectangles[j].h
                rectangles[j].sheet = canvas.order

                #Corte inferior
                c1 = c.Canvas(rectangles[j].xx, rectangles[j].y, 
                canvas.w-rectangles[j].w, canvas.h, ORDER)
                c2 = c.Canvas(rectangles[j].x, rectangles[j].yy,
                rectangles[j].w, canvas.h-rectangles[j].h, ORDER)
                
                """
                #Corte lateral
                c1 = c.Canvas(rectangles[j].xx, rectangles[j].y, 
                canvas.w-rectangles[j].w, rectangles[j].h, ORDER)
                c2 = c.Canvas(rectangles[j].x, rectangles[j].yy,
                canvas.w, canvas.h-rectangles[j].h, ORDER)
                """

                if not (rectangles[j] in cutted):
                    cutted.append(rectangles[j])
                    rectangles.remove(rectangles[j])

                divide(c1, rectangles)
                divide(c2, rectangles)
                
                return

        canvasnotused.append(canvas)
