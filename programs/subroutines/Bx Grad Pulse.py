prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL2-11 ON")
    prg.add(500, "Bx Grad OFF")
    prg.add(30500, "Bx Grad ON")
    prg.add(31000, "TTL2-11 OFF")
    return prg
