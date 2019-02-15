prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10, "Rele 1 Close")
    prg.add(20, "Rele 2 Open")
    prg.add(30, "Rele 3 Close")
    prg.add(40, "Rele 4 Open")
    prg.add(50, "Rele 5 Close")
    prg.add(60, "IGBT 1 pinch", -10.0000)
    prg.add(70, "IGBT 2 pinch+comp", -10.0000)
    prg.add(80, "IGBT 3 Close")
    prg.add(90, "IGBT 4 Open")
    prg.add(100, "IGBT 5 Close")
    prg.add(110, "IGBT 6 Open")
    return prg
