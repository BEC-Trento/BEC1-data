prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Bx Grad OFF")
    prg.add(8000, "Bx Grad ON")
    return prg
