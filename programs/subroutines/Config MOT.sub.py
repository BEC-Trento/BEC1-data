prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10, "Rele 1 Close")
    prg.add(20, "Rele 2 Open")
    prg.add(30, "Rele 3 Close")
    prg.add(40, "Rele 4 Open")
    prg.add(50, "Rele 5 Close")
    prg.add(80, "IGBT 3 Close")
    prg.add(90, "IGBT 4 Open")
    prg.add(100, "IGBT 5 Close")
    prg.add(110, "IGBT 2 Open")
    return prg
