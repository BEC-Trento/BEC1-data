prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-19000, "B comp y", 0.500000)
    prg.add(-2000, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(-1600, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(-1200, "Na Probe/Push (+) freq", 120.000000)
    prg.add(-1000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(-800, "Na Probe/Push (-) freq", 100.000000)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1500, "Trig OFF Stingray 1")
    prg.add(999500, "Trig ON Stingray 1")
    prg.add(1000000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1001000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1001500, "Trig OFF Stingray 1")
    prg.add(1010000, "Na Repumper MOT Amp", 1.000000)
    prg.add(1020000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2001500, "Trig OFF Stingray 1")
    prg.add(2999500, "Trig ON Stingray 1")
    prg.add(3001500, "Trig OFF Stingray 1")
    prg.add(4000000, "B comp y", 0.000000)
    return prg
