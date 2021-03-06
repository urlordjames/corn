from parse import parsate

varlist = {}
i = 0

def runate(filename, debug):
    global i
    exe = parsate(filename, debug)
    if debug:
        print(exe)

    def num(n):
        return int(n[:-1])

    def fixnums(num1, num2, validtypes):
        while not type(num1) in validtypes:
            num1 = execute(num1)
        while not type(num2) in validtypes:
            num2 = execute(num2)
        return num1, num2

    def execute(ln):
        if debug:
            print(ln)
        assert ln is not None
        if type(ln) == int or type(ln) == bool:
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
        if ln[0] == "jmp":
            global i
            condition = execute(ln[1][0])
            while not type(condition) == bool:
                condition = execute(condition)
            if condition:
                val = ln[1][1]
                while not type(val) == int:
                    val = execute(val)
                i += val
                return True
            return False
        if ln[0] == "intop":
            num1, num2 = fixnums(ln[1], ln[2], [int])
            return int(eval("num1 " + ln[3] + " num2"))
        if ln[0] == "boolop":
            num1, num2 = fixnums(ln[1], ln[2], [int, bool])
            return bool(eval("num1 " + ln[3] + " num2"))
        if ln[0] == "asop":
            varlist.update({ln[1]: execute(ln[2])})
            return True
        return False

    while not i == len(exe):
        execute(exe[i])
        i += 1

if __name__ == "__main__":
    runate("test.cn", False)
