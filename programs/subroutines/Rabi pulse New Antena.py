prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO2 Amp", 1)
    prg.add(2000, "RFO", 591)
    prg.add(3000, "RFO2 Amp", 120)
    prg.add(4000, "RF02 ON")
    prg.add(4190, "RF02 OFF")
    prg.add(4640, "RFO", 0)
    prg.add(4740, "RFO2 Amp", 1)
    prg.add(4790, "RFO1 Amp", 1)
    prg.add(5010, "B comp x ramp", start_t=0, stop_x=1010, n_points=20, start_x=1882, stop_t=3)
    prg.add(30120, "Pulse uw ON")
    return prg
