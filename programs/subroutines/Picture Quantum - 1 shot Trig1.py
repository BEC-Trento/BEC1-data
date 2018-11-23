prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1000, "Trig ON Stingray 1")
    prg.add(0, "Picture Set Probe Pulse.sub", enable=False)
    prg.add(0, "Pulse Probe Na", polarity=1, pulse_t=0.10000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('probe_tau')))
    prg.add(2000, "Trig OFF Stingray 1")
    return prg
