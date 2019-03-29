prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-50000, "B comp x", 2000.0)
    prg.add(-10049, "IGBT B comp x ON")
    prg.add(0, "Bx Grad ON")
    prg.add(120000, "Bx Grad OFF")
    prg.add(121000, "IGBT B comp x OFF")
    return prg
