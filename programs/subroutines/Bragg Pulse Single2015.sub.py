prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-20000000, "Na Bragg (+) freq", 110.00)
    prg.add(-19500000, "Na 3D MOT cool (-) freq", 150.00)
    prg.add(-19200000, "Na 3D MOT cool (+) freq", 150.00)
    prg.add(-19000000, "Na Bragg (-) freq", 110.00)
    prg.add(-4000000, "Shutter Bragg Open")
    prg.add(-500000, "Shutter Bragg Close")
    prg.add(-20000, "Bragg OFF")
    prg.add(-6000, "Na Bragg", 104)
    prg.add(-2200, "Na 3D MOT cool (+) freq", 110.00)
    prg.add(-1800, "Na 3D MOT cool (-) freq", 110.00)
    prg.add(-1400, "Na 3D MOT cool (+) Amp", 300)
    prg.add(-1000, "Na 3D MOT cool (-) Amp", 300)
    prg.add(0, "Bragg ON")
    prg.add(250000, "Bragg OFF")
    prg.add(310750, "Na 3D MOT cool (-) Amp", 1)
    prg.add(312750, "Na 3D MOT cool (+) Amp", 1)
    prg.add(2099000, "Na Bragg (-) Amp", 1000)
    prg.add(2149000, "Na Bragg (+) Amp", 1000)
    prg.add(2199000, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(5249000, "Na 3D MOT cool (-) Amp", 1000)
    return prg
