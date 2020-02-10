def lexate(filename):
    f = open(filename, "r")
    corn = f.read()
    f.close()

    masterlist = {
        "print": "print",
        "(": "fnop",
        ")": "fnend",
        "+": "+"
    }
    
    cornparse = []

    for ln in corn.split("\n"):
        if ln[0] == "#":
            continue
        tokens = []
        for block in ln.split(" "):
            if len(block) > 1 and block[-1:] == "i":
                tokens.append(block)
            else:
                tokens.append(masterlist[block])
        cornparse.append(tokens)

    return cornparse
