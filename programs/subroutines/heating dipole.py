prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "TTL2 5 OFF")
    prg.add(10000, "Bragg burst ON")
    prg.add(1710000, "TTL2 5 ON")
    prg.add(1910000, "Bragg burst OFF")
    return prg
