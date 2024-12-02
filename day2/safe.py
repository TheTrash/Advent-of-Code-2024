



def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row.split(" "):
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp

f = open("example.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

matrix = create_matrix(l)

safe = 0
for row in matrix:
    asc = False
    asc_c = 0
    desc = False
    desc_c = 0
    print(row)
    i = 0
    while(i < len(row)):
        print(i)
        if row[i-1] > row[i] and asc == False:
            if 0 < (row[i-1] - row[i]) < 4:
                desc = True
                desc_c +=1
            else:
                break
        if row[i] > row[i-1] and desc == False:
            if 0 < (row[i] - row[i - 1]) < 4:
                asc = True
                asc_c +=1
            else:
                break 
        i+=1                
    if asc_c == len(row)-1:
        #print("good asc")
        safe +=1
    elif desc_c == len(row)-1:
        #print("good desc")
        safe +=1
    else:
        #print("unsafe")
        pass


print(f"Total safe: {safe}")