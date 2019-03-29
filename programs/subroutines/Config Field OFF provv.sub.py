prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", -10.000000)
    prg.add(10, "IGBT 2 Provv OFF")
    prg.add(20, "IGBT 3 Open")
    prg.add(30, "IGBT 4 Open")
    prg.add(40, "IGBT 5 Open")
    prg.add(50, "IGBT 6 Open")
    return prg
