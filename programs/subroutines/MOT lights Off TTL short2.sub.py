prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4600, "Na Probe/Push (+) Amp", 1, enable=False)
    prg.add(-4600, "Na Probe/Push (-) Amp", 1, enable=False)
    prg.add(-3000, "Na Dark Spot Amp", 1, enable=False)
    prg.add(-2900, "Na Repumper1 (+) Amp", 1, enable=False)
    prg.add(-2000, "Na Repumper MOT Amp", 1, enable=False)
    prg.add(-1200, "Na Probe/Push (+) OFF")
    prg.add(-1000, "Na Zeeman slower (-) Amp", 1)
    prg.add(-500, "Na 2D MOT (+) Amp", 1)
    prg.add(-200, "TTL Repumper MOT OFF")
    prg.add(-100, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 1)
    prg.add(500, "Na 3D MOT cool (+) Amp", 1)
    return prg
