prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-702680, "Pulse Trig Stingray z", comment="F1", polarity=1, pulse_t=0.10000, enable=False)
    prg.add(-310, "Repumper AOM TTL")
    prg.add(-310, "Pulse uw ON", functions=dict(time=lambda x: x - 1e-3*cmd.get_var('marconi1_pulsetime')), enable=False)
    prg.add(-310, "Pulse uw OFF", enable=False)
    prg.add(-300, "Pulse Trig Stingray z", comment="atoms", polarity=1, pulse_t=0.15445)
    prg.add(0, "Probe z AOM TTL")
    prg.add(999910, "Pulse Trig Stingray z", comment="probe", polarity=1, pulse_t=0.35400)
    prg.add(1001410, "Probe z AOM TTL")
    prg.add(1010000, "Na Probe/Push (-) amp", 0)
    prg.add(1011000, "Na Probe z (+) amp", 0)
    prg.add(2016500, "Pulse Trig Stingray z", comment="dark", polarity=1, pulse_t=0.10000)
    prg.add(3851934, "Shutter Probe/Push Close")
    return prg