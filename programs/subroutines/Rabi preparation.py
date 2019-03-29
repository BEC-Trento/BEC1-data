prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(1000, "B comp x ramp", start_t=0, stop_x=2000, n_points=300, start_x=330, stop_t=100, enable=False)
    prg.add(1001000, "B comp y ramp", start_t=0, stop_x=0, n_points=200, start_x=0, stop_t=100)
    prg.add(1002000, "Analog71 Ramp", start_t=0.0000, stop_x=0.425, n_points=300, start_x=0.325, stop_t=100.0000)
    prg.add(3052000, "B comp x ramp", start_t=0, stop_x=1050, n_points=200, start_x=0, stop_t=100)
    return prg
