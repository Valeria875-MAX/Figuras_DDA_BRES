def dda(x,y,x2,y2):
    dx = x2-x
    dy = y2-y
    steps= abs(dy)
    if abs(dx)>abs(dy):
        steps=abs(dx)

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p3 = y
    x_vars=[p1]
    y_vars=[p3]
    for i in range(steps):
        if dx<0:
            p1 -= increment_x
        else:
            p1 += increment_x

        x_vars.append(round(p1))
        if dy<0:
            p3 += increment_y
        else:
            p3 +=increment_y
        y_vars.append(round(p3))

        
    return x_vars,y_vars


def bresenham(x,y,x2,y2):
    dx = abs(x2 -x)
    dy = abs(y2 -y)
    p = 2 * dy -dx
    x_vars=[]
    y_vars=[]
    while x <= x2:
        x_vars.append(x)
        y_vars.append(y)
        x += 1
        if p<0:
            p = p + 2 * dy
        else:
            p = p + (2 * dy) - (2 * dx)
            y += 1
    return x_vars,y_vars


def puntos_cuadrilateros(x,y):
    return [[1,1],[1,y+1],[x+1,1],[x+1,y+1]]

def puntos_equilateros(b):
    origen = [1,1]
    punto2 = [b,1]
    y = round(((b**2)-((b/2)**2))**0.5)#teorema de pitagoras
    x = round(b/2)
    punto3 = [x,y]
    return[origen,punto2,punto3]

def puntos_Rectangulo(x,y):

    return[[1,1],[x,1],[x,y]]

def puntos_Poligono(x,y):
    lados= [0,0]
    lapiz= [0,1]
    return([int(lapiz.pos()[0]),int (lapiz.pos()[1])])
            
    

if __name__ == '__main__':
    x = dda(1,1,1,5)
    print (x)