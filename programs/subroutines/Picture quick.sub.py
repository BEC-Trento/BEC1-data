prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4400000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(-4350000, "Na Repumper MOT Amp", 1.000000)
    prg.add(-3010000, "Shutter repump Na Open")
    prg.add(-3000000, "Shutter Probe Na Open")
    prg.add(-2510000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-2500000, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-19000, "B comp y", 0.500000)
    prg.add(-15000, "Na Repumper Tune (+) freq", 1713.000000)
    prg.add(-10000, "Na Repumper MOT Amp", 1000.000000)
    prg.add(-9500, "Na Repumper1 (+) Amp", 1000.000000)
    prg.add(-2500, "Na Repumper MOT Amp", 1.000000)
    prg.add(-2000, "Na Repumper1 (+) Amp", 1.000000)
    prg.add(-1200, "Na Probe/Push (+) freq", 110.000000)
    prg.add(-800, "Na Probe/Push (-) freq", 110.000000)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(1500, "Trig OFF Stingray 1")
    prg.add(10000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(40000, "Shutter Probe Na Close")
    prg.add(100000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(104500, "Trig ON Stingray 1")
    prg.add(105000, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(106620, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(774500, "Trig OFF Stingray 1")
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2669500, "Trig OFF Stingray 1")
    prg.add(3702500, "Trig ON Stingray 1")
    prg.add(3704500, "Trig OFF Stingray 1")
    prg.add(4000000, "B comp y", 0.000000)
    return prg
