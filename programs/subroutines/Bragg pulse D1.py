prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-4500000, "Bragg OFF")
    prg.add(-4100000, "Shutter Gray molasses Open")
    prg.add(-4000000, "Shutter Phase Imprint Open")
    prg.add(-3500000, "Na Bragg ch1 Amp", 1)
    prg.add(-3400000, "Na Bragg ch2 Amp", 1)
    prg.add(-250000, "Shutter Phase Imprint Close")
    prg.add(-200000, "Shutter Gray molasses Close")
    prg.add(-10000, "Na Bragg relative freq", 0.00)
    prg.add(-1000, "Na Bragg ch2 Amp", 1000)
    prg.add(-500, "Na Bragg ch1 Amp", 1000)
    prg.add(0, "Bragg burst ON")
    prg.add(20, "Bragg burst OFF")
    prg.add(1000, "Na Bragg ch1 Amp", 1)
    prg.add(1500, "Na Bragg ch2 Amp", 1)
    prg.add(2200000, "Bragg ON")
    prg.add(3000000, "Na Bragg ch1 Amp", 1000)
    prg.add(3100000, "Na Bragg ch2 Amp", 1000)
    return prg
