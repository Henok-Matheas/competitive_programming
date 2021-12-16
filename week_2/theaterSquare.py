
[6,6,4]
def theaterSquare(x,y,a):
    row = (x // a) + 1
    column = (y // a) + 1
    return row * column

print(theaterSquare(6,6,4))