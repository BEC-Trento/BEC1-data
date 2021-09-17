prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-2300, "Na Push (+) amp", 0)
    prg.add(-2200, "Na Probe y (+) amp", 0, enable=False)
    prg.add(-2100, "TTL Push OFF")
    prg.add(-2000, "Na Probe/Push (-) amp", 0, enable=False)
    prg.add(-1900, "Na Probe z (+) amp", 0)
    prg.add(-1800, "TTL Probe y OFF")
    prg.add(-1739, "Na Repumper1 (+) Amp", 0)
    prg.add(-1700, "TTL Probe z OFF")
    prg.add(-1600, "Na Zeeman slower (-) Amp", 0)
    prg.add(-1500, "Na 2D MOT (+) Amp", 0)
    prg.add(-1300, "Na Repumper2 (+) Amp", 0)
    prg.add(-1100, "TTL Repumper MOT OFF")
    prg.add(-1010, "Na 2D MOT (-) Amp", 0)
    prg.add(-1000, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 0)
    prg.add(1450, "Na 3D MOT cool (+) Amp", 0)
    prg.add(10000, "Shutter EOM Na Close", enable=False)
    prg.add(11000, "Shutter 2DMOT Close", enable=False)
    prg.add(11500, "Shutter Dark Spot Close", enable=False)
    prg.add(12000, "Shutter Probe/Push Close", enable=False)
    prg.add(15000, "Shutter 3DMOT cool Na Close", enable=False)
    prg.add(16000, "Shutter repump Na Close", enable=False)
    return prg
