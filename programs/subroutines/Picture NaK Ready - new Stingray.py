prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1012300, "Picture SetRepumper", enable=False)
    prg.add(-300000, "Picture SetImaging", enable=False)
    prg.add(-1600, "TTL Repumper MOT ON")
    prg.add(-100, "TTL Repumper MOT OFF")
    prg.add(0, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1000, "Na Probe/Push (+) ON")
    prg.add(1000, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3* cmd.get_var('probe_tau')))
    prg.add(3000, "Na Probe/Push (+) Amp", 1000)
    prg.add(3500, "Na Probe/Push (-) Amp", 1000)
    prg.add(699500, "Na Probe/Push (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(700000, "Na Probe/Push (-) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(702300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(703000, "Na Probe/Push (+) ON")
    prg.add(703000, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3* cmd.get_var('probe_tau')))
    prg.add(800000, "Shutter Probe Na Close")
    prg.add(1498600, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(1900000, "Na Probe/Push (+) ON")
    prg.add(1901000, "Na Probe/Push (+) Amp", 1000)
    prg.add(1902000, "Na Probe/Push (-) Amp", 1000)
    prg.add(2298300, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000, enable=False)
    return prg
