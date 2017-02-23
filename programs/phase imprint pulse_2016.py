prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5000000, "Shutter Phase Imprint Open")
    prg.add(-4995000, "Phase Imprint 2016 ch1 Amp", 1)
    prg.add(-4990000, "Bragg OFF")
    prg.add(-1000, "Phase Imprint 2016 ch1 Amp", 1000)
    prg.add(0, "Bragg burst ON")
    prg.add(1000, "Phase Imprint 2016 ch1 Amp", 1)
    prg.add(21000, "Bragg burst OFF")
    prg.add(31000, "Shutter Phase Imprint Close")
    prg.add(5000000, "Bragg ON")
    prg.add(5001000, "Phase Imprint 2016 ch1 Amp", 1000)
    return prg
