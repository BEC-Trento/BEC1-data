prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(11000000, "Bx Grad ON")
    prg.add(25000000, "TTL2-11 ON")
    prg.add(25000010, "Bx Grad OFF")
    prg.add(25050010, "Bx Grad ON")
    prg.add(26030000, "TTL2-11 OFF")
    return prg
