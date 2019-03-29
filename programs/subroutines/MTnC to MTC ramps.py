prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5000, "IGBT 2 ramp", start_t=0.0000, stop_x=10.000, n_points=70, start_x=5.000, stop_t=1500.0000)
    prg.add(0, "IGBT 1 ramp", start_t=0.0000, stop_x=5.000, n_points=70, start_x=10.000, stop_t=1500.0000)
    prg.add(15010000, "IGBT 1 pinch", -10.0000)
    return prg
