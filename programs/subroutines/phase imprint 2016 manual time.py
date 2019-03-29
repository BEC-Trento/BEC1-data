prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5000000, "Shutter Phase Imprint Open")
    prg.add(-4995000, "Phase Imprint 2016 ch1 Amp", 1)
    prg.add(-4990000, "Bragg OFF")
    prg.add(-1000, "Phase Imprint 2016 ch1 Amp", 1000)
    prg.add(-50, "Bragg burst ON")
    prg.add(0, "Bragg ON")
    prg.add(100000, "Bragg OFF")
    prg.add(101000, "Phase Imprint 2016 ch1 Amp", 1)
    prg.add(121000, "Bragg burst OFF")
    prg.add(131000, "Shutter Phase Imprint Close")
    prg.add(5100000, "Bragg ON")
    prg.add(5101000, "Phase Imprint 2016 ch1 Amp", 1000)
    return prg
