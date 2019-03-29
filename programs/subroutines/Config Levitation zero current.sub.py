prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(50, "IGBT 1 pinch", -10.0000)
    prg.add(60, "IGBT 2 pinch+comp", -10.0000)
    prg.add(70, "IGBT 3 Close")
    prg.add(80, "IGBT 4 Close")
    prg.add(90, "IGBT 5 Open")
    return prg
