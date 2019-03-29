prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-1000000, "Shutter Push Na Close")
    prg.add(-800, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-400, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(0, "Na 2D MOT (+) Amp", 1.000000)
    prg.add(780, "IGBT 5 Open")
    prg.add(790, "IGBT 4 Open")
    prg.add(800, "IGBT 3 Open")
    prg.add(810, "Na Dark Spot Amp", 1.000000)
    prg.add(1200, "Na Repumper MOT Amp", 1.000000)
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(2400, "Na 3D MOT cool (+) Amp", 1.000000)
    return prg
