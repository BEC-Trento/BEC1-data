prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 6 Open")
    prg.add(100, "IGBT 1 pinch", -10.0000)
    prg.add(200, "IGBT 2 pinch+comp", -10.0000)
    prg.add(300, "IGBT 3 Close")
    prg.add(400, "IGBT 4 Close")
    prg.add(500, "IGBT 5 Open")
    prg.add(1000, "Decompress Current 200-50", start_t=0.0000, stop_x=10.000, n_points=200, start_x=0.000, stop_t=98.0000)
    prg.add(1000000, "IGBT 3 Open")
    return prg
