prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(1000000, "Pinning Lock ramp", start_t=0, stop_x=8, n_points=100, start_x=0, stop_t=2)
    prg.add(1050000, "Pinning Lock ramp", start_t=0, stop_x=0, n_points=100, start_x=8, stop_t=2)
    return prg
