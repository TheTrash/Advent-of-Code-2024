step = 0


def beauty_print(matr, debug = False):
    if(debug):
        print("\n")
    for i in range(len(matr)):
        row = ""
        for j in range(len(matr[0])):
            row += matr[i][j]
        if debug:
            print(row, i)
        else:
            print(row)

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

def is_within_bounds(position, matrix_size):
    rows, cols = matrix_size
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

def go_on(position, direction):
    global step
    x = position[0]
    y = position[1] 
    while( matrix[x][y] != "#"):
        matrix[x][y] = "X"
        x  += directions[direction][0]
        y  += directions[direction][1]
        step += 1
    return (x,y), next_direction(direction)
    
def next_direction(direction):
    order = ["up", "right", "down", "left"]
    next_index = (order.index(direction) + 1) % len(order)
    return order[next_index]

f = open("example.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

matrix = create_matrix(l)

directions = {
    "up": (-1, 0),  # Per spostarsi verso l'alto, decrementa la riga di 1
    "down": (1, 0),  # Per spostarsi verso il basso, incrementa la riga di 1
    "left": (0, -1),  # Per spostarsi a sinistra, decrementa la colonna di 1
    "right": (0, 1)  # Per spostarsi a destra, incrementa la colonna di 1
}


position = None
direction = None

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "^":
            print(f"start at ({i},{j})")
            position = (i,j)
            direction = "up"
            break


next_position = (position[0]+directions[direction][0],position[1]+directions[direction][1])
while(is_within_bounds(next_position,matrix_size=(len(matrix),len(matrix[0])))):
      position, direction = go_on(position,direction)
      print(position, direction)
      print("new step")
      beauty_print(matrix)
      var = input()
      
print(step)




