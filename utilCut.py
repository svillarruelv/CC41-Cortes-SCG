import Canvas as c

def waste(w, h, canvasnotused):
    area = 0
    for i in range (len(canvasnotused)):
        area += (canvasnotused[i].w * canvasnotused[i].h)

    waste = (area//(w*h))*100
    return waste, area


def fitin(canvas, rectangle):
    if (rectangle.w <= canvas.w and rectangle.h <= canvas.h):
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

