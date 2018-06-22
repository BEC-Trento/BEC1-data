prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL Repumper MOT ON")
    prg.add(100000, "Shutter Repump2 Open")
    prg.add(200000, "Shutter 3DMOT cool Na Close")
    prg.add(210000, "Na Repumper2 (+) Amp", 1000)
    return prg
