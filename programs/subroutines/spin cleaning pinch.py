prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", 10.0000)
    prg.add(10000, "IGBT 2 pinch+comp", -10.0000)
    prg.add(20000, "Rele 5 Close")
    prg.add(480000, "IGBT 6 Open")
    prg.add(500000, "Decompress Current 200-50", start_t=0.0000, stop_x=12.000, n_points=150, start_x=0.000, stop_t=40.0000)
    prg.add(1000000, "Decompress Current 200-50", start_t=0.0000, stop_x=0.000, n_points=150, start_x=12.000, stop_t=40.0000)
    prg.add(1500000, "IGBT 4 Open")
    prg.add(1500100, "IGBT 5 Open")
    prg.add(1510000, "IGBT 6 Close")
    prg.add(1520000, "Rele 5 Open")
    prg.add(1530000, "IGBT 2 pinch+comp", 10.0000)
    prg.add(2000000, "IGBT 1 pinch", -10.0000)
    return prg
