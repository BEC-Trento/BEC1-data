prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Na Repumper MOT Amp", 1000)
    prg.add(500, "Na Repumper1 (+) Amp", 1000)
    prg.add(1000, "Na Zeeman slower (-) Amp", 1000)
    prg.add(1500, "Na Probe/Push (-) Amp", 1000)
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(2500, "Na 2D MOT (-) Amp", 1000)
    prg.add(3000, "Na Dark Spot Amp", 1000)
    prg.add(3500, "Na Repumper2 (+) Amp", 1000)
    prg.add(4000, "Na Probe/Push (+) Amp", 1000)
    prg.add(4100, "Na Probe/Push (+) ON")
    prg.add(4500, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(5000, "Na 2D MOT (+) Amp", 1000)
    return prg
