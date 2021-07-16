prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-50000, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(-4339, "Probe z AOM TTL", enable=False)
    prg.add(-2250, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.15445)
    prg.add(-900, "Pulse uw with RF imaging", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')))
    prg.add(-310, "Repumper AOM TTL", enable=False)
    prg.add(-310, "Pulse uw ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(-310, "Pulse uw OFF", enable=False)
    prg.add(0, "Probe z AOM TTL")
    prg.add(999910, "Pulse Trig Stingray z", comment="probe", polarity=1, pulse_t=0.35400)
    prg.add(1001410, "Probe z AOM TTL")
    prg.add(1010000, "Na Probe/Push (-) amp", 0)
    prg.add(1011000, "Na Probe z (+) amp", 0)
    prg.add(1851934, "Shutter Probe/Push Close")
    prg.add(2016500, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000)
    return prg
