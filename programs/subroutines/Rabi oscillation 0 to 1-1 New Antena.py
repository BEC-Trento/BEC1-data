prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(800, "Analog71 Ramp", start_t=0.0000, stop_x=0.427, n_points=300, start_x=0.325, stop_t=50.0000)
    prg.add(900, "B comp y ramp", start_t=0, stop_x=0.023, n_points=300, start_x=0, stop_t=50)
    prg.add(1100, "B comp x ramp", start_t=0, stop_x=532, n_points=300, start_x=0, stop_t=50)
    prg.add(521100, "RFO2 Amp", 1)
    prg.add(523100, "RFO", 501)
    prg.add(524100, "RFO2 Amp", 1000)
    prg.add(525100, "RF02 ON")
    prg.add(525325, "RF02 OFF")
    prg.add(525425, "RFO", 0)
    prg.add(525525, "RFO2 Amp", 1)
    prg.add(525700, "Pulse uw ON")
    return prg
