prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "GM ON")
    prg.add(7500, "GM amp(+) ramp", start_t=0, stop_x=750, n_points=15, start_x=1000, stop_t=1)
    prg.add(18000, "Na Gray molasses (+) freq", 125.00)
    prg.add(18500, "Na Gray molasses (-) freq", 75.00)
    prg.add(19000, "GM amp(+) ramp", start_t=0, stop_x=200, n_points=30, start_x=750, stop_t=3)
    prg.add(50000, "GM OFF")
    return prg
