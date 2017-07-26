prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(5000000, "TTL2 5 ON")
    prg.add(10000000, "Dipole Trap x DAC V", 2.5000)
    prg.add(12000000, "heating dipole")
    prg.add(13000000, "Dipole Trap x DAC V", 0.0000)
    return prg
