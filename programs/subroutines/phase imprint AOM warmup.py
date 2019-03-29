prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-5896000, "Shutter Phase Imprint Close")
    prg.add(0, "Bragg ON")
    prg.add(1000, "Phase Imprint 2016 ch1 Amp", 1000)
    return prg
