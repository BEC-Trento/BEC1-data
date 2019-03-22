prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-1200, "Na Probe/Push (+) OFF")
    prg.add(-1000, "Na Zeeman slower (-) Amp", 1)
    prg.add(-500, "Na 2D MOT (+) Amp", 1)
    prg.add(-200, "TTL Repumper MOT OFF")
    prg.add(-100, "TTL Dark Spot OFF")
    prg.add(0, "Na 3D MOT cool (-) Amp", 1)
    prg.add(100, "Na Probe/Push (+) Amp", 1000)
    prg.add(500, "Na 3D MOT cool (+) Amp", 1)
    prg.add(1000, "Na Repumper Tune (+) freq", 1712.0)
    prg.add(1500, "Na Repumper2 (+) Amp", 1000)
    prg.add(1600, "Na Probe/Push (-) Amp", 1000, enable=False)
    prg.add(1610, "Trigger LZ OFF")
    return prg
