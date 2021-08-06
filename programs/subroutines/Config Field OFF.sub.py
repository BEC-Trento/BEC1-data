prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(20, "IGBT 3 Open")
    prg.add(30, "IGBT 4 Open")
    prg.add(50, "IGBT 2 Open")
    prg.add(60, "IGBT 5 Open")
    prg.add(5069, "Delta 1 Current", 0.000)
    return prg
