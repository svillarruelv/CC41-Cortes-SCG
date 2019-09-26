import utilCut as uc
import util as u
import Canvas as c
import Rectangle as r
import Graphics as g
import DataIn as di
import DataOut as do


W, H, N, RECTANGLES = di.Read()
RECTANGLES = u.merge_sort(RECTANGLES)

order = 1
CANVAS = c.Canvas(0, 0, W, H, order)
canvasnotused = []
cutted = []
noncutted = []
cuts = 0

def cut(N, RECTANGLES, CANVAS):

    def divide(canvas, rectangles):
        if (len(rectangles)<1): return
        for j in range (len(rectangles)):
            flag, rectangles[j] = uc.fitin(canvas, rectangles[j])
            if (flag):

                rectangles[j].x = canvas.x
                rectangles[j].y = canvas.y
                rectangles[j].xx = rectangles[j].x+rectangles[j].w
                rectangles[j].yy = rectangles[j].y+rectangles[j].h
                rectangles[j].sheet = canvas.order

                
                #Corte inferior
                c1 = c.Canvas(rectangles[j].xx, rectangles[j].y, 
                canvas.w-rectangles[j].w, canvas.h, order)
                c2 = c.Canvas(rectangles[j].x, rectangles[j].yy,
                rectangles[j].w, canvas.h-rectangles[j].h, order)
                
                """
                #Corte lateral
                c1 = c.Canvas(rectangles[j].xx, rectangles[j].y, 
                canvas.w-rectangles[j].w, rectangles[j].h, order)
                c2 = c.Canvas(rectangles[j].x, rectangles[j].yy,
                canvas.w, canvas.h-rectangles[j].h, order)
                """

                if not (rectangles[j] in cutted):
                    cutted.append(rectangles[j])
                    rectangles.remove(rectangles[j])

                divide(c1, rectangles)
                divide(c2, rectangles)
                
                return

        canvasnotused.append(canvas)

    divide(CANVAS, RECTANGLES)
    uc.extra(W, H, canvasnotused, RECTANGLES, cutted)

    for i in range(len(RECTANGLES)):
        print(RECTANGLES[i].label)

    waste, area = uc.waste(W, H, canvasnotused)
    do.results(order, waste, area, cuts, cutted)
    g.set_draws(W, H, cutted)
    g.draw()


cut(N, RECTANGLES, CANVAS)