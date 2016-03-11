prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(800, "Analog71 Ramp", start_t=0.0000, stop_x=0.400, n_points=300, start_x=0.325, stop_t=50.0000)
    prg.add(900, "B comp y ramp", start_t=0, stop_x=1200, n_points=300, start_x=1500, stop_t=50)
    prg.add(1100, "B comp x ramp", start_t=0, stop_x=3700, n_points=300, start_x=0, stop_t=50)
    prg.add(521100, "RFO2 Amp", 1)
    prg.add(523100, "RFO", 791)
    prg.add(524100, "RFO2 Amp", 40)
    prg.add(525100, "RF02 ON")
    prg.add(525600, "RF02 OFF")
    prg.add(525700, "RFO", 0)
    prg.add(525800, "RFO2 Amp", 1)
    prg.add(525850, "RFO1 Amp", 1)
    prg.add(525975, "Pulse uw ON", enable=False)
    return prg
