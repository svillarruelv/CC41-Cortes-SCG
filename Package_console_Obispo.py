#!/usr/bin/env python
# coding: utf-8

# In[30]:


def ordenamientoBurbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j][4] < lista[j+1][4]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;


# In[31]:


#para las figuras repetidas
def Repetidos(elem):
    for _ in elem:
        #Agregar condicional para que no agregue mas de una area
        _.append(_[1]*_[2])
        while(_[3]>1):
            _[3]-=1
            elem.append(_)


# In[32]:


def RotarRect(Element):
    aux=Element[1]
    Element[1]=Element[2]
    Element[2]=aux
    #Si se ha rotado, le agrego un 1
    Element.append(1)


# In[109]:


def Fit(E,P,GG):
#si no fitea, entonces lo voltea y prueba de nuevo
    if(E[1]<=P[2] and E[2]<=P[3]):
    #siempre tratar de ocupar el menor espacio posible
        aux1=E[1]/P[2] + E[2]/P[3]
        aux2=E[2]/P[2] + E[1]/P[3]
        if(aux1>aux2): #si su posicion normal ocupa mas que la girada: se gira
            RotarRect(E)
        else:
        #si no se ha rotado le pongo '0'
            E.append(0)
    else:
        if(GG==1):
            
            return False
        RotarRect(E)
        Fit(E,P,1)    
    return True    
#si ya no fitea por nada del mundo crear otra plancha con las restantes


# In[100]:


import math
def BestFit(E,PC,R):
    Rx=[]
    Rx1=[]
    total=0
    total1=0
    for elem in E:
        if(len(E)==1):
            return R
        if(Fit(elem,PC,0)):
            #Datos del nodo
            node=[elem[0],PC[0],PC[1],E[0][5],elem[4]]
            R.append(node)
            return R
            #Al colocar un elemento se crean partes
            #Entre más parecidas(cuadradas) las partes, mejor
            #cuanto mas espacio dejas mas arriesgas a perder
            
            
        y=(PC[2]-elem[1])*(PC[3]) - (elem[1])*(PC[3]-elem[2])
        x=(PC[2]-elem[1])*(elem[2]) - (PC[2])*(PC[3]-elem[2])
        pc=PC
        pc1=PC
        if(math.fabs(x)>math.fabs(y)):
            pc[0]=elem[1]
            pc1[2]=elem[1]
            pc1[1]=elem[2]
            
            Rx=BestFit(E[1:],pc,R)
        else:
            pc[0]=elem[1]
            pc[3]=elem[2]
            pc1[1]=elem[2]
    #al dividir el canvas en dos, se fitean las piezas que mejor quepan al lado del primer bloque
            #if()
            
            Rx1=BestFit(E[1:],pc1,R)
        for node in Rx:
            total+=node[4]
        for node in Rx1:
            total1+=node[4]
        if(total>total1):
            a=total/(PC[2]*PC[3])
            Rx.append(a)
            return R.extend(Rx)
        else:
            a=total1/(PC[2]*PC[3])
            Rx1.append(a)
            return R.extend(Rx1)
        
    #pc[2]=E[0][2]
    #pc2[3]=E[0][2]

    #Rpta2 = BestFit(E[1:],pc,R) + BestFit(E[1:],pc2,R)

    #print(Rpta2)
    #print(Rpta1)


# In[110]:


R=[]
PC=[0,0,720,670]
rectangulos=[[1,120,120,1],[2,285,130,1],[3,200,300,1],[4,165,320,1],[5,235,470,1],[6,200,170,1],[7,285,220,1],[8,555,200,1]]
Repetidos(rectangulos)
ordenamientoBurbuja(rectangulos,len(rectangulos))
#print(rectangulos)
BestFit(rectangulos,PC,R)


# In[ ]:




