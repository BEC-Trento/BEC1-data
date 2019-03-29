prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-20000000, "Na Probe/Push (-) freq", 150.00)
    prg.add(-19500000, "Na 3D MOT cool (-) freq", 150.00)
    prg.add(-19200000, "Na 3D MOT cool (+) freq", 150.00)
    prg.add(-19000000, "Na Probe/Push (+) freq", 150.00)
    prg.add(-3000000, "Shutter Bragg Open")
    prg.add(-2990000, "Na Probe/Push (-) Amp", 1)
    prg.add(-2980000, "Na Probe/Push (+) Amp", 1)
    prg.add(-515500, "Shutter Bragg Close")
    prg.add(-57000, "Na Probe/Push (+) OFF")
    prg.add(-20000, "Na 3D MOT cool (-) OFF")
    prg.add(-6000, "Na 3D MOT cool", 100)
    prg.add(-5000, "Na Probe/Push", 1)
    prg.add(-2200, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(-1800, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(-1400, "Na Probe/Push (-) Amp", 1000)
    prg.add(-1000, "Na Probe/Push (+) Amp", 1000)
    prg.add(0, "Bragg ON")
    prg.add(100, "Bragg OFF")
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(2400, "Na 3D MOT cool (+) Amp", 1)
    prg.add(2800, "Na Probe/Push (-) Amp", 1)
    prg.add(3200, "Na Probe/Push (+) Amp", 1)
    prg.add(7800, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(8200, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(8600, "Na Probe/Push (-) Amp", 1000)
    prg.add(9000, "Na Probe/Push (+) Amp", 1000)
    prg.add(10000, "Bragg ON")
    prg.add(10100, "Bragg OFF")
    prg.add(12000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(12400, "Na 3D MOT cool (+) Amp", 1)
    prg.add(12800, "Na Probe/Push (-) Amp", 1)
    prg.add(13200, "Na Probe/Push (+) Amp", 1)
    prg.add(39000, "Na Probe/Push (+) ON")
    return prg
