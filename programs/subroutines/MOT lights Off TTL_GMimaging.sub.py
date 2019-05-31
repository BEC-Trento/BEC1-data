prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-12000, "Na Probe/Push (+) Amp", 0, enable=False)
    prg.add(-11600, "Na Probe/Push (+) OFF", enable=False)
    prg.add(-11200, "Na Probe/Push (-) Amp", 0, enable=False)
    prg.add(-11000, "Na Zeeman slower (-) Amp", 0)
    prg.add(-10900, "Na 2D MOT (+) Amp", 0)
    prg.add(-10400, "Na 2D MOT (-) Amp", 0)
    prg.add(-5800, "Na Repumper2 (+) Amp", 0)
    prg.add(-5400, "Na Repumper1 (+) Amp", 0)
    prg.add(-5000, "TTL Repumper MOT OFF")
    prg.add(-4900, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 0)
    prg.add(1000, "Na 3D MOT cool (+) Amp", 0)
    prg.add(140000, "Shutter EOM Na Close")
    prg.add(145000, "Shutter 3DMOT cool Na Close")
    prg.add(150000, "Shutter Push Na Close")
    prg.add(160000, "Shutter repump Na Close")
    return prg
