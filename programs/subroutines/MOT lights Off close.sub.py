prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-11600, "Na Probe/Push (+) Amp", 1)
    prg.add(-11200, "Na Probe/Push (-) Amp", 1)
    prg.add(-10800, "Na Repumper MOT Amp", 1)
    prg.add(-10400, "Na Zeeman slower (-) Amp", 1)
    prg.add(-10000, "Na 2D MOT (+) Amp", 1)
    prg.add(0, "Na Dark Spot Amp", 1)
    prg.add(1200, "Na Repumper1 (+) Amp", 1)
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(2500, "Na 3D MOT cool (+) Amp", 1)
    return prg
