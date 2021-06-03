import turtle
from Algoritmos.Algoritmos import *

LENGTH = 20
window = turtle.Screen()  #Creamos una ventana de turtle
window.screensize(1000,1000) #Le dimos un tamaño a la ventana 

fig= turtle.Turtle() #Creamos el lapiz con el que vamos a dibujar



def linea(x_vars,y_vars):  #DEfinimos la linua
    """Dibuja una linea en pixeles

    Args:
        x_vars (list): [coordenadas x]
        y_vars (list): [coordenadas y]
    """
    for i in range(len(x_vars)):
        x=LENGTH* x_vars[i]
        y=LENGTH* y_vars[i]

        fig.penup() #levantamos el lapiz para que no dibuje
        fig.goto(x,y)
        fig.pendown()  #Colocamos el lapiz en el lienzo para poder dibujar
        for i in range(4):   
            fig. fd(LENGTH)  #
            fig.rt(90)  #noventa grados

def cuadrilateros(matriz,algoritmo): #definimos el cuadrilatero dentro llamamos de matriz algoritmo 
    if algoritmo == 1:
        lado1 = dda(matriz[0][0],matriz[0][1],matriz[1][0],matriz[1][1])    #matriz de [[x],[y]]
        lado2 = dda(matriz[0][0],matriz[0][1],matriz[2][0],matriz[2][1])
        lado3 = dda(matriz[2][0],matriz[2][1],matriz[3][0],matriz[3][1])
        lado4 = dda(matriz[1][0],matriz[1][1],matriz[3][0],matriz[3][1])
    else:
        lado1 = bresenham(matriz[0][0],matriz[0][1],matriz[1][0],matriz[1][1])    #matriz de [[x],[y]]
        lado2 = bresenham(matriz[0][0],matriz[0][1],matriz[2][0],matriz[2][1])
        lado3 = bresenham(matriz[2][0],matriz[2][1],matriz[3][0],matriz[3][1])
        lado4 = bresenham(matriz[1][0],matriz[1][1],matriz[3][0],matriz[3][1])
    return [lado1,lado2,lado3,lado4]
def triangulos(matriz,algoritmo):
    if algoritmo ==1:
        lado1 =dda(matriz[0][0], matriz[0][1], matriz[1][0],matriz[1][1])
        lado2 =dda(matriz[0][0], matriz[0][1], matriz[2][0],matriz[2][1])
        lado3 =dda(matriz[2][0], matriz[2][1], matriz[1][0],matriz[1][1])

    else:
        lado1 =bresenham(matriz[0][0], matriz[0][1], matriz[1][0],matriz[1][1])
        lado2 =bresenham(matriz[0][0], matriz[0][1], matriz[2][0],matriz[2][1])
        lado3 =bresenham(matriz[2][0], matriz[2][1], matriz[1][0],matriz[1][1])
        
    return [lado1,lado2,lado3]

def poligono(matriz,algoritmo):
    if algoritmo ==1:
        lado1 =dda(matriz[0][0], matriz[0][1], matriz[1][0],matriz[1][1])
        lado2 =dda(matriz[0][0], matriz[0][1], matriz[2][0],matriz[2][1])
        lado3 =dda(matriz[2][0], matriz[2][1], matriz[1][0],matriz[1][1])

    else:
        lado1 =bresenham(matriz[0][0], matriz[0][1], matriz[1][0],matriz[1][1])
        lado2 =bresenham(matriz[0][0], matriz[0][1], matriz[2][0],matriz[2][1])
        lado3 =bresenham(matriz[0][0], matriz[2][1], matriz[1][0],matriz[1][1])
        
    return [lado1,lado2,lado3]


if __name__ == '__main__':
    print ("""Elije una opcion:
    1) Cuadrilateros(Cuadrado/Rectangulo)
    2)Triangulo equilatero
    3)Triangulo rectangulo
    4)Poligono 
    """)
    opcion = int(input("-->"))

    print("""Algoritmo a usar
    1)dda
    2)bresenham
    """)
    algoritmo = int(input("-->"))
    #Definir listas
    if (opcion == 1):
        #Cuadrilateros
        width,height =input("(x,y) ").split(",")
        width = int(width)-1
        height = int(height)-1
        puntos = puntos_cuadrilateros(width, height) 
        print(f"Puntos: {puntos}")
        resultados = cuadrilateros(puntos,algoritmo)
        print(f"Resultados: {resultados}")
       
    elif (opcion == 2):
        #Triangulo equilatero
        width =input("(base) ")
        width = int(width)-1
        puntos = puntos_equilateros(width) 
        print(f"Puntos: {puntos}")
        resultados = triangulos(puntos,algoritmo)
        print(f"Resultados: {resultados}")
       
    elif (opcion == 3):
        #Triangulo rectangulo
        width,height=input("(x,y)").split(",")
        width=int (width)
        height=int (height)
        puntos = puntos_Rectangulo(width, height)
        print(f"Puntos:{puntos}")
        resultados= triangulos(puntos,algoritmo)
        print(f"Resultados:{resultados}")

    elif (opcion == 4):
        #Poligono 
        size =10
        def angulo(n):
            alfa = 180 *(n-2)
            return alfa//n

        def get_angulos(lados,lapiz):
            points =[]
            for i in range(lados):
                points.append([int(lapiz.pos()[0]),int (lapiz.pos()[1])])
                lapiz.forward(size)
                lapiz.left(angulo)
            return points    
        width,height=input("(x,y)").split(",")
        width=int (width)
        height=int (height)
        puntos = puntos_Poligono(width, height)
        print(f"Puntos:{puntos}")
        resultados= poligono(puntos,algoritmo)
        print(f"Resultados:{resultados}")

    for punto in resultados:
        linea(punto[0],punto[1])

turtle.mainloop()
