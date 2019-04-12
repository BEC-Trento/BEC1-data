prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "GM ON")
    prg.add(20000, "GM OFF")
    return prg
