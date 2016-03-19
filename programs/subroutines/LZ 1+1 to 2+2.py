prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "B comp x", 850.0)
    prg.add(5000, "Pulse 2 uw ON")
    prg.add(6000, "B comp x ramp", start_t=0, stop_x=950, n_points=100, start_x=850, stop_t=5)
    prg.add(50500, "Pulse 2 uw OFF")
    prg.add(51000, "B comp x", 0.0)
    return prg
