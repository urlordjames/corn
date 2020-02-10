from parse import parsate

def runate(filename):
    exe = parsate(filename)

    def execute(ln):
        if len(ln) == 1:
            return ln[0]
        if ln[0] == "print":
            print(execute(ln[1]))
        if ln[0] == "+":
            return int(ln[1]) + int(execute(ln[2]))

    for ln in exe:
        execute(ln)

runate("test.cn")
