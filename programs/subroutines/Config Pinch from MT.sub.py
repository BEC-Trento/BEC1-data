prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(20, "Rele 2 Open")
    prg.add(30, "Rele 5 Open")
    prg.add(40, "Rele 1 Close")
    prg.add(50, "Rele 3 Open")
    prg.add(60, "Rele 4 Close")
    prg.add(70, "IGBT 3 Open")
    prg.add(80, "IGBT 4 Close")
    prg.add(90, "IGBT 5 Open")
    prg.add(100, "IGBT 1 pinch", 10.000000)
    prg.add(110, "IGBT 2 pinch+comp", -10.000000)
    return prg
