prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(500, "Na Probe/Push (-) Amp", 1000)
    prg.add(1500, "Na Probe/Push (-) Amp", 1)
    prg.add(11000, "Trig OFF Stingray 1")
    prg.add(120000, "Trig ON Stingray 2")
    prg.add(120500, "Na Probe/Push (-) Amp", 1000)
    prg.add(121500, "Na Probe/Push (-) Amp", 1)
    prg.add(131000, "Trig OFF Stingray 2")
    return prg
