prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(2000, "TTL Repumper MOT OFF")
    prg.add(17000, "TTL Repumper MOT ON")
    prg.add(22000, "TTL Repumper MOT OFF")
    prg.add(47000, "BREAKPOINT")
    prg.add(48000, "NOP")
    prg.add(62000, "TTL Repumper MOT ON")
    prg.add(65000, "TTL Repumper MOT OFF")
    return prg
