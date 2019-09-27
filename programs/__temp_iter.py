prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(10000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(100000, "Na 3D MOT cool (-) OFF")
    prg.add(1000000, "Mirrors Imaging")
    prg.add(9000000, "Trig ON Stingray 1", enable=False)
    prg.add(9001000, "Trig OFF Stingray 1", enable=False)
    prg.add(10000000, "BEC_imaging", enable=False)
    prg.add(10000000, "DMD_imaging")
    prg.add(10000512, "Scope 1 Trigger ON", enable=False)
    prg.add(10000562, "Scope 1 Trigger OFF", enable=False)
    prg.add(20000000, "Na Probe/Push (+) ON")
    prg.add(20010000, "Shutter Probe Na Open")
    prg.add(20020000, "Na Probe/Push (+) Amp", 1000)
    prg.add(20030000, "Na Probe/Push (-) Amp", 1000)
    return prg
