prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO2 Amp", 1)
    prg.add(2000, "RFO", 591)
    prg.add(3000, "RFO2 Amp", 120)
    prg.add(4000, "RF02 ON")
    prg.add(4180, "RF02 OFF")
    prg.add(4630, "RFO", 0)
    prg.add(4730, "RFO2 Amp", 1)
    prg.add(4780, "RFO1 Amp", 1)
    prg.add(5000, "B comp x ramp", start_t=0, stop_x=1000, n_points=20, start_x=1880, stop_t=3)
    prg.add(37000, "Pulse uw ON")
    return prg
