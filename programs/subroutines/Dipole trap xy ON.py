prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x AOM (+) freq", 110.00)
    prg.add(1000, "Dipole Trap y AOM (-) freq", 110.00)
    return prg
