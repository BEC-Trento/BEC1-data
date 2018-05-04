prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT B comp x OFF")
    prg.add(10000, "IGBT B comp y OFF")
    prg.add(20000, "IGBT B comp z OFF")
    return prg
