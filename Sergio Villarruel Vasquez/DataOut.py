import prism as p

def results(order, volume, totalVolume, prisms):
    waste = volume/totalVolume
    print("Contenedores usados: ", order)
    print("Volumen disponible: ", totalVolume, "m3")
    print("Volumen ocupado: ", volume, "m3 (", round(100*waste,2),"%)")
    print("Cajas a transportar: ", len(prisms))
    print("Contenedor \t Formato \t Coordenadas \t\t\t Orientacion")

    for i in range (len(prisms)):
        print(prisms[i].room, "\t\t\t\t\t", prisms[i].label, "\t\t\t\t", "(",prisms[i].x,", ",prisms[i].y,", ",prisms[i].z,")", "\t", prisms[i].orientation)