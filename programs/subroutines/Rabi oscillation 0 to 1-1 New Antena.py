prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(800, "Analog71 Ramp", start_t=0.0000, stop_x=0.250, n_points=300, start_x=0.325, stop_t=50.0000)
    prg.add(1100, "B comp x ramp", start_t=0, stop_x=180, n_points=300, start_x=0, stop_t=50)
    prg.add(505000, "RFO", 701)
    prg.add(506000, "RFO2 Amp", 30)
    prg.add(510000, "RF02 ON")
    prg.add(510020, "RF02 OFF")
    prg.add(516100, "RFO2 Amp", 1)
    prg.add(517000, "RFO", 0)
    prg.add(520000, "IGBT B comp x OFF", enable=False)
    prg.add(540000, "RFO1 Amp", 1, enable=False)
    prg.add(550000, "B comp x ramp", start_t=0, stop_x=0, n_points=300, start_x=77, stop_t=50, enable=False)
    return prg
