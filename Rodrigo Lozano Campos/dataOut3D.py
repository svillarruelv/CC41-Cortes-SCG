import prism as p

def results(order, waste, volume, totalVolume, cuts, prisms):
    print("Contenedores usados: ", order)
    print("Volumen disponible: ", totalVolume, "m3")
    print("Volumen ocupado: ", totalVolume-volume,"m3 (",100-waste,"%)")
    print("Cajas a transportar: ", len(prisms))
    print("Contenedor \t Formato \t\t Coordenadas \t\t\t Orientacion")

    for i in range (len(prisms)):
        print(prisms[i].sheet,   "\t\t\t", prisms[i].label,"\t",(prisms[i].x,prisms[i].y,prisms[i].z),  "\t\t\t\t", prisms[i].orientation)