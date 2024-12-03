import re

f = open("input.txt", "r")
l = [  n for n in f.readlines()  ]

p = re.compile(r"mul\([0-9]+,[0-9]+\)")
f = re.compile(r"[0-9]+")

s = 0
for row in l:
    #print(row)
    m = p.findall( row )
    for e in m:
        #print(e)
        res = f.findall(e)
        s += int(res[0]) * int(res[1])

print(s)