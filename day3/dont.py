import re

f = open("input.txt", "r")
l = [  n.replace("\n", "") for n in f.readlines()  ]
st = ''.join(l)

p = re.compile(r"mul\([0-9]+,[0-9]+\)")
f = re.compile(r"[0-9]+")
d = re.compile(r"don't\b(.*?)do\b")

s = 0
mapper = []

m = re.sub( r"don't\b(.*?)do\b", "", st )
print(m)

for mul in p.findall(m):
    #print(mul)
    res = f.findall(mul)
    s += int(res[0]) * int(res[1])


print(s)