prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3000000, "Shutter Probe Na Close")
    prg.add(-11600, "Na Probe/Push (+) Amp", 1, enable=False)
    prg.add(-11200, "Na Probe/Push (-) Amp", 1, enable=False)
    prg.add(-11000, "Na Zeeman slower (-) Amp", 1, enable=False)
    prg.add(-10900, "Na 2D MOT (+) Amp", 1, enable=False)
    prg.add(-10800, "Na Dark Spot Amp", 1, enable=False)
    prg.add(-5000, "Na Repumper MOT Amp", 1, enable=False)
    prg.add(-4900, "Na Repumper1 (+) Amp", 1, enable=False)
    prg.add(0, "Na 3D MOT cool (-) Amp", 1, enable=False)
    prg.add(0, "MOT lights Off close.sub")
    prg.add(1000, "Na 3D MOT cool (+) Amp", 1, enable=False)
    return prg
