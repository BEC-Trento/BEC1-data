prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Probe y (+) amp", 0)
    prg.add(5000, "Na Probe z (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp')))
    prg.add(10000, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('push_amp')))
    prg.add(20000, "Na Probe y (+) freq", 60.00)
    prg.add(25000, "Na Probe z (+) freq", 0.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(30000, "Na Probe/Push (-) freq", 0.00, functions=dict(frequency=lambda x: 110-cmd.get_var('push_det')/2))
    prg.add(35000, "TTL Probe y OFF")
    prg.add(40000, "TTL Probe z ON")
    prg.add(115000, "Shutter Probe/Push Open")
    return prg
