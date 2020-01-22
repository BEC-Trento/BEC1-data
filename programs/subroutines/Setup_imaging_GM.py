prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-110000, "Shutter repump Na Open")
    prg.add(-100000, "Shutter Probe/Push Open")
    prg.add(-14000, "TTL Repumper MOT OFF")
    prg.add(-13000, "TTL Push OFF")
    prg.add(-12000, "TTL Probe z OFF")
    prg.add(-11000, "TTL Dark Spot OFF")
    prg.add(-10000, "TTL Probe y OFF")
    prg.add(-3500, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-3000, "Na Probe y (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-2500, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-2000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(0, "Na Repumper2 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')), enable=False)
    prg.add(0, "Na Repumper1 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')), enable=False)
    return prg
