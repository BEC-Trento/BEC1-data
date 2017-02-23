prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Breakpoint Main Table TTL OFF")
    prg.add(100, "Breakpoint Na Table TTL OFF")
    prg.add(500, "Breakpoint Main Table TTL ON")
    prg.add(600, "Breakpoint Na Table TTL ON")
    prg.add(20600, "Breakpoint Main Table TTL OFF")
    prg.add(20700, "Breakpoint Na Table TTL OFF")
    prg.add(20750, "BREAKPOINT")
    prg.add(21100, "NOP")
    return prg
