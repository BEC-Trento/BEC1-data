prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Analog72", 0.0000)
    prg.add(0, "Analog72 ramp", start_t=0.0000, stop_x=1.000, n_points=100, start_x=0.000, stop_t=2000.0000, enable=False)
    prg.add(10000000, "Analog72", 1.0000)
    prg.add(20000000, "Analog72", 0.0000)
    return prg
def commands(cmd):
    a=[4,5,6]
    cmd.set_var("hhh", 4)
    while(cmd.running):
        a.pop()
        if len(a) == 0:
         cmd.stop()
    return prg
