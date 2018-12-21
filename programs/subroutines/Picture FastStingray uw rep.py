prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1012300, "Picture SetRepumper")
    prg.add(-1002300, "Picture SetImaging")
    prg.add(-701700, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-2000, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau')))
    prg.add(-2000, "Na Probe/Push (+) OFF")
    prg.add(-1000, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(-950, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-550, "Na Probe/Push (+) ON")
    prg.add(-550, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(797150, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1596850, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000, enable=False)
    return prg
