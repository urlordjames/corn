from parse import parsate

def runate(filename):
    exe = parsate(filename)

    def num(n):
        if n[-1:] == "i":
            return int(n[:-1])

    def execute(ln):
        if len(ln) == 1:
            return num(ln[0])
        if ln[0] == "print":
            print(execute(ln[1]))
        if ln[0] == "+":
            num1 = num(ln[1])
            num2 = execute(ln[2])
            assert type(num1) == type(num2) and type(num1) == int
            return num1 + num2

    for ln in exe:
        execute(ln)

runate("test.cn")
