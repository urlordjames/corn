from lex import lexate

def parsate(filename):
    tklist = lexate(filename)

    intops = {
        "+": "+",
        "-": "-",
        "*": "*",
        "**": "**",
        "^": "**"
    }

    boolops = {
        "gop": ">",
        "lop": "<",
        "eop": "=="
    }
    
    def parse(ln):
        z = []
        if type(ln) == bool:
            return ln
        if len(ln) == 1:
            if type(ln) == list:
                return ln
            if type(ln) == dict:
                return varlist[ln]
        if type(ln) == str:
            return ln
        if ln[1] == "fnop":
            endindex = 1
            while not ln[endindex] == "fnend":
                endindex += 1
            return [ln[0], parse(ln[2:endindex])]
        if ln[1] == "sepop":
            return [ln[0], ln[2]]
        if ln[1] in intops:
            return ["intop", parse(ln[0]), parse(ln[2:]), intops[ln[1]]]
        if ln[1] in boolops:
            return ["boolop", parse(ln[0]), parse(ln[2:]), boolops[ln[1]]]
        if ln[3] == "asop":
            return [ln[3], ln[2], parse(ln[4:])]
        return z

    cnexe = []

    for ln in tklist:
        cnexe.append(parse(ln))
        
    return cnexe
