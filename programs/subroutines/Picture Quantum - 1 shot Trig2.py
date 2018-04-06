prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-500, "Trig ON Stingray 2")
    prg.add(0, "Na Probe/Push (-) Amp", 1000)
    prg.add(1000, "Na Probe/Push (-) Amp", 1)
    prg.add(2000, "Trig OFF Stingray 2")
    return prg
