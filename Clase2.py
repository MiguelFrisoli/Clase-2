"""Write a function that takes the base and height of a triangle and return its area"""

def tri_area(base, height):
    area = (float (base * height))/2
    return print ("El Área del triangulo es igual a: ", area, "cm cuadrados")

tri_area(7,9)


"""Write a function that converts hours into seconds."""

def how_many_seconds(hours):
    h = int (hours * 3600)
    return print(hours, "is equal to ", h, "seconds")

how_many_seconds(2)