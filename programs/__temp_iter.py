prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(20999500, "TTL3-12 ON")
    prg.add(21000000, "Bragg Pulse Single2015.sub")
    prg.add(21000500, "TTL3-12 OFF")
    return prg
