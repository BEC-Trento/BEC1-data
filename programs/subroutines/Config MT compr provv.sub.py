prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Rele 1 Close")
    prg.add(10, "IGBT 2 Provv ON")
    prg.add(20, "Rele 2 Open")
    prg.add(30, "Rele 3 Close")
    prg.add(40, "Rele 4 Open")
    prg.add(60, "IGBT 3 Open")
    prg.add(70, "IGBT 4 Open")
    prg.add(80, "IGBT 5 Close")
    prg.add(90, "IGBT 6 Open")
    prg.add(500, "IGBT 1 pinch", -10.000000)
    return prg
