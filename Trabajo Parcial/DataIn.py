
from Rectangle import Rectangle
from tkinter import filedialog as fd

def get_file():
    filename = fd.askopenfilename()
    return filename

def get_line(line):
    return [str(n) for n in line.split(' ')]

def set_var(array):

    sheet_w=int(array[0][0])

    #Validación Width
    if sheet_w < 0 :
        print("Número invalido de Width")
        return 0,0,0,0

    sheet_h=int(array[0][1])

    #Validación Height
    if sheet_h < 0 :
        print("Número invalido de Height")
        return 0,0,0,0

    n=int(array[1][0])

    #Validación número de cuadrados
    if n < 0:
        print("Número invalido de cuadrados")
        return 0,0,0,0

    rectangles = []
    for i in range(n):
        l=array[i+2][0]
        w=int(array[i+2][1])
        h=int(array[i+2][2])
        #Validación w,h cuadrado
        if w>sheet_w or h>sheet_h:
            print("La pieza",l,"es más grande que la plancha")
            return 0,0,0,0
        if w<0:
            print("Número invalido de Width de la pieza", l)
            return 0,0,0,0
        if h<0:
            print("Número invalido de Height de la pieza", l)
            return 0,0,0,0

        p=int(array[i+2][3])
        for j in range(p):
            rectangles.append(Rectangle(0,0,l+str(j+1),w,h))
    #Validación de labels
    for i in range(len(rectangles)):
        for j in range(i+1,len(rectangles)):
            if rectangles[i].label==rectangles[j].label:
                print("Se repite el label", rectangles[i].label)
                return 0,0,0,0
    return sheet_w,sheet_h,n,rectangles

def Read():
    """
    Función para leer un archivo y obtener los valores correspondientes
    Devuelve Width de Plano, Height de Plano, Número de rectangulos y Arreglo de rectangulos
    """
    path = get_file()
    file = open(path,"r")
    f1=file.readlines()
    t = []
    for line in f1:
        t.append(get_line(line))
    return set_var(t)



