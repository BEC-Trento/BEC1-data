prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Na Repumper MOT/Dark Spot", 0)
    prg.add(10000, "TTL Repumper MOT ON")
    prg.add(20000, "TTL Dark Spot ON")
    prg.add(40000, "Shutter repump Na Open")
    return prg
