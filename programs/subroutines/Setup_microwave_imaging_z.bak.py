prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5520000, "TTL Probe y OFF")
    prg.add(-5510000, "TTL Probe z OFF")
    prg.add(-5500000, "TTL Push OFF")
    prg.add(-5499000, "Shutter Probe/Push Open")
    prg.add(-5490000, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(-5489500, "Na Probe y (+) amp", 0)
    prg.add(-5489000, "Na Probe z (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_z_amp')))
    prg.add(-5488000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_z_det')/2))
    prg.add(-5487000, "Na Probe z (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_z_det')/2))
    prg.add(-2699000, "TTL Dark Spot OFF")
    prg.add(-2599000, "TTL Repumper MOT OFF")
    prg.add(-2598000, "Na Repumper2 (+) Amp", 1, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    prg.add(-2597000, "Na Repumper1 (+) Amp", 1, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    return prg
