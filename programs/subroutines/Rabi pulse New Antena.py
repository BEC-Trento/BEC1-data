prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "RFO2 Amp", 1)
    prg.add(2000, "RFO", 651)
    prg.add(3000, "RFO2 Amp", 160)
    prg.add(4000, "RF02 ON")
    prg.add(4160, "RF02 OFF")
    prg.add(4210, "Pulse uw ON")
    prg.add(4780, "RFO", 0)
    prg.add(4880, "RFO2 Amp", 1)
    prg.add(4930, "RFO1 Amp", 1)
    prg.add(5150, "B comp x ramp", start_t=0, stop_x=1010, n_points=20, start_x=1882, stop_t=3, enable=False)
    return prg
