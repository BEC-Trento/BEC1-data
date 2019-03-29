prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-2000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-1600, "Na Repumper MOT Amp", 1.000000)
    prg.add(-800, "Na 2D MOT (+) Amp", 1.000000)
    prg.add(-400, "Na Zeeman slower (-) Amp", 1.000000)
    prg.add(0, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(400, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(800, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(1200, "Na Dark Spot Amp", 1.000000)
    prg.add(2000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(2500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(2900, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(4500, "Na Repumper MOT Amp", 1.000000)
    prg.add(4900, "Na Repumper1 (+) Amp", 1.000000)
    return prg
