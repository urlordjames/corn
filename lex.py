def lexate(filename):
    f = open(filename, "r")
    stuff = f.read()
    f.close()

    cornparse = []

    masterlist = {
        "print": "print",
        "(": "fnop",
        ")": "fnend",
        "+": "+",
    }

    numbers = []

    for i in range(0,10):
       numbers.append(str(i))

    tokenlist = masterlist.keys()

    for line in stuff.split("\n"):
        if line[0] == "#":
            continue
            tbegin = 0
        tbuffer = ""
        tokens = []
        i = 0
        num = False
        for l in line:
            for c in tokenlist:
                if i > len(c) - 1:
                   break
                if l in numbers:
                   tbuffer += str(l)
                   num = True
                   break
                if l == "i" and num:
                   tbuffer += l
                   tokens.append(tbuffer)
                   tbuffer = ""
                   i = 0
                   num = False
                   break
                if l == c[i]:
                  tbuffer += l
                  if tbuffer in tokenlist:
                     tokens.append(masterlist[tbuffer])
                     tbuffer = ""
                     i = 0
                  else:
                     i += 1
        cornparse.append(tokens)
    return cornparse
