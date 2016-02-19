prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3000000, "Shutter Probe Na Close")
    prg.add(-2000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-1600, "Na Repumper MOT Amp", 1.000000)
    prg.add(-1200, "K probe Repumper (+) Amp", 1.000000)
    prg.add(-800, "Na 2D MOT (+) Amp", 1.000000)
    prg.add(-400, "Na Zeeman slower (-) Amp", 1.000000)
    prg.add(0, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(400, "Na Dark Spot Amp", 1.000000)
    prg.add(800, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(1200, "K probe Cooler (-) Amp", 1.000000)
    prg.add(1600, "K Repumper 1p (+) Amp", 1.000000)
    prg.add(2400, "K Cooler 1p (-) Amp", 200.000000)
    prg.add(3600, "K Cooler 1p (-) Amp", 1.000000)
    prg.add(4200, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(4600, "Na 3D MOT cool (+) Amp", 1.000000)
    return prg
