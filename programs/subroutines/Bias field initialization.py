prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Analog71", 0.3250)
    prg.add(10000, "B comp y", 0.0000)
    prg.add(20000, "B comp x", 0.0)
    return prg
