import Canvas as c
import Rectangle as rec
import math

def waste(w, h, canvasnotused):
    area = 0
    for i in range (len(canvasnotused)):
        area += (canvasnotused[i].w * canvasnotused[i].h)

    waste = (area/(w*h))*100
    waste = round(waste, 2)
    return waste, area


def fitin(canvas, rectangle):
    if (rectangle.w <= canvas.w+2 and rectangle.h <= canvas.h+2):
        return True, rectangle
    else:
        aux = rectangle.w
        rectangle.w = rectangle.h
        rectangle.h = aux
        rectangle.orientation = "G"
        if (rectangle.w <= canvas.w and rectangle.h <= canvas.h):
            return True, rectangle
        else:
            aux = rectangle.w
            rectangle.w = rectangle.h
            rectangle.h = aux
            rectangle.orientation = "N"
            return False, rectangle


def collission(rectangle, cut):
    left = rectangle.x
    right = rectangle.xx
    top = rectangle.y
    bottom = rectangle.yy
    c_left = cut.x
    c_right = cut.xx
    c_top = cut.y
    c_bottom = cut.yy
    return right >= c_left and left <= c_right and top >= c_bottom and bottom <= c_top 
        

def borders(rectangle, w, h):
    #left = rectangle.x
    right = rectangle.xx
    #top = rectangle.y + rectangle.h
    bottom = rectangle.yy
    return bottom > h or right > w


def extra(W, H, canvases, rectangles, cutted):
    for i in range (len(canvases)):
        for j in range (len(rectangles)):
            r = rec.Rectangle(canvases[i].x, canvases[i].y, rectangles[j].label, rectangles[j].w, rectangles[j].h)
            r.xx = r.x + r.w
            r.yy = r.y + r.h
            if not (borders(r, W, H)):
                flag = True
                for k in range (len(cutted)):
                    if (collission(r,cutted[k])):
                        flag = False
                        break;
                if (flag):
                    cutted.append(r)
                    
                    aux = (canvases[i].w+canvases[i].h)-(rectangles[j].w+rectangles[j].h)
                    canvases[i].w = math.sqrt(aux)
                    canvases[i].h = math.sqrt(aux)

                    rectangles.pop(j)
                    break



            








"""
def divide(canvas, rectangles):
    for j in range (len(rectangles)):
        flag, rectangles[j] = fitin(canvas, rectangles[j])
        if (flag):

            rectangles[j].x = canvas.x
            rectangles[j].y = canvas.y
            rectangles[j].xx = rectangles[j].x+rectangles[j].w
            rectangles[j].yy = rectangles[j].y+rectangles[j].h
            rectangles[j].sheet = canvas.order

            cutted.append(rectangles[j])


            c1 = c.Canvas(rectangles[j].xx, rectangles[j].y, 
            canvas.w-rectangles[j].w, canvas.h, order)
            c2 = c.Canvas(rectangles[j].x, rectangles[j].yy,
            rectangles[j].w, canvas.h-rectangles[j].h, order)

            rectangles = rectangles[j:]

            divide(c1, rectangles)
            divide(c2, noncutted)
                

        else:
            noncutted.append(rectangles[j])


TODO:
def wichbest(canvas, rectangle):

    can1 = c.Canvas(canvas.x, canvas., )

    if ()
    return 
"""

