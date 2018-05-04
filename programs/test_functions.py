prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL2-12 ON")
    prg.add(10000, "Dipole y Func", start_t=0.0000, func_args="amp=5, t0 = 0.1", n_points=500, func="amp*(arctan((t-0.5*stop_t)/t0)/pi + 0.5)", stop_t=2500.0000)
    prg.add(10000, "Pulse uw Func", start_t=0.0000, func_args="fr = 200, a=2", n_points=25, func="a*sin(2*pi*fr*t)**2 + 1", stop_t=100.0000, enable=False)
    prg.add(10050000, "TTL2-12 OFF")
    prg.add(30100000, "Dipole Trap y DAC V", 0.0000)
    return prg
