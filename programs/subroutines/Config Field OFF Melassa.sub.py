prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", -10.000000)
    prg.add(10, "IGBT 2 pinch+comp", -10.000000)
    prg.add(20, "IGBT 5 Open")
    return prg
