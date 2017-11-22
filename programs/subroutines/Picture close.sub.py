prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-19000, "B comp y", 0.5000)
    prg.add(-19000, "Analog71", 0.5000, enable=False)
    prg.add(-10000, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-9000, "Na Repumper MOT Amp", 1000)
    prg.add(-8000, "Na Repumper1 (+) Amp", 1000)
    prg.add(-5000, "Na Probe/Push (+) freq", 120.00)
    prg.add(-4000, "Na Probe/Push (-) freq", 100.00)
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(2000, "Trig OFF Stingray 1")
    prg.add(999500, "Trig ON Stingray 1")
    prg.add(1000000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1001000, "Na Probe/Push (-) Amp", 1)
    prg.add(1002000, "Trig OFF Stingray 1")
    prg.add(1010000, "Na Repumper MOT Amp", 1)
    prg.add(1020000, "Na Repumper1 (+) Amp", 1)
    prg.add(1999500, "Trig ON Stingray 1")
    prg.add(2001500, "Trig OFF Stingray 1")
    prg.add(2999500, "Trig ON Stingray 1")
    prg.add(3001500, "Trig OFF Stingray 1")
    prg.add(4000000, "B comp y", 0.0000)
    return prg
