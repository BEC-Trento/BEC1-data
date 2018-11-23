prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Config Field OFF.sub")
    prg.add(10000, "TTL Fluo Lock OFF")
    prg.add(20000, "Initialize 0 TTL0")
    prg.add(20100, "Initialize Test IGBT")
    prg.add(20200, "Initialize 0 TTL2")
    prg.add(20300, "Initialize 0 TTL3")
    prg.add(20400, "Initialize 0 TTL4")
    prg.add(25400, "Bcomp y Sign Minus", enable=False)
    prg.add(25450, "Na 3D MOT cool (-) ON")
    prg.add(25500, "Na Probe/Push (+) ON")
    prg.add(25550, "Pulse MOT Na OFF")
    prg.add(27000, "Mirrors MOT")
    prg.add(30100, "Breakpoint Main Table TTL OFF")
    prg.add(30200, "Breakpoint Na Table TTL OFF")
    prg.add(30600, "Breakpoint Main Table TTL ON")
    prg.add(30700, "Breakpoint Na Table TTL ON")
    prg.add(41300, "Breakpoint Main Table TTL OFF")
    prg.add(41400, "Breakpoint Na Table TTL OFF")
    prg.add(41450, "BREAKPOINT")
    prg.add(41800, "NOP")
    return prg
