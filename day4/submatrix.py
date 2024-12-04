import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

f = open("input.txt", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]


def check_mas(m):
  
    find = [  [["S"," ","M"],
            [" ","A"," "],
            ["S"," ","M"]],
           [["S"," ","S"],
            [" ","A"," "],
            ["M"," ","M"]],
           [["M"," ","S"],
            [" ","A"," "],
            ["M"," ","S"]],
           [["M"," ","M"],
            [" ","A"," "],
            ["S"," ","S"]]
    ]

    c = 0
    for f in find:
        if f[0][0] == m[0][0] and f[0][2] == m[0][2] and f[1][1] == m[1][1] and f[2][0] == m[2][0] and f[2][2] == m[2][2]:
            c+=1
    return c 


matrix = create_matrix(l)
grid = np.array(matrix)

v = sliding_window_view(matrix, (3,3))
s = 0
for e in v:
    for j in e:
        s += check_mas(j)

print(s)