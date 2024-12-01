f = open("input.txt", "r")
l1 = []
l2 = []
for n in f.readlines():
    tmp = n.replace("\n","").split("   ")
    l1.append(int(tmp[0]))
    l2.append(int(tmp[1]))

print(l1)
print(l2)

l1.sort()
l2.sort()

print(l1)
print(l2)

s = 0
c = 0
for a,b in zip(l1,l2):
    if c%2 == 0:
        s += abs(a-b)
        print(f"{a}-{b}={abs(a-b)} ")


print(s)