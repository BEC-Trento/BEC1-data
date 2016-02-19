prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 6 Close")
    prg.add(10000, "IGBT 2 pinch+comp", 10.0000)
    prg.add(20000, "IGBT 1 pinch", -10.0000)
    prg.add(30000, "Rele 2 Close")
    prg.add(40000, "Rele 4 Close")
    prg.add(480000, "Rele 5 Open")
    prg.add(490000, "Rele 1 Open")
    prg.add(500000, "Rele 3 Open")
    return prg
