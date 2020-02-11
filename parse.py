from lex import lexate

def parsate(filename):
    tklist = lexate(filename)

    vartypes = {
        "int": "_int"
    }
    
    def parse(ln):
        z = []
        if len(ln) == 1:
            if type(ln) == list:
                return ln
            if type(ln) == dict:
                return varlist[ln]
        if ln[1] == "fnop":
            endindex = 1
            while not ln[endindex] == "fnend":
                endindex += 1
            return [ln[0], parse(ln[2:endindex])]
        if ln[1] == "+":
            return [ln[1], ln[0], parse(ln[2:])]
        if ln[3] == "asop":
            return [ln[3], ln[2], parse(ln[4:])]
        return z

    cnexe = []

    for ln in tklist:
        cnexe.append(parse(ln))
        
    return cnexe
