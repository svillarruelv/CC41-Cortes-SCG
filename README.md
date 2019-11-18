# Trabajo Final de Complejidad Algorítmica 2019-02

Trabajo Final para el curso de Complejidad Algorítmica de la carrera de Ingeniería de Software y Ciencias de la Computación de la Universidad Peruana de Ciencias Aplicadas (UPC)

Las empresas dedicadas a la logística, comúnmente afrontan situaciones de empaquetamiento en 3 dimensiones. Al momento de llenar contenedores, camiones, barco y/o aviones de carga, se desea hacer la menor cantidad de viajes posibles por ende deben asegurarse de enviar la mayor cantidad de elementos en cada transporte que realizan. 
Las empresas, que afrontan dichas situaciones, deben decidir cómo prefieren atacar el problema, y que tipo de solución es más apropiada. Para esto, deben contratar o consultar personal especializado en procesos, algoritmos y complejidad algorítmica para analizar y discutir las ventajas y desventajas que conlleva cada algoritmo, y decidir qué solución es más apropiada.

Los problemas de optimización de empaquetamiento y el cortes son problemas NP. Estos algoritmos son actualmente muy dificiles de calcular debido a su alto tiempo de procesamiento. Existen soluciones que nos dan el mejor ordenamiento para un tiempo "x", más no el mejor de todos los posibles casos. Esto lo podemos decir en el caso donde existan multiples datos que procesar.

Nuestro proyecto busca encontrar y dar una solucion al problema de empaquetamiento. Para llevar a acabo dicha tarea hemos realizado unas aplicaciones con ayuda del lenguaje de programacion Python, en donde hemos implementado algunas estrategias de programación que nos permiten poder calcular una posible solución.


## Formato de Dataset

Nuestro proyecto recibe archivos con extensión ".txt" los cuales DEBEN seguir el siguiente formato

```
          
2 3 5         Alto, Ancho, Largo
3             Cantidad de formatos de cajas
2 A 1 1 2     N formatos, Identificador, Alto, Ancho, Largo
3 B 1 2 3
1 C 1 2 5
```

### Requisitos

Se debe tener en cuenta que nuestra aplicación usa los siguientes modulos.

```
matlplotlib
mpl_toolkits.mplot3d
```

## Ejemplo de funcionamiento

Ejecutar cada algoritmo, se deberá cambiar el data set de entrada desde el path de la funcion de lectura. Posteriormente se muestra el gráfico y se arrojan los resultados en la consola.


## Conclusiones

Los algoritmos funcionan de acuerdo a la cantidad de datos ingresados, mientras más se saturen tendran un desempeño más lento. No existe una solución exacta para este tipo de problemas de empaquetamiento puesto que depende de diversas variables.

## Elaborado con

* [Python] - El lenguaje de programación usado
* [GitHub] - Hub de git
* [GitKraken] - Interfaz gráfica para git
* [VisualStudioCode] - Editor de código

## Autores

* **Rodrigo Lozano** - *Trabajo Final* - [RalcBK](https://github.com/RalcBK)
* **Carlos Obispo** - *Trabajo Inicial*
* **Sergio Villarruel** - *Trabajo Inicial* - [SergioVillarruel](https://github.com/SergioVillarruel)

## Licencia

This project is licensed and finaced by us. :)

## Agradecimientos

* A Luis Canaval por exigirnos y confiar en nosotros.
* A toda la documentación repartida por la web.
* Por la Alianza.
* A todo aquel que confió en nosotros y a quienes no.

## SquareCubeGames©
