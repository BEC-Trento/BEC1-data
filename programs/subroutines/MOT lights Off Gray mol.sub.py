prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-400, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-350, "Na Repumper MOT Amp", 1.000000)
    prg.add(0, "Na 2D MOT (+) Amp", 1.000000)
    prg.add(10, "Na Zeeman slower (-) Amp", 1.000000)
    prg.add(20, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(30, "Na Dark Spot Amp", 1.000000)
    prg.add(400, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(3000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(3400, "Na 3D MOT cool (+) Amp", 1.000000)
    return prg
