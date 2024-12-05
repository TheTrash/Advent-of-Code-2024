f = open("input.txt", "r")


def check_pages_validity(pages,verb = True):
    if verb: print(pages)
    res = ""
    swap = False
    for i in range(len(pages)):
        t = pages[i]
        if res == "not ok":
            break
        if verb: print("analizzando ", t)
        if t in rules.keys():
            for e in pages[i+1:]:
                if verb: print("front " , e)
                if e in rules[t]:
                    res = "ok"
                else:
                    res = "not ok"
                    ei= pages.index(e)
                    ti = pages.index(t)
                    pages[ei] , pages[ti] = pages[ti], pages[ei]
                    swap = True
                    break
            for e in pages[0:i]:
                if verb: print("back " , e)
                if e in rules[t]:
                    res = "not ok"
                    ei= pages.index(e)
                    ti = pages.index(t)
                    pages[ei] , pages[ti] = pages[ti], pages[ei]
                    swap = True
                    break 
                else:
                    res = "ok"
    if verb : var = input()

    #print(pages, res)
    return pages, swap

verbose = True
rules = {}
i = 0
first = True
valid_pages = []
invalid_pages = []
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
        pages, resp = check_pages_validity(pages, False)
        print(resp, pages)
        if resp == False:
            valid_pages.append(pages)
        else:
            while(resp == True):
                pages, resp = check_pages_validity(pages, False)
            invalid_pages.append(pages)
        


s = 0
for pages in invalid_pages:
    print(pages, pages[int(len(pages)/2)])
    s += int(pages[int(len(pages)/2)])

print(s)