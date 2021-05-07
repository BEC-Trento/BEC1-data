prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x Dac V", 0.0000)
    prg.add(10000, "Dipole Trap y DAC V", 0.0000)
    prg.add(20000, "Dipole Trap x AOM (+) Amp", 1)
    prg.add(30000, "Dipole Trap y AOM (-) Amp", 1)
    prg.add(40000, "Dipole Trap x AOM (+) freq", 60.00)
    prg.add(50000, "Dipole Trap y AOM (-) freq", 60.00)
    return prg
