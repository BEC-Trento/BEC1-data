prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Decompress Current 200-100", start_t=0.0000, stop_x=0.000, n_points=300, start_x=50.000, stop_t=198.0000)
    prg.add(1995000, "IGBT 5 Open")
    prg.add(1996000, "IGBT 4 Open")
    return prg
