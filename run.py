from parse import parsate

def runate(filename):
    exe = parsate(filename)

    varlist = {}

    def num(n):
        return int(n[:-1])

    def execute(ln):
        assert ln is not None
        if type(ln) == int:
            return ln
        if type(ln) == list and len(ln) == 1:
            return execute(ln[0])
        if type(ln) == str:
            if ln[-1:] == "i":
                return num(ln)
            if ln in varlist:
                return execute(varlist[ln])
        if ln[0] == "print":
            print(execute(ln[1]))
            return True
        if ln[0] == "+":
            num1 = ln[1]
            while not type(num1) == int:
                num1 = execute(num1)
            num2 = ln[2]
            while not type(num2) == int:
                num2 = execute(num2)
            assert type(num1) == type(num2) and type(num1) == int
            return num1 + num2
        if ln[0] == "asop":
            varlist.update({ln[1]: execute(ln[2])})
            return True
        return False

    for ln in exe:
        execute(ln)

runate("test.cn")
