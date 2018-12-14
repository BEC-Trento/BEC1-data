prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1000)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1000)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2010000, "Na 3D MOT cool (-) OFF")
    prg.add(-710000, "Na Probe/Push (+) OFF")
    prg.add(-700000, "Shutter Probe Na Open")
    prg.add(-99564, "Na Probe/Push (+) freq", 110.00, functions=dict(frequency=lambda x: x + cmd.get_var('probe_det')/2))
    prg.add(-90000, "Na Probe/Push (-) freq", 110.00, functions=dict(frequency=lambda x: x - cmd.get_var('probe_det')/2))
    prg.add(-10000, "Na Probe/Push (-) Amp", 300, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    prg.add(0, "Na Probe/Push (+) Amp", 300, functions=dict(amplitude=lambda x: cmd.get_var('probe_amp')))
    return prg
