prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=151, start_x=200.000, stop_t=200.0000)
    prg.add(500, "Delta 2 Voltage ramp", start_t=0.0000, stop_x=0.000, n_points=151, start_x=30.000, stop_t=200.0000)
    return prg
