prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(500, "Na Probe/Push (-) Amp", 1000)
    prg.add(1500, "Na Probe/Push (-) Amp", 1)
    prg.add(2500, "Trig OFF Stingray 1")
    return prg
