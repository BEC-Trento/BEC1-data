prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Bx Grad ON")
    prg.add(5000000, "TTL2-11 ON")
    prg.add(5000010, "Bx Grad OFF")
    prg.add(5020010, "Bx Grad ON")
    prg.add(6000000, "TTL2-11 OFF")
    return prg
