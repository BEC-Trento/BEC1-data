prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x (+) Amp", 1.000000)
    prg.add(400, "Dipole Trap y (-) Amp", 1.000000)
    return prg
