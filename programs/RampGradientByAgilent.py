prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Bragg burst ON")
    prg.add(2200000, "Bragg burst OFF")
    return prg
