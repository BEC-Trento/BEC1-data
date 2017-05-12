prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(10000000, "TTL2 5 OFF", enable=False)
    prg.add(10500000, "TTL2 5 ON", enable=False)
    prg.add(10500000, "TTL2 5 OFF", enable=False)
    prg.add(10500000, "Bx Grad ON")
    prg.add(11000000, "Bx Grad OFF")
    prg.add(11010000, "Bx Grad ON")
    prg.add(13000000, "Bx Grad OFF")
    return prg
