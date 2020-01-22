prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2933000, "TTL Probe y OFF")
    prg.add(-2913000, "TTL Push OFF")
    prg.add(-2903000, "Na Probe/Push (-) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_push_amp')))
    prg.add(-2902500, "Na Probe y (+) amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-112000, "TTL Dark Spot OFF")
    prg.add(-101000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(-100500, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-12000, "TTL Repumper MOT OFF")
    prg.add(-11000, "Na Repumper2 (+) Amp", 1, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    prg.add(-10000, "Na Repumper1 (+) Amp", 1, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    prg.add(-5000, "Shutter repump Na Open")
    return prg
