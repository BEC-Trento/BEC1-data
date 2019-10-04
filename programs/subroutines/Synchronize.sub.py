prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-21000, "Breakpoint Main Table TTL OFF")
    prg.add(-20900, "Breakpoint Na Table TTL OFF")
    prg.add(-20500, "Breakpoint Main Table TTL ON")
    prg.add(-20400, "Breakpoint Na Table TTL ON")
    prg.add(-400, "Breakpoint Main Table TTL OFF")
    prg.add(-300, "Breakpoint Na Table TTL OFF")
    prg.add(-250, "BREAKPOINT")
    prg.add(100, "NOP")
    return prg
