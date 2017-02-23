prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "TTL2 ON", enable=False)
    prg.add(0, "TTL2-15 ON")
    prg.add(10000, "B comp y", 0.0000)
    prg.add(2000000, "B comp y ramp", start_t=0, stop_x=2, n_points=200, start_x=0, stop_t=130)
    prg.add(5500000, "B comp y ramp", start_t=0, stop_x=0, n_points=100, start_x=2, stop_t=130)
    prg.add(7000000, "TTL2-15 OFF")
    return prg
