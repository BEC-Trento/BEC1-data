prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-520000, "TTL Probe y OFF")
    prg.add(-510000, "TTL Probe z OFF")
    prg.add(-500000, "TTL Push OFF")
    prg.add(-490000, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(-489500, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-489000, "Na Probe z (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-488000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(-487500, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-487000, "Na Probe z (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-150000, "Shutter Probe/Push Open")
    return prg
