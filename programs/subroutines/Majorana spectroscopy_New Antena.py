prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(800, "Analog71 Ramp", start_t=0.0000, stop_x=0.200, n_points=300, start_x=0.000, stop_t=400.0000)
    prg.add(900, "B comp y ramp", start_t=0, stop_x=0, n_points=300, start_x=0, stop_t=400)
    prg.add(1100, "B comp x ramp", start_t=0, stop_x=0, n_points=300, start_x=0, stop_t=400)
    prg.add(4100000, "B comp x ramp", start_t=0, stop_x=8000, n_points=300, start_x=0, stop_t=200)
    return prg
