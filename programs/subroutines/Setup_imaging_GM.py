prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1020000, "Shutter repump Na Open")
    prg.add(-1010000, "Shutter Probe/Push Open")
    prg.add(-1002000, "TTL Repumper MOT OFF")
    prg.add(-1001500, "TTL Push OFF")
    prg.add(-1001000, "TTL Probe z OFF")
    prg.add(-1000000, "TTL Probe y OFF")
    prg.add(-120000, "TTL Dark Spot OFF")
    prg.add(-57000, "Na Probe/Push (-) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-56000, "Na Probe y (+) amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(-55000, "Na Probe y (+) freq", 115.00, functions=dict(frequency=lambda x: 110+cmd.get_var('probe_det')/2))
    prg.add(-54000, "Na Probe/Push (-) freq", 105.00, functions=dict(frequency=lambda x: 110-cmd.get_var('probe_det')/2))
    prg.add(-23000, "Na Repumper2 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-22000, "Na Repumper1 (+) Amp", 1000, functions=dict(amplitude=lambda x: cmd.get_var('Rep_amp')))
    prg.add(-22000, "B comp x", 0.6, functions=dict(value=lambda x: cmd.get_var('Bx_GM'), funct_enable=False), enable=False)
    prg.add(-21000, "B comp y", 0.0000, functions=dict(value=lambda x: cmd.get_var('By_img')), enable=False)
    prg.add(-20000, "B comp z", 0.7500, functions=dict(value=lambda x: cmd.get_var('Bz_GM'), funct_enable=False), enable=False)
    return prg
