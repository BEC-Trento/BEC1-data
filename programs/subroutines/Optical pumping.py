prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "TTL Repumper MOT OFF")
    prg.add(10000, "TTL Repumper MOT ON")
    prg.add(20000, "TTL Repumper MOT OFF")
    prg.add(30000, "B comp x", 0.0)
    prg.add(40000, "B comp y", 0.4000)
    return prg
