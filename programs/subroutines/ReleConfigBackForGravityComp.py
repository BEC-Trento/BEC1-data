prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 4 Open")
    prg.add(100, "IGBT 5 Open")
    prg.add(5000, "Rele 3 Close")
    prg.add(10000, "Rele 1 Close")
    prg.add(20000, "Rele 5 Open")
    prg.add(40000, "Rele 2 Open")
    prg.add(500000, "Rele 4 Open")
    return prg
