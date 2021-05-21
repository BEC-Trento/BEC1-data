prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(20000, "Dipole Trap x ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000)
    return prg
