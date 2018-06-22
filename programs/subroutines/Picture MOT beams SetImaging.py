prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-2040000, "Na 3D MOT cool (-) OFF")
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(-190000, "Na 3D MOT cool (+) freq", 110.00)
    prg.add(-180000, "Na 3D MOT cool (-) freq", 110.00)
    prg.add(-150000, "Na Probe/Push (+) OFF")
    prg.add(-99564, "Na Probe/Push (+) freq", 110.00, functions=dict(frequency=lambda x: x + 0.5*cmd.get_var('det'), funct_enable=False))
    prg.add(-90000, "Na Probe/Push (-) freq", 110.00, functions=dict(frequency=lambda x: x - 0.5*cmd.get_var('det'), funct_enable=False))
    prg.add(-10000, "Na Probe/Push (-) Amp", 1000)
    prg.add(0, "Na Probe/Push (+) Amp", 1000)
    return prg
