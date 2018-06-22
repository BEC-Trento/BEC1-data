prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Delta 1 Current ramp", start_t=0.0000, stop_x=50.000, n_points=100, start_x=12.000, stop_t=1000.0000)
    prg.add(11000000, "Pulse TTL2-12", polarity=1, pulse_t=0.56000)
    prg.add(11010000, "MT trap Heating", start_t=0.0000, func_args="amp=5, freq=160, offs=50", n_points=200, func="amp*sin(2*pi*freq*t) + offs", stop_t=18.0000)
    prg.add(20000000, "Delta 1 Current ramp", start_t=0.0000, stop_x=12.000, n_points=100, start_x=50.000, stop_t=1000.0000)
    return prg
