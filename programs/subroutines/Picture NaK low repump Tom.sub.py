prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4393000, "K probe Repumper (+) Amp", 1, enable=False)
    prg.add(-4383000, "K Repumper 1p (+) Amp", 1, enable=False)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3013000, "Shutter repump Na Open")
    prg.add(-2493000, "K probe Cooler (-) Amp", 1, enable=False)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-5400, "K probe Cooler (-) freq", 99.50, enable=False)
    prg.add(-5000, "K Cooler 2p (+) freq", 97.50, enable=False)
    prg.add(-4600, "K Repumper 1p (+) Amp", 1000, enable=False)
    prg.add(-4200, "K Repumper 1p (+) freq", 115.00, enable=False)
    prg.add(-3800, "K Repumper 2p (+) freq", 96.00, enable=False)
    prg.add(-2500, "Na Repumper MOT Amp", 300)
    prg.add(-2000, "Na Repumper1 (+) Amp", 1000)
    prg.add(-1600, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-1200, "Na Probe/Push (+) freq", 110.00)
    prg.add(-800, "Na Probe/Push (-) freq", 110.00)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(400, "K probe Cooler (-) Amp", 1000, enable=False)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(1400, "K probe Cooler (-) Amp", 1, enable=False)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(250000, "Shutter Probe Na Close")
    prg.add(999500, "Trig ON Stingray 1")
    prg.add(1000000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000400, "K probe Cooler (-) Amp", 1000, enable=False)
    prg.add(1001000, "Na Probe/Push (-) Amp", 1)
    prg.add(1001400, "K probe Cooler (-) Amp", 1, enable=False)
    prg.add(1002000, "Trig OFF Stingray 1")
    prg.add(1010000, "Na Repumper MOT Amp", 1)
    prg.add(1020000, "Na Repumper1 (+) Amp", 1)
    prg.add(1030000, "K Repumper 1p (+) Amp", 1, enable=False)
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2001500, "Trig OFF Stingray 1")
    prg.add(2999500, "Trig ON Stingray 1")
    prg.add(3001500, "Trig OFF Stingray 1")
    prg.add(4000000, "B comp y", 0.0000)
    prg.add(4010000, "IGBT B comp y OFF")
    return prg
