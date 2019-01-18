prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1112300, "Picture SetRepumper")
    prg.add(-1102300, "Picture SetImaging")
    prg.add(-702300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-2600, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau')))
    prg.add(-2600, "Na Probe/Push (+) OFF")
    prg.add(-2054, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(-1700, "Pulse uw", polarity=1, pulse_t=0.00000, functions=dict(pulse_t=lambda x: 1e-3*cmd.get_var('uw_tau')))
    prg.add(-1680, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('uw_tau')))
    prg.add(-1680, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*(cmd.get_var('probe_tau') + cmd.get_var('uw_tau'))))
    prg.add(1560000, "Na Probe/Push (+) Amp", 10, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(1570000, "Na Probe/Push (-) Amp", 10, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(1595999, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1596999, "Na Probe/Push (+) ON")
    prg.add(1596999, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(2396699, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    return prg
