prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-6000000, "Shutter Probe Na Open")
    prg.add(-2400000, "Na Repumper1 (+) Amp", 1)
    prg.add(-2300000, "Na Dark Spot Amp", 1)
    prg.add(-2200000, "Na Repumper MOT Amp", 1)
    prg.add(-2100000, "Na Probe/Push (-) Amp", 1)
    prg.add(-2000000, "Shutter repump Na Open")
    prg.add(-1800000, "Na Probe/Push (+) Amp", 1)
    prg.add(-730000, "Na 3D MOT cool (-) Amp", 1, enable=False)
    prg.add(-720000, "Na 3D MOT cool (+) Amp", 1, enable=False)
    prg.add(-709600, "Shutter 3DMOT cool Na Open")
    prg.add(-2100, "Na Repumper MOT Amp", 1000)
    prg.add(-1600, "Na Repumper1 (+) Amp", 1000)
    prg.add(-1200, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-800, "Na Probe/Push (+) freq", 110.00)
    prg.add(-400, "Na Probe/Push (-) freq", 110.00)
    prg.add(-100, "Trig ON Stingray 1")
    prg.add(0, "Na Probe/Push (+) Amp", 1000)
    prg.add(400, "Na Probe/Push (-) Amp", 1000)
    prg.add(1400, "Na Probe/Push (-) Amp", 1)
    prg.add(2400, "Trig OFF Stingray 1")
    prg.add(250400, "Shutter Probe Na Close")
    prg.add(999900, "Trig ON Stingray 1")
    prg.add(1000400, "Na Probe/Push (-) Amp", 1000)
    prg.add(1001400, "Na Probe/Push (-) Amp", 1)
    prg.add(1002400, "Trig OFF Stingray 1")
    prg.add(1010400, "Na Repumper MOT Amp", 1)
    prg.add(1020400, "Na Repumper1 (+) Amp", 1)
    prg.add(1999900, "Trig ON Stingray 1")
    prg.add(2001900, "Trig OFF Stingray 1")
    prg.add(2999900, "Trig ON Stingray 1")
    prg.add(3001900, "Trig OFF Stingray 1")
    prg.add(4000400, "B comp y", 0.0000)
    prg.add(4010400, "IGBT B comp y OFF")
    return prg
