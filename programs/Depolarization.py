prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "B comp x", 0.8)
    prg.add(10000, "B comp y", 0.0000)
    prg.add(20000, "B comp z", 0.7100)
    prg.add(30000, "B comp x ramp", start_t=0, stop_x=0.6, n_points=50, start_x=0.8, stop_t=50)
    prg.add(40000, "B comp y ramp", start_t=0, stop_x=0.1, n_points=50, start_x=0, stop_t=50)
    prg.add(50000, "B comp z ramp", start_t=0.0000, stop_x=0.900, n_points=50, start_x=0.710, stop_t=50.0000)
    prg.add(530000, "B comp x", 1.4)
    prg.add(540000, "B comp y", 0.0400)
    prg.add(550000, "B comp z", 0.8100)
    return prg
