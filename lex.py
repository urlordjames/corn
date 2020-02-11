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
        "-": "-",
        "var": "var",
        "int": "int",
        "=": "asop",
        ">": "gop",
        "<": "lop",
        "==": "eop"
    }

    numbers = ["-"]

    for i in range(0,10):
        numbers.append(str(i))

    tokenlist = masterlist.keys()

    for line in stuff.split("\n"):
        if line[0] == "#":
            continue
        tokens = []
        for token in line.split(" "):
            if token[-1:] == "i":
                tokens.append(token)
                continue
            if token in masterlist:
                tokens.append(masterlist[token])
                continue
            tokens.append(token)
        cornparse.append(tokens)
    return cornparse
