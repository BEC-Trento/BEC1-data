prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-20000000, "Na Probe/Push (-) freq", 150.000000)
    prg.add(-19500000, "Na 3D MOT cool (-) freq", 150.000000)
    prg.add(-19200000, "Na 3D MOT cool (+) freq", 150.000000)
    prg.add(-19000000, "Na Probe/Push (+) freq", 150.000000)
    prg.add(-3000000, "Shutter Bragg Open")
    prg.add(-2990000, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-2980000, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-515500, "Shutter Bragg Close")
    prg.add(-157000, "Na Probe/Push (+) OFF")
    prg.add(-120000, "Na 3D MOT cool (-) OFF")
    prg.add(-116000, "Na 3D MOT cool", 1.000000)
    prg.add(-115000, "Na Probe/Push", 69.000000)
    prg.add(-112200, "Na 3D MOT cool (+) Amp", 1000.000000)
    prg.add(-111800, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(-111400, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(-111000, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(-110020, "TTL4-15 ON")
    prg.add(-110000, "Bragg ON")
    prg.add(-109930, "Bragg OFF")
    prg.add(-109400, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(-109000, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(-108600, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(-108200, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(-106000, "Na 3D MOT cool", 69.000000)
    prg.add(-105000, "Na Probe/Push", 1.000000)
    prg.add(-1600, "Na 3D MOT cool (+) Amp", 1000.000000)
    prg.add(-1200, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(-800, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(-400, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(0, "Bragg ON")
    prg.add(120, "Bragg OFF")
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(2400, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(2800, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3200, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(17800, "Na 3D MOT cool (+) Amp", 1000.000000)
    prg.add(18200, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(18600, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(19000, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(20000, "Bragg ON")
    prg.add(20120, "Bragg OFF")
    prg.add(22000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(22400, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(22799, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(23200, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(25560, "TTL4-15 OFF")
    prg.add(39000, "Na Probe/Push (+) ON")
    return prg
