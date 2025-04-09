li = [1, 2, 3, 4, 5, 6]

def square(ele):
    return ele ** 2

def cube(ele):
    return ele **3


square_list =list(map(square,li))
print("Square of li", square_list)

cube_list = list(map(cube,li))
print("Cube of li", cube_list)

