prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-500, "Trig ON Stingray 2")
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(2000, "Trig OFF Stingray 2")
    prg.add(899500, "Trig ON Stingray 2")
    prg.add(900000, "Na Probe/Push (-) Amp", 1000)
    prg.add(901000, "Na Probe/Push (-) Amp", 1)
    prg.add(902000, "Trig OFF Stingray 2")
    prg.add(912000, "Na Repumper MOT Amp", 1)
    prg.add(922000, "Na Repumper1 (+) Amp", 1)
    prg.add(932000, "K Repumper 1p (+) Amp", 1)
    prg.add(1199500, "Trig ON Stingray 2")
    prg.add(1200000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1201000, "Na Probe/Push (-) Amp", 1)
    prg.add(1202000, "Trig OFF Stingray 2")
    prg.add(1469500, "Trig ON Stingray 2")
    prg.add(1470000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1471000, "Na Probe/Push (-) Amp", 1)
    prg.add(1472000, "Trig OFF Stingray 2")
    prg.add(1739500, "Trig ON Stingray 2")
    prg.add(1740000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1741000, "Na Probe/Push (-) Amp", 1)
    prg.add(1742000, "Trig OFF Stingray 2")
    return prg