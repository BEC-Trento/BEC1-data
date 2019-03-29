prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(8000, "RFO", 701)
    prg.add(8500, "RFO2 Amp", 300)
    prg.add(9000, "B comp x", 100.0, enable=False)
    prg.add(10000, "B comp x ramp", start_t=0, stop_x=1000, n_points=200, start_x=0, stop_t=30)
    prg.add(10100, "RF02 ON")
    prg.add(310100, "RF02 OFF")
    prg.add(310500, "B comp x", 0.0)
    prg.add(311100, "RFO2 Amp", 1)
    prg.add(312100, "RFO", 0)
    return prg
