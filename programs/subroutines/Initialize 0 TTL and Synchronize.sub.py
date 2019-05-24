prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Config Field OFF.sub")
    prg.add(3000, "TTL Fluo Lock OFF")
    prg.add(13000, "Initialize 0 TTL0", enable=False)
    prg.add(13100, "Initialize Test IGBT", enable=False)
    prg.add(13200, "Initialize 0 TTL2", enable=False)
    prg.add(13300, "Initialize 0 TTL3", enable=False)
    prg.add(13400, "Initialize 0 TTL4", enable=False)
    prg.add(18400, "Bcomp y Sign Minus", enable=False)
    prg.add(18450, "Na 3D MOT cool (-) ON", enable=False)
    prg.add(18500, "Na Probe/Push (+) ON", enable=False)
    prg.add(18550, "Pulse MOT Na OFF", enable=False)
    prg.add(20000, "Mirrors MOT", enable=False)
    prg.add(23100, "Breakpoint Main Table TTL OFF")
    prg.add(23200, "Breakpoint Na Table TTL OFF")
    prg.add(23600, "Breakpoint Main Table TTL ON")
    prg.add(23700, "Breakpoint Na Table TTL ON")
    prg.add(34400, "Breakpoint Na Table TTL OFF")
    prg.add(34900, "Breakpoint Main Table TTL OFF")
    prg.add(44449, "BREAKPOINT")
    prg.add(44800, "NOP")
    return prg
