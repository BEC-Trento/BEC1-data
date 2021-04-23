prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(2000000, "Dipole Trap x AOM (+) Amp", 1000)
    prg.add(5000000, "Dipole Trap x AOM (+) Amp", 1, enable=False)
    prg.add(7000000, "Dipole Trap x AOM (+) freq", 110.00)
    return prg
