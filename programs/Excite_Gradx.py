prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Bx Grad ON")
    prg.add(50000, "Bragg burst ON")
    prg.add(100000, "Bragg burst OFF")
    prg.add(3000000, "Bx Grad OFF")
    return prg
