f = open("input.txt", "r")

verbose = False
rules = {}
i = 0
first = True
valid_pages = []

for l in f.readlines():
    if l != "\n" and first:
        rule = l.replace("\n","").split("|")
        if verbose : print(rule)
        if rule[0] in rules.keys():
            rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = [rule[1]]
        i+=1
    elif l == "\n":
        first = False
        if verbose :print(rules)
    else:
        pages = l.replace("\n","").split(",")
        if verbose: print(pages)
        res = ""
        for i in range(len(pages)):
            t = pages[i]
            if res == "not ok":
                break
            if verbose: print("analizzando ", t)
            if t in rules.keys():
                for e in pages[i+1:]:
                    if verbose: print("front " , e)
                    if e in rules[t]:
                        pass
                        res = "ok"
                    else:
                        res = "not ok"
                        break
                for e in pages[0:i]:
                    if verbose: print("back " , e)
                    if e in rules[t]:
                        res = "not ok"
                        break 
                    else:
                        res = "ok"
        if verbose : var = input()      
        print(pages, res)
        if res == "ok":
            valid_pages.append(pages)

s = 0
for pages in valid_pages:
    s += int(pages[int(len(pages)/2)])

print(s)