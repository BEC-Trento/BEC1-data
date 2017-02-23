prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Bx Grad ON")
    prg.add(51000, "Bx Grad OFF")
    return prg
