prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(100, "IGBT B comp x ON")
    prg.add(150, "IGBT B comp y ON")
    prg.add(200, "IGBT 5 Open")
    prg.add(300, "IGBT 4 Open")
    prg.add(2500, "B comp x ramp", start_t=0, stop_x=850, n_points=300, start_x=1369, stop_t=150)
    prg.add(1511000, "B comp y ramp", start_t=0, stop_x=0.058, n_points=300, start_x=3, stop_t=150)
    prg.add(3021000, "Analog71 Ramp", start_t=0.0000, stop_x=0.800, n_points=300, start_x=0.000, stop_t=50.0000)
    return prg
