prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open", enable=False)
    prg.add(300, "IGBT 4 Open", enable=False)
    prg.add(1000, "Analog71 Ramp", start_t=0.0000, stop_x=0.425, n_points=300, start_x=0.000, stop_t=150.0000)
    prg.add(1500, "B comp x ramp", start_t=0, stop_x=370, n_points=300, start_x=1369, stop_t=150)
    prg.add(1510000, "B comp y ramp", start_t=0, stop_x=0, n_points=300, start_x=2, stop_t=150)
    return prg
