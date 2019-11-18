from DataIn import *
from DataOut import *
from prism import Prism
from room import Room

def collition(p1,p2):
    
    x_min = p1.x
    x_max = p1.x + p1.l
    x_min2 = p2.x
    x_max2 = p2.x + p2.l 

    y_min = p1.y 
    y_max = p1.y + p1.w 
    y_min2 = p2.y 
    y_max2 = p2.y + p2.w 

    z_min = p1.z 
    z_max = p1.z + p1.h 
    z_min2 = p2.z 
    z_max2 = p2.z + p2.h
    
    isColliding = ((x_max >= x_min2 and x_max <= x_max2) or (x_min <= x_max2 and x_min >= x_min2)) and ((y_max >= y_min2 and y_max <= y_max2) or (y_min <= y_max2 and y_min >= y_min2)) and ((z_max >= z_min2 and z_max <= z_max2) or (z_min <= z_max2 and z_min >= z_min2))
              
    return isColliding

H,W,L,prisms=Read()

rooms = []
r_index = 0
r = Room(W,H,L,r_index+1)
rooms.append(r)
for prism in prisms:
    #Verificar que la pieza no se haya colocado aun
    if prism.room == 0:
        
        if(len(rooms[r_index].set)==0):
                    prism.room = r_index+1
                    rooms[r_index].volumeused += prism.volume
                    rooms[r_index].set.append(prism)
                    continue

        #Probar las distintas rotaciones
        rotation=1
        while(rotation<7):
            prism.rotate(rotation)
            for prism2 in rooms[r_index].set:
                if collition(prism,prism2):
                    prism.x = prism2.x + prism2.l
                    print("HOLA")
                # if collition(prism,prism2) or prism.x+prism.l > L:
                if prism.x+prism.l > L:
                    prism.x = prism2.x
                    prism.y = prism2.y + prism2.w
                    print("HOLAA")
                # if collition(prism,prism2) or prism.y+prism.w > W:
                if prism.y+prism.w > W:
                    prism.x = prism2.x
                    prism.y = prism2.y
                    prism.z = prism2.z + prism2.h
                    print("HOLAAA")
            if prism.x + prism.l <= rooms[r_index].l and prism.y + prism.w <= rooms[r_index].w and prism.z + prism.h <= rooms[r_index].h:
                prism.room = r_index+1
                rooms[r_index].volumeused += prism.volume
                rooms[r_index].set.append(prism)
                rotation=7
                print("PUDE ENTRAR")
                break
            if rotation == 6:
                    r_index += 1
                    rotation = 1
                    rooms.append(Room(W,H,L,r_index+1))
                    print("HOLAAAA")
            print("PALSIGUIENTE")
            rotation += 1
totalvol=0
totalvolwasted=0
for room in rooms:
    totalvol += room.volume
    print(room.volumeused)
    totalvolwasted += room.volumeused

results(len(rooms),totalvolwasted,totalvol,prisms)

