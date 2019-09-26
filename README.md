# Trabajo Parcial de Complejidad Algorítmica 2019-02

Trabajo Parcial para el curso de Complejidad Algorítmica de la carrera de Ingeniería de Software y Ciencias de la Computación de la Universidad Peruana de Ciencias Aplicadas (UPC)

Los problemas de optimización de empaquetamiento y el cortes son problemas NP. Estos algoritmos son actualmente muy dificiles de calcular debido a su alto tiempo de procesamiento. Existen soluciones que nos dan el mejor ordenamiento para un tiempo "x", más no el mejor de todos los posibles casos. Esto lo podemos decir en el caso donde existan multiples datos que procesar.

Nuestro proyecto busca encontrar y dar una solucion al problema de cortes y empaquetamiento. Para llevar a acabo dicha tarea hemos realizado unas aplicaciones con ayuda del lenguaje de programacion Python, en donde hemos implementado algunas estrategias de programación como un Backtracking, Divide and conquer, y Fuerza Bruta que nos permiten poder calcular una solución posible.



## Formato de Dataset

Nuestro proyecto recibe archivos con extensión ".txt" los cuales DEBEN seguir el siguiente formato

```
720 670
8
A 120 120 2
B 285 130 1
C 200 300 1
D 165 320 1
E 235 470 1
F 200 170 1
G 285 220 1
H 555 200 1
```

Donde en la primera linea se especifica el ancho y largo de la plancha, en la segunda linea el número de piezas a evaluar, seguido de la lista de piezas con su respectivo label, ancho, largo y número de piezas del mismo formato.

### Requisitos

Se debe tener en cuenta que nuestra aplicación usa los siguientes modulos.

```
matlplotlib
tkinter
```

## Ejemplo de funcionamiento

Ejecutar la funcion main() y se abrirá un cuadro de dialogo dónde se deberá ingresar el dataset en formato .txt para poder filtrar la información en este mismo y procesarlo. Posteriormente se muestra el gráfic y se arrojan los resultados en la consola.

Los datasets del 2 a 5 contemplan las diferentes validaciones de datos que tiene nuestra implementación.

## Conclusiones

Si tenemos una extensa cantidad de datos, el algoritmo número 2, que se encuentra en el archivo cut.py, logra solucionar de mejor manera el problema. Por ser más sencillo el primer algoritmo se trata de un O(n) y el segundo con una mejor respuesta nos da un O(n^2). El segundo algoritmo nos da una mejor solución para archivos con pequeños, mientras que el primero puede llegar a ser escalable.

## Elaborado con

* [Python] - El lenguaje de programación usado
* [GitHub] - Hub de git
* [GitKraken] - Interfaz gráfica para git
* [VisualStudioCode] - Editor de código

## Autores

* **Sergio Villarruel** - *Trabajo Inicial* - [SergioVillarruel](https://github.com/SergioVillarruel)
* **Rodrigo Lozano** - *Trabajo Inicial* - [RalcBK](https://github.com/RalcBK)
* **Carlos Obispo** - *Trabajo Inicial* - [ZBishopM](https://github.com/ZBishopM)

## Licencia

This project is licensed and finaced by us. :)

## Agradecimientos

* A Luis Canaval por exigirnos y confiar en nosotros.
* A toda la documentación repartida por la web.
* Por la Alianza.
* A todo aquel que confió en nosotros y a quienes no.

## SquareCubeGames©
