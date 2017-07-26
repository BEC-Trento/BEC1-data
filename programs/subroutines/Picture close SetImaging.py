prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3050000, "Shutter repump Na Open")
    prg.add(-3000000, "Shutter Probe Na Open")
    prg.add(-2950000, "Shutter 3DMOT cool Na Open")
    prg.add(0, "Na Repumper1 (+) Amp", 1)
    prg.add(450, "Na Dark Spot Amp", 1)
    prg.add(900, "Na Repumper MOT Amp", 1)
    prg.add(1350, "Na Probe/Push (-) Amp", 1)
    prg.add(1800, "Na Probe/Push (+) Amp", 1)
    prg.add(2250, "Na 3D MOT cool (-) Amp", 1)
    prg.add(2700, "Na 3D MOT cool (+) Amp", 1)
    prg.add(3150, "Na Probe/Push (+) ON")
    prg.add(3600, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(4050, "Na Probe/Push (+) freq", 110.00)
    prg.add(4500, "Na Probe/Push (-) freq", 110.00)
    prg.add(4950, "Na Probe/Push (+) Amp", 1000)
    return prg
