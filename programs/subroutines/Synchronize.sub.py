prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Breakpoint Main Table TTL OFF")
    prg.add(10, "Breakpoint K Table TTL OFF")
    prg.add(20, "Breakpoint Na Table TTL OFF")
    prg.add(450, "Breakpoint Main Table TTL ON")
    prg.add(460, "Breakpoint K Table TTL ON")
    prg.add(470, "Breakpoint Na Table TTL ON")
    prg.add(900, "Breakpoint Main Table TTL OFF")
    prg.add(910, "Breakpoint K Table TTL OFF")
    prg.add(920, "Breakpoint Na Table TTL OFF")
    prg.add(950, "BREAKPOINT")
    prg.add(1000, "NOP")
    return prg
