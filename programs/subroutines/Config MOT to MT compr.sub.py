prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-10000, "IGBT 2 pinch+comp", 10.0000)
    prg.add(0, "IGBT 3 Open")
    prg.add(10, "TTL2-12 OFF", enable=False)
    return prg
