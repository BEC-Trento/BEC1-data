prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-601600, "Na Probe/Push (+) Amp", 1)
    prg.add(-600300, "Na Probe/Push (-) Amp", 1)
    prg.add(-9300, "Na Zeeman slower (-) Amp", 1)
    prg.add(-8300, "Na 2D MOT (+) Amp", 1)
    prg.add(-6700, "TTL Repumper MOT OFF")
    prg.add(-2100, "Na Repumper1 (+) Amp", 1)
    prg.add(-1900, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 1)
    prg.add(600, "Na 3D MOT cool (+) Amp", 1)
    return prg
