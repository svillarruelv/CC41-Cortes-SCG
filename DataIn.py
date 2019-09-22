
import Rectangle

def getline(line):
    return [str(n) for n in line.split(' ')]


def set_var(array):
    sheet_w=int(array[0][0])
    sheet_h=int(array[0][1])
    n=int(array[1][0])
    rectangles = []
    for i in range(n):
        l=array[i+2][0]
        w=int(array[i+2][1])
        h=int(array[i+2][2])
        p=int(array[i+2][3])
        for j in range(p):
            rectangles.append(Rectangle(0,0,l+str(j+1),w,h))
    return sheet_w,sheet_h,n,rectangles


def Read(path):
    """
    Función para leer un archivo y obtener los valores
    Devuelve Width de Plano, Height de Plano, Número de rectangulos y Arreglo de rectangulos
    """
    file = open(path,"r")
    f1=file.readlines()
    t = []
    for line in f1:
        t.append(getline(line))
    return set_var(t)







