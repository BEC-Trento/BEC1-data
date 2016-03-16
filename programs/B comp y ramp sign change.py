prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "B comp y ramp", start_t=0, stop_x=0.09, n_points=100, start_x=1500, stop_t=100)
    prg.add(950000, "Bcomp y Sign Minus", enable=False)
    prg.add(1050000, "B comp y ramp", start_t=0, stop_x=0.02, n_points=100, start_x=0, stop_t=100, enable=False)
    return prg
