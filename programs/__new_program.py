prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole Trap y DAC V", 0.0000)
    prg.add(10000000, "Dipole Trap y DAC V", 5.0000)
    prg.add(40000000, "Dipole Trap y DAC V", 0.0000)
    return prg
