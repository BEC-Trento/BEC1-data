prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1112300, "Picture SetRepumper")
    prg.add(-1102300, "Picture SetImaging")
    prg.add(-702300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-2600, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau')))
    prg.add(-2600, "Na Probe/Push (+) OFF")
    prg.add(-1600, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(-1600, "empty.sub")
    prg.add(-1554, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-550, "Na Probe/Push (+) ON")
    prg.add(-550, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(797100, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(798100, "Na Probe/Push (+) ON")
    prg.add(798100, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(1597800, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    return prg
