prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", -10.0000)
    prg.add(10, "IGBT 2 pinch+comp", -10.0000)
    prg.add(20, "IGBT 3 Open")
    prg.add(30, "IGBT 4 Open")
    prg.add(50, "IGBT 6 Open")
    prg.add(60, "IGBT 5 Open")
    return prg
