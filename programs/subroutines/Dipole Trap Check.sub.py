prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x (+) Amp", 50.000000)
    prg.add(400, "Dipole Trap y (-) Amp", 150.000000)
    return prg
