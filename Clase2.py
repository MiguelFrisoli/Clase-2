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


"""Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5."""

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str (num)

print (fizz_buzz(98))

