prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Na Repumper (+)", 0)
    prg.add(10000, "TTL2-13 ON")
    prg.add(20000, "TTL2-15 ON")
    prg.add(40000, "Shutter repump Na Open")
    return prg
