prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Scope 2 Trigger Pulse", polarity=1, pulse_t=0.01230)
    prg.add(10, "B comp x", 1.0, enable=False)
    prg.add(10, "B comp x func", start_t=0.0000, func_args="amp=0.5, freq=10, offset=1", n_points=500, func="amp*sin(2*pi*freq*t) + offset", stop_t=500.0000)
    prg.add(6000000, "B comp x", 0.0)
    return prg
