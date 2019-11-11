import util as u
import Canvas as c
import Rectangle as r
import Graphics as g
import DataIn as di
import utilCut as uc
import DataOut as do


# W, H, N, RECTANGLES = di.Read()
# RECTANGLES = u.merge_sort(RECTANGLES)
# ORDER = 1
# CANVAS = c.Canvas(0, 0, W, H, ORDER)

canvasnotused = []
cutted = []
cuts = 0

def cut(W,H,N, RECTANGLES, CANVAS, ORDER):

    def divide(canvas, rectangles):
        if (len(rectangles)<1): 
            canvasnotused.append(canvas)
            return
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

    divide(CANVAS, RECTANGLES)

    if RECTANGLES:
        #tienen que ser de ese canvas
        uc.extra(W, H, canvasnotused, RECTANGLES, cutted, ORDER)

    if RECTANGLES:
        ORDER += 1
        newcanvas = c.Canvas(0,0,W,H,ORDER)
        cut(W,H,len(RECTANGLES), RECTANGLES, newcanvas, ORDER)
        return


    waste, area = uc.waste(W, H, canvasnotused, ORDER)
    do.results(ORDER, waste, area, cuts, cutted)
    g.set_draws(ORDER, W, H, cutted)
    g.draw()

