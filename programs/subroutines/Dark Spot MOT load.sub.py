prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-400, "Na 3D MOT cool (-) freq", 120.00)
    prg.add(0, "Na Dark Spot Amp", 1000)
    prg.add(400, "Na Repumper MOT Amp", 1)
    prg.add(800, "Na 3D MOT cool (+) freq", 100.00)
    return prg
