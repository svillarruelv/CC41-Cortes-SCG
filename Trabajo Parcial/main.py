import Rectangle as r
import DataIn as di
import cut as cu
from guillotine import guillotine
import Canvas as c
import util as u

def UNO():
    W, H, N, rectangles = di.Read()
    guillotine(W, H, N, rectangles)

def DOS():
    W, H, N, RECTANGLES = di.Read()
    RECTANGLES = u.merge_sort(RECTANGLES)
    ORDER = 1
    CANVAS = c.Canvas(0, 0, W, H, ORDER)
    cu.cut(W,H,N, RECTANGLES, CANVAS, ORDER)


def main():
    n = 3
    while True:
        n = int(input("Ingrese (1) o (2) para ver la distintas soluciones y (0) para salir:"))
        if n==0:
            break
        if n==1:
            UNO()
        if n==2:
            DOS()
main()