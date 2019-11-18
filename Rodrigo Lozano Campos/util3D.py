import canvas as c
import prism as p
import math


def waste(w, h, l, canvasnotused, order):
    volume = 0
    for i in range (len(canvasnotused)):
        volume += (canvasnotused[i].w * canvasnotused[i].h * canvasnotused[i].l)

    waste = (volume/((w*h*l)*order))*100
    waste = round(waste, 2)
    volume = round(volume, 2)
    totalVolume = w*h*l*order
    return waste, volume, totalVolume


def fitin(canvas, prism):
    if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
        return True, prism
    else:
        aux = prism.w
        prism.w = prism.h
        prism.h = aux
        prism.orientation = 2
        if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
            return True, prism
        else:
            aux = prism.l
            prism.l = prism.h
            prism.h = aux
            prism.orientation = 4
            if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
                return True, prism
            else:
                aux = prism.w
                prism.w = prism.h
                prism.h = aux
                prism.orientation = 3
                if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
                    return True, prism
                else:
                    aux = prism.l
                    prism.l = prism.h
                    prism.h = aux
                    prism.orientation = 5
                    if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
                        return True, prism
                    else:
                        aux = prism.w
                        prism.w = prism.h
                        prism.h = aux
                        prism.orientation = 6
                        if (prism.w <= canvas.w and prism.h <= canvas.h and prism.l <= canvas.l):
                            return True, prism
                        else:
                            aux = prism.l
                            prism.l = prism.h
                            prism.h = aux
                            prism.orientation = 1
                            return False, prism


def collission(prism, cut):
    left = prism.x
    right = prism.xx
    back = prism.y
    front = prism.yy
    bottom = prism.z
    top = prism.zz
    c_left = cut.x
    c_right = cut.xx
    c_back = cut.y
    c_front = cut.yy
    c_bottom = cut.z
    c_top = cut.zz
    return right > c_left and left < c_right and back < c_front and front > c_back and bottom < c_top and top > c_bottom
        

def borders(prism, w, h, l):
    #left = prism.x
    side = prism.xx
    #top = prism.y + prism.h
    front = prism.yy
    top = prism.zz
    return front > h or side > w or top > l


def extra(W, H, L, canvases, prisms, cutted, order):
    for i in range (len(canvases)):
        for j in range (len(prisms)):
            r = p.Prism(prisms[j].label, prisms[j].w, prisms[j].h, prisms[j].l)
            r.x  = canvases[i].x
            r.y  = canvases[i].y
            r.z  = canvases[i].z
            r.xx = r.x + r.w
            r.yy = r.y + r.h
            r.zz = r.z + r.l
            
            if (borders(r, W, H, L)):
                aux = r.w
                r.w = r.h
                r.h = aux
                r.orientation = 2
                if (borders(r, W, H, L)):
                    aux = r.l
                    r.l = r.h
                    r.h = aux
                    r.orientation = 4
                    if (borders(r, W, H, L)):
                        aux = r.w
                        r.w = r.h
                        r.h = aux
                        r.orientation = 3
                        if (borders(r, W, H, L)):
                            aux = r.l
                            r.l = r.h
                            r.h = aux
                            r.orientation = 5
                            if (borders(r, W, H, L)):
                                aux = r.w
                                r.w = r.h
                                r.h = aux
                                r.orientation = 6
                                if (borders(r, W, H, L)):
                                    break

            flag = True
            for k in range (len(cutted)):
                if (cutted[k].sheet == order):    
                    if (collission(r,cutted[k])):
                        flag = False
                        break
            if not flag:
                flag = True
                aux = r.w
                r.w = r.h
                r.h = aux
                r.orientation = 2
                for k in range (len(cutted)):
                    if (cutted[k].sheet == order):    
                        if (collission(r,cutted[k])):
                            flag = False
                            break
            if not flag:
                flag = True
                aux = r.l
                r.l = r.h
                r.h = aux
                r.orientation = 4
                for k in range (len(cutted)):
                    if (cutted[k].sheet == order):    
                        if (collission(r,cutted[k])):
                            flag = False
                            break
            if not flag:
                flag = True
                aux = r.w
                r.w = r.h
                r.h = aux
                r.orientation = 3
                for k in range (len(cutted)):
                    if (cutted[k].sheet == order):    
                        if (collission(r,cutted[k])):
                            flag = False
                            break
            if not flag:
                flag = True
                aux = r.l
                r.l = r.h
                r.h = aux
                r.orientation = 5
                for k in range (len(cutted)):
                    if (cutted[k].sheet == order):    
                        if (collission(r,cutted[k])):
                            flag = False
                            break
            if not flag:
                flag = True
                aux = r.w
                r.w = r.h
                r.h = aux
                r.orientation = 6
                for k in range (len(cutted)):
                    if (cutted[k].sheet == order):    
                        if (collission(r,cutted[k])):
                            flag = False
                            aux = r.l
                            r.l = r.h
                            r.h = aux
                            r.orientation = 1
                            break
            if (flag):
                r.sheet=order
                cutted.append(r)
                """
                    aux = (canvases[i].w*canvases[i].h)-(prisms[j].w*prisms[j].h)
                    if (aux>0):
                        canvases[i].w = round(math.sqrt(aux), 1)
                        canvases[i].h = round(math.sqrt(aux), 1)
                    canvases[i].x=r.x
                    canvases[i].y=r.yy
                """
                prisms.pop(j)
                break


###################################################################################################
#Order functions      
def split(input_list):
    n = len(input_list)
    m = n // 2
    return input_list[:m], input_list[m:]

def merge_sorted_lists(list_left, list_right):
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left
    
    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)

    while len(list_merged) < list_len_target:
        if list_left[index_left].volume >= list_right[index_right].volume:
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1

        if index_right == len(list_right):
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            list_merged += list_right[index_right:]
            break
        
    return list_merged

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)

        return merge_sorted_lists(merge_sort(left), merge_sort(right))
