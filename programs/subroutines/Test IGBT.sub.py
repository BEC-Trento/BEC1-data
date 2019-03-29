prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "IGBT pinch", 0.000000)
    prg.add(110000, "IGBT pinch+comp", 0.000000)
    prg.add(5000000, "IGBT pinch+comp", 6.000000)
    prg.add(10000000, "IGBT pinch", 9.900000)
    prg.add(15000000, "IGBT pinch+comp", 9.900000)
    prg.add(25000000, "IGBT pinch", -9.900000)
    prg.add(30000000, "IGBT pinch+comp", -9.900000)
    prg.add(45000000, "IGBT pinch", -1.000000)
    prg.add(55000000, "IGBT pinch+comp", -1.000000)
    return prg
