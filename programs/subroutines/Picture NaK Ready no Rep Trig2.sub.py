prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3011000, "IGBT B comp y OFF", enable=False)
    prg.add(-201000, "B comp y", 0.0500, enable=False)
    prg.add(-40000, "IGBT B comp y ON", enable=False)
    prg.add(-500, "Trig ON Stingray 2")
    prg.add(-400, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(2000, "Trig OFF Stingray 2")
    prg.add(999500, "Trig ON Stingray 2")
    prg.add(1000000, "Na Probe/Push (-) Amp", 1000)
    prg.add(1001000, "Na Probe/Push (-) Amp", 1)
    prg.add(1002000, "Trig OFF Stingray 2")
    prg.add(1010000, "Na Repumper MOT Amp", 1)
    prg.add(1020000, "Na Repumper1 (+) Amp", 1)
    prg.add(1999500, "Trig ON Stingray 2")
    prg.add(2001500, "Trig OFF Stingray 2")
    prg.add(2999500, "Trig ON Stingray 2")
    prg.add(3001500, "Trig OFF Stingray 2")
    prg.add(4000000, "B comp y", 0.0000, enable=False)
    prg.add(4010000, "IGBT B comp y OFF", enable=False)
    return prg
