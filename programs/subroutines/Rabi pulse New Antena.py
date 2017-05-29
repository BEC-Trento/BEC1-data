prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO2 Amp", 1)
    prg.add(2000, "RFO", 701)
    prg.add(2500, "RFO2 Amp", 170)
    prg.add(3000, "RF02 ON")
    prg.add(3120, "RF02 OFF")
    prg.add(3500, "B comp x", 800.0)
    prg.add(3575, "Pulse uw ON")
    prg.add(4185, "RFO", 0)
    prg.add(4285, "RFO2 Amp", 1)
    prg.add(4335, "RFO1 Amp", 1)
    prg.add(4555, "B comp x ramp", start_t=0, stop_x=1010, n_points=20, start_x=1882, stop_t=3, enable=False)
    return prg
