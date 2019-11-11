from Rectangle import Rectangle

def results(order, waste, area, cuts, rectangles):
    print("Planchas: ", order," plancha utilizada")
    print("Desperdicio: ", waste, "%, Area: ", area, " metros cuadrados")
    print("Cortes: ", cuts)
    print("Plancha ", rectangles[0].sheet)

    for i in range (len(rectangles)):

        print(rectangles[i].label, " ", rectangles[i].x, " ", rectangles[i].y, " ", rectangles[i].orientation)

        if (i+1!=len(rectangles)):
            if (rectangles[i+1].sheet != rectangles[i].sheet):
             print()
             print("Plancha ", rectangles[i+1].sheet)
        
    