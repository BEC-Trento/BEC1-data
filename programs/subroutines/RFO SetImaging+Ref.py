prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4393000, "K probe Repumper (+) Amp", 1)
    prg.add(-4383000, "K Repumper 1p (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-4003000, "Shutter Probe Na Open")
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3013000, "Shutter repump Na Open")
    prg.add(-2493000, "K probe Cooler (-) Amp", 1)
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-1200, "Na Probe/Push (+) freq", 112.00)
    prg.add(-800, "Na Probe/Push (-) freq", 108.00)
    prg.add(-500, "Trig ON Stingray 1", enable=False)
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000, enable=False)
    prg.add(1000, "Na Probe/Push (-) Amp", 1, enable=False)
    prg.add(2000, "Trig OFF Stingray 1", enable=False)
    prg.add(302000, "Trig ON Stingray 2", enable=False)
    prg.add(302500, "Na Probe/Push (-) Amp", 1000, enable=False)
    prg.add(303500, "Na Probe/Push (-) Amp", 1, enable=False)
    prg.add(304500, "Trig OFF Stingray 2", enable=False)
    return prg
