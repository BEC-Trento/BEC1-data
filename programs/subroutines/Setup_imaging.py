prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-5500000, "Na Probe/Push (+) OFF")
    prg.add(-5498990, "Scope 1 Trigger ON", enable=False)
    prg.add(-5490000, "Na Probe/Push (-) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-5489000, "Na Probe/Push (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-5488000, "Na Probe/Push (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-5487000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(-5479000, "Shutter Probe Na Open")
    prg.add(-2989000, "Shutter repump Na Open")
    prg.add(-2699000, "TTL Dark Spot OFF")
    prg.add(-2599000, "TTL Repumper MOT OFF")
    prg.add(-2598000, "Na Repumper2 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-2597000, "Na Repumper1 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-149000, "B comp x", 0.6, functions=dict(value=lambda x: cmd.get_var('Bx_GM'), funct_enable=False), enable=False)
    prg.add(-148000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_img')), enable=False)
    prg.add(-147000, "B comp z", 0.7500, functions=dict(value=lambda x: cmd.get_var('Bz_GM'), funct_enable=False), enable=False)
    prg.add(-12000, "Na Probe/Push (+) OFF")
    return prg
