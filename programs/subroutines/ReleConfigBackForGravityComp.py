prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 4 Open")
    prg.add(100, "IGBT 5 Open")
    prg.add(2000, "IGBT 6 Open")
    prg.add(4000, "IGBT 1 pinch", -10.0000)
    prg.add(5000, "Rele 3 Close")
    prg.add(6000, "IGBT 2 pinch+comp", -10.0000)
    prg.add(8000, "Rele 5 Close")
    prg.add(10000, "Rele 1 Close")
    prg.add(40000, "Rele 2 Open")
    prg.add(50000, "Rele 4 Open")
    return prg
