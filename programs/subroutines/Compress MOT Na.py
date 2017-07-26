prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Na 3D MOT cool (-) freq ramp", start_t=0.0000, stop_x=126.000, n_points=100, start_x=120.000, stop_t=20.0000)
    prg.add(0, "Na 3D MOT cool (-) freq", 130.00, enable=False)
    prg.add(100, "Na 3D MOT cool (+) freq ramp", start_t=0.0000, stop_x=94.000, n_points=100, start_x=100.000, stop_t=20.0000)
    prg.add(100, "Na 3D MOT cool (+) freq", 90.00, enable=False)
    prg.add(490, "TTL2-12 ON")
    prg.add(500, "Delta 1 Current ramp", start_t=0.0000, stop_x=16.000, n_points=188, start_x=12.000, stop_t=20.0000)
    prg.add(1000, "Na Repumper1 (+) Amp ramp", start_t=0.0000, stop_x=900.000, n_points=100, start_x=1000.000, stop_t=5.0000, enable=False)
    prg.add(20513, "TTL2-12 OFF")
    return prg
