
from prism import Prism
from tkinter import filedialog as fd

def get_file():
    filename = fd.askopenfilename()
    return filename

def get_line(line):
    return [str(n) for n in line.split(' ')]

def set_var(array):

    room_h=int(array[0][0])
    room_w=int(array[0][1])
    room_l=int(array[0][2])

    N=int(array[1][0])

    prisms = []
    for i in range(N):
        n=array[i+2][0]

        label=int(array[i+2][1])
        h=int(array[i+2][2])
        w=int(array[i+2][3])
        l=int(array[i+2][4])

        for j in range(n):
            prisms.append(Prism(label+str(j+1),h,w,l))

    return room_h,room_w,room_l,prisms

def Read():
    """
    Función para leer un archivo y obtener los valores correspondientes
    Devuelve Altura Room, Ancho Room, Largo Room y Arreglo de Prismas
    """
    path = get_file()
    file = open(path,"r")
    f1=file.readlines()
    t = []
    for line in f1:
        t.append(get_line(line))
    return set_var(t)



