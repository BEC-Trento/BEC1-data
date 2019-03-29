prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-100, "IGBT B comp z OFF")
    prg.add(0, "IGBT B comp z ON")
    return prg
