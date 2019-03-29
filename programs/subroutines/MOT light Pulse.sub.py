prg_comment=""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-19500000, "Na 3D MOT cool (-) freq", 150.00)
    prg.add(-19200000, "Na 3D MOT cool (+) freq", 150.00)
    prg.add(-9000000, "Na 3D MOT cool (-) Amp", 1)
    prg.add(-9000000, "Na 3D MOT cool (+) Amp", 1)
    prg.add(-8500000, "Shutter 3DMOT cool Na Close")
    prg.add(-5000000, "Shutter 3DMOT cool Na Open")
    prg.add(-20000, "Bragg OFF")
    prg.add(-16000, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(-8000, "Na 3D MOT cool (-) Amp", 1000)
    prg.add(-2200, "Na 3D MOT cool (+) freq", 110.00)
    prg.add(-1800, "Na 3D MOT cool (-) freq", 110.00)
    prg.add(0, "Bragg ON")
    prg.add(3000, "Bragg OFF")
    prg.add(1511750, "Na 3D MOT cool (-) Amp", 1)
    prg.add(1513750, "Na 3D MOT cool (+) Amp", 1)
    prg.add(2000000, "Na 3D MOT cool (+) Amp", 1000)
    prg.add(5050000, "Na 3D MOT cool (-) Amp", 1000)
    return prg
