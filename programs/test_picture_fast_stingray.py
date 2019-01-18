prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Mirrors Imaging")
    prg.add(9100000, "Picture SetRepumper")
    prg.add(9110000, "Picture SetImaging")
    prg.add(10220000, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(10369604, "Pulse TTL2-12", polarity=1, pulse_t=1.00000)
    prg.add(10369700, "Na Probe/Push (+) ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('probe_tau')))
    prg.add(10369700, "Na Probe/Push (+) OFF")
    prg.add(10370200, "TTL Repumper MOT ON")
    prg.add(10371700, "TTL Repumper MOT OFF")
    prg.add(10371800, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000)
    prg.add(10372800, "Na Probe/Push (+) ON")
    prg.add(10372800, "Na Probe/Push (+) OFF", functions=dict(time=lambda x: x + 1e-3*cmd.get_var('probe_tau')))
    prg.add(10530400, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000, enable=False)
    prg.add(11330100, "Pulse Trig Stingray 1", polarity=1, pulse_t=0.01000, enable=False)
    prg.add(28620000, "All AOM On.sub")
    return prg
