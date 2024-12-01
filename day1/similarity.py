f = open("input.txt", "r")
l1 = []
l2 = []

occurr = {}
for n in f.readlines():
    tmp = n.replace("\n","").split("   ")
    l1.append(int(tmp[0]))
    l2.append(tmp[1])

s = 0
c = 0
for e in l2:
    if e in occurr.keys():
        occurr[e] += 1
    else:
        occurr[e] = 1


print(occurr)

for e in l1:
    if str(e) in occurr.keys():
        s += e * occurr[str(e)]
    else:
        s += 0

print(s)