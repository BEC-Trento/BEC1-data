prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Dipole Trap x rise ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=100.0000)
    prg.add(3000000, "Dipole Trap x DAC V", 0.0000)
    return prg
