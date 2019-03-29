prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(50, "TTL RF OFF")
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(800, "Analog71 Ramp", start_t=0.0000, stop_x=0.200, n_points=300, start_x=1.000, stop_t=50.0000)
    prg.add(900, "B comp y ramp", start_t=0, stop_x=0, n_points=300, start_x=0, stop_t=50)
    prg.add(1100, "B comp x ramp", start_t=0, stop_x=850, n_points=300, start_x=0, stop_t=50)
    prg.add(505000, "RFO", 201)
    prg.add(506000, "RFO1 Amp", 1000)
    prg.add(507000, "TTL RF ON")
    prg.add(507150, "TTL RF OFF")
    prg.add(507160, "RFO1 Amp", 0)
    prg.add(507170, "RFO", 0)
    prg.add(507200, "Pulse uw ON")
    return prg
