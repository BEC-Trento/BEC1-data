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
    prg.add(-57000, "Na Probe/Push (+) OFF")
    prg.add(-20000, "Na 3D MOT cool (-) OFF")
    prg.add(-6000, "Na 3D MOT cool", 68.000000)
    prg.add(-5000, "Na Probe/Push", 1.000000)
    prg.add(-2200, "Na 3D MOT cool (+) Amp", 1000.000000)
    prg.add(-1800, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(-1400, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(-1000, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(-20, "TTL4-15 ON")
    prg.add(0, "Bragg ON")
    prg.add(100, "Bragg OFF")
    prg.add(2000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(2400, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(2800, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(3200, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(37800, "Na 3D MOT cool (+) Amp", 1000.000000)
    prg.add(38200, "Na 3D MOT cool (-) Amp", 1000.000000)
    prg.add(38600, "Na Probe/Push (-) Amp", 1000.000000)
    prg.add(39000, "Na Probe/Push (+) Amp", 1000.000000)
    prg.add(40000, "Bragg ON")
    prg.add(40100, "Bragg OFF")
    prg.add(42000, "Na 3D MOT cool (-) Amp", 1.000000)
    prg.add(42400, "Na 3D MOT cool (+) Amp", 1.000000)
    prg.add(42800, "Na Probe/Push (-) Amp", 1.000000)
    prg.add(43200, "Na Probe/Push (+) Amp", 1.000000)
    prg.add(45560, "TTL4-15 OFF")
    prg.add(59000, "Na Probe/Push (+) ON")
    return prg
