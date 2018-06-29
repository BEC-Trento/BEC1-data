prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "open Probe", enable=False)
    prg.add(0, "startup.prg")
    prg.add(10000000, "Pulse TTL2-12", polarity=1, pulse_t=0.25000)
    prg.add(15000000, "Picture SetImaging")
    prg.add(17000000, "TTL2-12 Pulse Ramp", start_t=0.0000, stop_x=0.1500, n_points=50, start_x=0.1500, stop_t=4000.0000)
    prg.add(17000010, "Pulse Probe Na", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(17000010, "Probe Pulse Ramp", start_t=0.0000, stop_x=0.1000, n_points=50, start_x=0.1000, stop_t=4000.0000, enable=False)
    prg.add(17000010, "Picture Ramp Trig1", start_t=0.0000, stop_x=0.000, n_points=30, start_x=1.000, stop_t=2900.0000)
    return prg
