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

"""A graph is a set of nodes and edges that connect those nodes.

Graph Example

There are two types of graphs; directed and undirected. 
In an undirected graph, the edges between nodes have no particular direction (like a two-way street) 
whereas in a directed graph, each edge has a direction associated with it (like a one-way street).

For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. 
In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.

We can encode graphs using an adjacency matrix. 
An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at row "i" and column "j" is a 0 
if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent."""

def are_nodes_adjacent(matrix, node1, node2):
    return matrix[node1][node2] == 1