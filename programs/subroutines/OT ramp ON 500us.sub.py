prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x (+) Amp", 1.000000)
    prg.add(400, "Dipole Trap y (-) Amp", 1.000000)
    prg.add(1000, "Dipole Trap x (+) Amp", 200.800000)
    prg.add(1400, "Dipole Trap y (-) Amp", 200.800000)
    prg.add(2000, "Dipole Trap x (+) Amp", 400.600000)
    prg.add(2400, "Dipole Trap y (-) Amp", 400.600000)
    prg.add(3000, "Dipole Trap x (+) Amp", 600.400000)
    prg.add(3400, "Dipole Trap y (-) Amp", 600.400000)
    prg.add(4000, "Dipole Trap x (+) Amp", 800.200000)
    prg.add(4400, "Dipole Trap y (-) Amp", 800.200000)
    prg.add(5000, "Dipole Trap x (+) Amp", 1000.000000)
    prg.add(5400, "Dipole Trap y (-) Amp", 1000.000000)
    return prg
