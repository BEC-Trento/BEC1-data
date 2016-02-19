prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-500, "Trig ON Stingray 1")
    prg.add(-480, "Na Probe/Push (-) freq", 110.000000)
    prg.add(-25, "Pulse uw ON")
    prg.add(-10, "Pulse uw OFF")
    prg.add(0, "Na Probe/Push (+) freq", 110.000000)
    prg.add(1000, "Na Probe/Push (+) freq", 150.000000)
    prg.add(1400, "Na Probe/Push (-) freq", 150.000000)
    prg.add(1500, "Trig OFF Stingray 1")
    return prg
