prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4503000, "Shutter Probe Na Open")
    prg.add(-4403000, "Na Repumper1 (+) Amp", 1)
    prg.add(-4363000, "Na Dark Spot Amp", 1)
    prg.add(-4353000, "Na Repumper MOT Amp", 1)
    prg.add(-3513000, "Na Probe/Push (-) Amp", 1)
    prg.add(-3503000, "Na Probe/Push (+) Amp", 1)
    prg.add(-3013000, "Shutter repump Na Open")
    prg.add(-2030000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-2020000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-200500, "Trig ON Stingray 1")
    prg.add(-189500, "Trig OFF Stingray 1")
    prg.add(-1200, "Na Probe/Push (+) freq", 113.25)
    prg.add(-800, "Na Probe/Push (-) freq", 106.75)
    prg.add(-700, "Na Probe/Push (+) Amp", 1000)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(10500, "Trig OFF Stingray 1")
    return prg
