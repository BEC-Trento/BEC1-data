prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Trig ON Stingray 1")
    prg.add(20, "Na Probe/Push (-) freq", 110.000000)
    prg.add(500, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1500, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1900, "Na Probe/Push (-) freq", 150.000000)
    prg.add(2000, "Trig OFF Stingray 1")
    return prg
