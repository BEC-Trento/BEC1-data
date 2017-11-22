prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Config Field OFF.sub")
    prg.add(20000, "Initialize 0 TTL0")
    prg.add(20100, "Initialize Test IGBT")
    prg.add(20200, "Initialize 0 TTL2")
    prg.add(20300, "Initialize 0 TTL3")
    prg.add(20400, "Initialize 0 TTL4")
    prg.add(20450, "Na 3D MOT cool (-) ON", enable=False)
    prg.add(20500, "Na Probe/Push (+) ON")
    prg.add(20550, "Pulse MOT Na OFF")
    prg.add(25100, "Breakpoint Main Table TTL OFF")
    prg.add(25200, "Breakpoint Na Table TTL OFF")
    prg.add(25600, "Breakpoint Main Table TTL ON")
    prg.add(25700, "Breakpoint Na Table TTL ON")
    prg.add(28100, "Bcomp z Sign Plus")
    prg.add(29100, "Bcomp y Sign Plus")
    prg.add(35100, "Bx Grad OFF")
    prg.add(45700, "Breakpoint Main Table TTL OFF")
    prg.add(45800, "Breakpoint Na Table TTL OFF")
    prg.add(45850, "BREAKPOINT")
    prg.add(46200, "NOP")
    return prg
