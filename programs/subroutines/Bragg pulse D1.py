prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-6000000, "Shutter Bragg D1 Open")
    prg.add(-4500000, "Bragg OFF")
    prg.add(-1100000, "Shutter Bragg D1 Close")
    prg.add(-20000, "Na Bragg relative freq", 0.00)
    prg.add(-15000, "Na Bragg ch2 Amp", 1000)
    prg.add(-10000, "Na Bragg ch1 Amp", 1000)
    prg.add(0, "Bragg burst ON")
    prg.add(1500000, "Bragg burst OFF")
    prg.add(11010020, "Na Bragg ch1 Amp", 1000)
    prg.add(11110020, "Na Bragg ch2 Amp", 1000)
    prg.add(11210020, "Bragg ON")
    return prg
