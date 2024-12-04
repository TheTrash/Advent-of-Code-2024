def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row.split(" "):
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp

def check_order(array):
    if all(array[i] <= array[i + 1] and 0 < abs(array[i] - array[i+1]) < 4 for i in range(len(array) - 1)):
        return True
    elif all(array[i] >= array[i + 1] and 0 < abs(array[i] - array[i+1]) < 4 for i in range(len(array) - 1)):
        return True
    else:
        return False
                    




f = open("input.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

matrix = create_matrix(l)

safe_count = 0
for row in matrix:
    for i in range(len(row)):
        #eseguo il taglio dell'array e controllo
        #print(row[0:i] + row[i+1:])
        if check_order(row[0:i] + row[i+1:]) == True:
            safe_count +=1
            break


print(f"Total safe: {safe_count}")