prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "IGBT 1 pinch", 10.0000)
    prg.add(100, "IGBT 2 pinch+comp", -10.0000)
    prg.add(200, "IGBT 3 Open")
    prg.add(300, "IGBT 4 Close")
    prg.add(400, "IGBT 5 Open")
    prg.add(500, "IGBT 6 Open")
    prg.add(1000, "Rele 5 Close")
    prg.add(2000, "Rele 3 Open")
    prg.add(3000, "Rele 4 Close")
    prg.add(3000, "Decompress Current 200-50", start_t=0.0000, stop_x=4.100, n_points=200, start_x=0.000, stop_t=48.0000)
    prg.add(497990, "Delta 1 Current", 20.000, enable=False)
    prg.add(498000, "IGBT 1 pinch", -10.0000)
    prg.add(498100, "IGBT 4 Open")
    prg.add(498200, "IGBT 5 Open")
    prg.add(498400, "Delta 1 Current", 0.000)
    prg.add(503000, "ReleConfigBacktoSG2")
    prg.add(998000, "IGBT 5 Open")
    return prg
