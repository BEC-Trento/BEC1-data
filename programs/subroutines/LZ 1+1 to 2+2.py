prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "B comp x ramp", start_t=0, stop_x=900, n_points=20, start_x=0, stop_t=2)
    prg.add(19900, "Pulse 2 uw ON")
    prg.add(39900, "B comp x ramp", start_t=0, stop_x=1100, n_points=10, start_x=900, stop_t=0.5)
    prg.add(45900, "Pulse 2 uw OFF")
    prg.add(46900, "B comp x ramp", start_t=0, stop_x=0, n_points=20, start_x=1100, stop_t=2)
    return prg
