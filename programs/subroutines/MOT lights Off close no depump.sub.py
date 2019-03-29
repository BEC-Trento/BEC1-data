prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-11600, "Na Probe/Push (+) Amp", 1)
    prg.add(-10300, "Na Probe/Push (-) Amp", 1)
    prg.add(-9300, "Na Zeeman slower (-) Amp", 1)
    prg.add(-8300, "Na 2D MOT (+) Amp", 1)
    prg.add(-6700, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-1600, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-1300, "TTL Dark Spot OFF")
    prg.add(0, "TTL Repumper MOT OFF")
    prg.add(6000, "Na Repumper1 (+) Amp", 1)
    return prg
