prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-3000000, "Shutter repump Na Open")
    prg.add(-2500000, "Shutter EOM Na Open")
    prg.add(-2000000, "Shutter 3DMOT cool Na Open")
    prg.add(-2500, "Na Repumper1 (+) Amp", 1000)
    prg.add(-2000, "Na Repumper2 (+) Amp", 1000)
    prg.add(-1600, "Na Repumper Tune (+) freq", 1713.0)
    prg.add(-1000, "TTL Repumper MOT ON")
    return prg
