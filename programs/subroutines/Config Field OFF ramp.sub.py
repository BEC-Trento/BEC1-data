prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", -10.0000)
    prg.add(20, "IGBT 3 Open")
    prg.add(60, "IGBT 2 ramp", start_t=0.0000, stop_x=-10.000, n_points=101, start_x=10.000, stop_t=1.0000)
    prg.add(10100, "IGBT 4 Open")
    prg.add(10120, "IGBT 5 Open")
    prg.add(10220, "IGBT 6 Open")
    return prg
