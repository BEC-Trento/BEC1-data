prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Scope 1 Trigger Pulse", polarity=1, pulse_t=0.01048)
    prg.add(100, "B comp x func", start_t=0.0000, func_args="amp=0.5, freq=100, offset=0.6", n_points=100, func="amp*sin(2*pi*freq*t) + offset", stop_t=500.0000)
    return prg
