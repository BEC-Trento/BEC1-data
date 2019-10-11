prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(10000, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(20000, "TTL Probe y ON")
    prg.add(25000, "TTL Probe z ON")
    prg.add(30000, "Mirrors Imaging")
    prg.add(100000, "Shutter Probe/Push Open")
    return prg
