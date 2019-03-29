prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(10000, "Rele 1 Close")
    prg.add(20000, "Rele 2 Open")
    prg.add(30000, "Rele 3 Close")
    prg.add(40000, "Rele 4 Open")
    prg.add(50000, "IGBT 1 pinch", -10.000000)
    prg.add(60000, "IGBT 2 pinch+comp", -10.000000)
    prg.add(70000, "IGBT 3 Close")
    prg.add(80000, "IGBT 4 Close")
    prg.add(90000, "IGBT 5 Open")
    return prg
