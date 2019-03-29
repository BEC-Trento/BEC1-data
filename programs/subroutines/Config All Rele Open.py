prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Rele 1 Open")
    prg.add(10000, "Rele 2 Open")
    prg.add(20000, "Rele 3 Open")
    prg.add(30000, "Rele 4 Open")
    prg.add(40000, "Rele 5 Open")
    return prg
