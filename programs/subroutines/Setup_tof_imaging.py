prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-250000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(-249500, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-162000, "TTL Dark Spot OFF")
    prg.add(-161000, "TTL Repumper MOT OFF")
    prg.add(-160000, "Na Repumper2 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    prg.add(-159000, "Na Repumper1 (+) Amp", 0, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp'), funct_enable=False))
    prg.add(-152000, "Shutter repump Na Open")
    return prg
